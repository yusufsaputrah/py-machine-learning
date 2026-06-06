import json

def fix_cell1(filename):
    with open(filename, 'r') as f:
        nb = json.load(f)
        
    for c in nb['cells']:
        if c['cell_type'] == 'code':
            text = "".join(c['source'])
            if "df = pd.read_csv(\"dataset_clustering_project/bank_transactions_data_edited.csv\")" in text:
                text = text.replace("pd.read_csv(\"dataset_clustering_project/bank_transactions_data_edited.csv\")", "pd.read_csv(url)")
                c['source'] = [line + '\n' for line in text.split('\n')]
                if c['source'][-1] == '\n':
                    c['source'].pop()

    with open(filename, 'w') as f:
        json.dump(nb, f, indent=1)

fix_cell1('[Clustering]_Submission_Akhir_BMLP_Your_Name.ipynb')
print("Fixed cell 1!")
