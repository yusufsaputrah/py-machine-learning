import nbformat
from nbclient import NotebookClient

for nb_path in ['[Clustering]_Submission_Akhir_BMLP_Your_Name.ipynb', '[Klasifikasi]_Submission_Akhir_BMLP_Your_Name.ipynb']:
    print(f"Executing {nb_path}...")
    with open(nb_path) as f:
        nb = nbformat.read(f, as_version=4)
    client = NotebookClient(nb, timeout=600, kernel_name='python3')
    client.execute()
    with open(nb_path, 'w') as f:
        nbformat.write(nb, f)
    print(f"Done with {nb_path}")
