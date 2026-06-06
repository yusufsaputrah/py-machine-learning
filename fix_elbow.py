import json

def fix_elbow(filename):
    with open(filename, 'r') as f:
        nb = json.load(f)
        
    for c in nb['cells']:
        if c['cell_type'] == 'code':
            text = "".join(c['source'])
            if "visualizer = KElbowVisualizer(model," in text:
                text = text.replace("visualizer = KElbowVisualizer(model,", "visualizer = KElbowVisualizer(model, force_model=True,")
                c['source'] = [line + '\n' for line in text.split('\n')]
                if c['source'][-1] == '\n':
                    c['source'].pop()

    with open(filename, 'w') as f:
        json.dump(nb, f, indent=1)

fix_elbow('[Clustering]_Submission_Akhir_BMLP_Your_Name.ipynb')
print("Fixed elbow!")
