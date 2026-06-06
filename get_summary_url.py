import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans

# 1. Load data
df = pd.read_csv('data_from_url.csv')

# 2. Clean data
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

cols_to_drop = [col for col in df.columns if 'id' in col.lower() or 'ip' in col.lower() or 'date' in col.lower()]
df = df.drop(columns=cols_to_drop)

# 3. Encoding
categorical_cols = list(df.select_dtypes(include=['object']).columns)
encoders = {}
for column in categorical_cols:
    label_encoder = LabelEncoder()
    df[column] = label_encoder.fit_transform(df[column])
    encoders[column] = label_encoder

# 4. Outliers
numerical_cols = df.select_dtypes(include=['number']).columns
numerical_cols = list(numerical_cols)
for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

# 5. Scaling
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# 6. Binning
col_to_bin = 'CustomerAge'
new_col_name = 'CustomerAgeGroup'
bin_labels = ['Rendah', 'Sedang', 'Tinggi']
df[new_col_name] = pd.qcut(df[col_to_bin], q=3, labels=bin_labels, duplicates='drop')
label_encoder = LabelEncoder()
df[new_col_name] = label_encoder.fit_transform(df[new_col_name])
encoders[new_col_name] = label_encoder
categorical_cols.extend([new_col_name])

df_used = df.copy()

# 7. Model
model = KMeans(n_clusters=2, random_state=42)
model.fit(df)

df_used['Cluster'] = model.labels_

agg_summary = df_used.groupby('Cluster')[numerical_cols].agg(['mean', 'min', 'max']).round(2).T
print("SCALED SUMMARY:")
print(agg_summary)

df_used.rename(columns={"Cluster": "Target"}, inplace=True)
df_inverse = df_used.copy()

df_inverse[numerical_cols] = scaler.inverse_transform(df_inverse[numerical_cols])
for column in categorical_cols:
    encoder = encoders[column]
    df_inverse[column] = encoder.inverse_transform(df_inverse[column].astype(int))

agg_summary_num = df_inverse.groupby('Target')[numerical_cols].agg(['mean', 'min', 'max']).round(2).T
print("\nINVERSE SUMMARY NUM:")
print(agg_summary_num)

