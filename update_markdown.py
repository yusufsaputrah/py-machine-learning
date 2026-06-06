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
                    "  - **Rata-rata (mean) CustomerAge:** 0.02 \n",
                    "  - **Rata-rata (mean) AccountBalance:** 0.01 \n",
                    "  - **Rata-rata (mean) TransactionAmount:** -0.01 \n",
                    "  - **Analisis:** Cluster 0 merepresentasikan kelompok nasabah yang usianya sedikit lebih tua dari rata-rata keseluruhan populasi (terlihat dari nilai CustomerAge positif) dengan jumlah saldo akun yang juga berada di atas rata-rata. Namun, rata-rata nominal transaksi yang dilakukan cenderung lebih rendah (negatif).\n",
                    "\n",
                    "2. **CLUSTER 1: (Nasabah Muda dengan Transaksi Aktif)**:\n",
                    "  - **Rata-rata (mean) CustomerAge:** -0.02 \n",
                    "  - **Rata-rata (mean) AccountBalance:** -0.01 \n",
                    "  - **Rata-rata (mean) TransactionAmount:** 0.01 \n",
                    "  - **Analisis:** Cluster 1 adalah kelompok nasabah yang berusia sedikit lebih muda di bawah rata-rata keseluruhan populasi (nilai CustomerAge negatif) dengan saldo yang juga relatif lebih rendah. Namun, rata-rata jumlah transaksi yang dilakukan sedikit lebih tinggi (positif), menandakan tingkat pengeluaran/transaksi yang lebih besar.\n"
                ]
            elif "Menjelaskan karakteristik tiap cluster berdasarkan rentangnya setelah **Inverse**" in text:
                cell['source'] = [
                    "## Menjelaskan karakteristik tiap cluster berdasarkan rentangnya setelah **Inverse**.\n",
                    "1. **Cluster 0: (Nasabah Senior dengan Saldo Tinggi)**:\n",
                    "  - **Rata-rata (mean) CustomerAge:** 45.06 \n",
                    "  - **Rata-rata (mean) AccountBalance:** 5142.17 \n",
                    "  - **Rata-rata (mean) TransactionAmount:** 255.55 \n",
                    "  - **Analisis:** Dari data asli yang telah dikembalikan rentangnya, terlihat jelas bahwa Cluster 0 berisi nasabah dengan rata-rata umur sekitar 45 tahun, memiliki tabungan mencapai 5142.17, namun jumlah rata-rata nilai transaksinya berada di kisaran 255.55.\n",
                    "\n",
                    "2. **Cluster 1: (Nasabah Muda dengan Transaksi Aktif)**:\n",
                    "  - **Rata-rata (mean) CustomerAge:** 44.33 \n",
                    "  - **Rata-rata (mean) AccountBalance:** 5058.81 \n",
                    "  - **Rata-rata (mean) TransactionAmount:** 258.15 \n",
                    "  - **Analisis:** Cluster 1 secara nyata memuat nasabah dengan rata-rata umur lebih muda, yakni sekitar 44.33 tahun, dengan rata-rata tabungan sebesar 5058.81. Mereka secara riil lebih aktif bertransaksi dengan jumlah nominal rata-rata di angka 258.15.\n"
                ]

    with open(filename, 'w') as f:
        json.dump(nb, f, indent=1)

update_clustering('[Clustering]_Submission_Akhir_BMLP_Your_Name.ipynb')
print("Markdown updated!")
