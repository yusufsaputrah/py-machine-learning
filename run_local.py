import json
import nbformat
from nbclient import NotebookClient

filename = '[Clustering]_Submission_Akhir_BMLP_Your_Name.ipynb'

# 1. Inject SSL bypass
with open(filename, 'r') as f:
    nb = json.load(f)
    
code_cells = [c for c in nb['cells'] if c['cell_type'] == 'code']
# Insert SSL bypass into the very first code cell
code_cells[0]['source'].insert(0, "import ssl\nssl._create_default_https_context = ssl._create_unverified_context\n")

with open(filename, 'w') as f:
    json.dump(nb, f, indent=1)

# 2. Execute
for nb_path in ['[Clustering]_Submission_Akhir_BMLP_Your_Name.ipynb', '[Klasifikasi]_Submission_Akhir_BMLP_Your_Name.ipynb']:
    print(f"Executing {nb_path}...")
    with open(nb_path) as f:
        nb_obj = nbformat.read(f, as_version=4)
    client = NotebookClient(nb_obj, timeout=600, kernel_name='python3')
    client.execute()
    with open(nb_path, 'w') as f:
        nbformat.write(nb_obj, f)
    print(f"Done with {nb_path}")

# 3. Remove SSL bypass
with open(filename, 'r') as f:
    nb = json.load(f)

code_cells = [c for c in nb['cells'] if c['cell_type'] == 'code']
if code_cells[0]['source'][0].startswith("import ssl"):
    code_cells[0]['source'].pop(0)
    code_cells[0]['source'].pop(0)

with open(filename, 'w') as f:
    json.dump(nb, f, indent=1)

print("Finished completely.")
