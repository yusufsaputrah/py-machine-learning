import json

def fill_blanks(cell, replacements):
    text = "".join(cell['source'])
    for repl in replacements:
        if "____" in text:
            # handle either 8 underscores or 4 underscores
            import re
            text = re.sub(r'_{4,8}', repl, text, count=1)
    cell['source'] = [line + '\n' for line in text.split('\n')]
    if cell['source'][-1] == '\n':
        cell['source'].pop()

def process_clustering(filename):
    with open(filename, 'r') as f:
        nb = json.load(f)
        
    code_cells = [c for c in nb['cells'] if c['cell_type'] == 'code']
    
    reps = {
        1: ['pd.read_csv("dataset_clustering_project/bank_transactions_data_edited.csv")'],
        2: ['head'],
        3: ['df'],
        4: ['df'],
        5: ['corr', 'heatmap'],
        6: ['histplot', 'ax=axes[i]'],
        7: ['boxplot', "'CustomerOccupation'", "'TransactionAmount'", 'xticks'],
        8: ['isnull()'],
        9: ['duplicated()'],
        10: ['dropna', 'inplace', 'isnull()'],
        11: ['drop_duplicates', 'inplace', 'duplicated()'],
        12: ['df.columns', "'id'", 'lower', 'lower', 'drop', 'head'],
        13: ['select_dtypes', 'columns', 'LabelEncoder', 'fit_transform', 'head'],
        14: ['df'],
        15: ['quantile', 'quantile', 'Q3', 'Q1', 'lower_bound', 'upper_bound'],
        16: ['StandardScaler', 'fit_transform', 'head'],
        17: ['CustomerAge', 'CustomerAgeGroup', 'Rendah', 'Sedang', 'Tinggi', 'qcut', 'LabelEncoder', 'fit_transform', 'head'],
        18: ['copy', 'describe'],
        19: ['KElbowVisualizer', 'model', 'k', 'metric', 'fit', 'show'],
        20: ['KMeans', '2', 'fit'],
        21: ['joblib', 'model'],
        22: ['labels_', 'silhouette_score', 'labels'],
        23: ['PCA', '2', 'fit_transform', 'labels', 'scatterplot', 'hue'],
        24: ['PCA', '2', 'fit_transform', 'df_pca_array', 'KMeans', '2', 'fit', 'data_final'],
        25: ['joblib', 'kmeans_pca'],
        26: ['labels', 'groupby', "'Cluster'", 'agg', 'agg_summary'],
        27: ['rename', 'columns', 'inplace', 'head'],
        28: ['df_used'],
        29: ['inverse_transform', 'head'],
        30: ['encoders', 'column', 'inverse_transform', 'head'],
        31: ['groupby', 'agg', 'groupby', 'agg'],
        32: ['df_inverse'],
        33: ['df_inverse']
    }
    
    for i, c in enumerate(code_cells):
        if i in reps:
            fill_blanks(c, reps[i])
            
    with open(filename, 'w') as f:
        json.dump(nb, f, indent=1)

process_clustering('[Clustering]_Submission_Akhir_BMLP_Your_Name.ipynb')
print("Clustering filled!")

def process_classification(filename):
    with open(filename, 'r') as f:
        nb = json.load(f)
        
    code_cells = [c for c in nb['cells'] if c['cell_type'] == 'code']
    
    reps = {
        1: ['df', 'data_clustering_inverse'],
        2: ['df'],
        3: ['df', 'get_dummies', 'categorical_cols', 'head'],
        4: ['drop', '1', "'Target'", 'train_test_split', '0.2', 'y'],
        5: ['DecisionTreeClassifier', 'fit', 'X_train', 'y_train'],
        6: ['decision_tree_model'],
        7: ['RandomForestClassifier', 'random_state=42', 'fit', 'X_train', 'y_train'],
        8: ['predict', 'X_test', 'predict', 'X_test', 'y_test', 'y_pred_dt', 'y_test', 'y_pred_new'],
        9: ['joblib'],
        10: ["'n_estimators': [50, 100]", "'max_depth': [10, 20]", "'min_samples_split': [2, 5]", 'GridSearchCV', 'RandomForestClassifier', 'param_grid', 'fit', 'X_train', 'y_train'],
        11: ['predict', 'X_test', 'y_test', 'y_pred_tuning'],
        12: ['joblib']
    }
    
    for i, c in enumerate(code_cells):
        if i in reps:
            fill_blanks(c, reps[i])
            # For cell 9, replace <NAMA ALGORITMA-MU>
            if i == 9:
                text = "".join(c['source'])
                text = text.replace("<NAMA ALGORITMA-MU>", "RandomForest")
                c['source'] = [line + '\n' for line in text.split('\n')]
                if c['source'][-1] == '\n':
                    c['source'].pop()

    with open(filename, 'w') as f:
        json.dump(nb, f, indent=1)

process_classification('[Klasifikasi]_Submission_Akhir_BMLP_Your_Name.ipynb')
print("Classification filled!")
