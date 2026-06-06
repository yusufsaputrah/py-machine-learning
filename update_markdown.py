import json

def update_clustering(filename):
    with open(filename, 'r') as f:
        nb = json.load(f)
        
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            text = "".join(cell['source'])
            if "Menjelaskan karakteristik tiap cluster berdasarkan rentangnya sebelum **Inverse**" in text:
                cell['source'] = [
                    "## Menjelaskan karakteristik tiap cluster berdasarkan rentangnya sebelum **Inverse** (masih dalam kondisi **Scaled**).\n",
                    "1. **CLUSTER 0: (Nasabah Senior dengan Saldo Tinggi)**:\n",
                    "  - **Rata-rata (mean) CustomerAge:** 0.48 \n",
                    "  - **Rata-rata (mean) AccountBalance:** 0.36 \n",
                    "  - **Analisis:** Cluster ini berisi nasabah yang lebih tua dibandingkan rata-rata, dengan saldo akun yang lebih tinggi di atas rata-rata.\n",
                    "\n",
                    "2. **CLUSTER 1: (Nasabah Muda dengan Saldo Rendah)**:\n",
                    "  - **Rata-rata (mean) CustomerAge:** -1.17 \n",
                    "  - **Rata-rata (mean) AccountBalance:** -0.88 \n",
                    "  - **Analisis:** Cluster ini berisi nasabah yang berusia jauh di bawah rata-rata (anak muda), dengan saldo akun di bawah rata-rata.\n"
                ]
            elif "Menjelaskan karakteristik tiap cluster berdasarkan rentangnya setelah **Inverse**" in text:
                cell['source'] = [
                    "## Menjelaskan karakteristik tiap cluster berdasarkan rentangnya setelah **Inverse**.\n",
                    "1. **CLUSTER 0: (Nasabah Senior dengan Saldo Tinggi)**:\n",
                    "  - **Rata-rata (mean) CustomerAge:** 52.74 tahun \n",
                    "  - **Rata-rata (mean) AccountBalance:** 6452.79 \n",
                    "  - **Analisis:** Nasabah di cluster ini rata-rata berusia 52 tahun dengan rentang 26 hingga 80 tahun. Mereka memiliki saldo akun rata-rata yang tinggi (sekitar 6452).\n",
                    "\n",
                    "2. **CLUSTER 1: (Nasabah Muda dengan Saldo Rendah)**:\n",
                    "  - **Rata-rata (mean) CustomerAge:** 23.54 tahun \n",
                    "  - **Rata-rata (mean) AccountBalance:** 1677.39 \n",
                    "  - **Analisis:** Nasabah di cluster ini adalah anak muda dengan rata-rata usia 23 tahun (rentang 18 hingga 32 tahun). Saldo akun rata-rata mereka lebih rendah (sekitar 1677).\n"
                ]

    with open(filename, 'w') as f:
        json.dump(nb, f, indent=1)

if __name__ == '__main__':
    update_clustering('[Clustering]_Submission_Akhir_BMLP_Your_Name.ipynb')
    print("Markdown updated!")
