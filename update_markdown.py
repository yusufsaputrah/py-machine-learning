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
                    "  - **Analisis:** Cluster 0 merepresentasikan kelompok nasabah yang usianya sedikit lebih tua dari rata-rata (terlihat dari nilai mean CustomerAge 0.02 dengan variasi rentang nilai min -1.50 hingga max 1.99). Saldo akun mereka juga di atas rata-rata (mean 0.01, min -1.28, max 2.52). Namun, rata-rata nominal transaksi yang dilakukan cenderung lebih rendah (mean -0.01, min -1.17, max 2.96).\n",
                    "\n",
                    "2. **CLUSTER 1: (Nasabah Muda dengan Transaksi Aktif)**:\n",
                    "  - **Rata-rata (mean) CustomerAge:** -0.02 \n",
                    "  - **Rata-rata (mean) AccountBalance:** -0.01 \n",
                    "  - **Rata-rata (mean) TransactionAmount:** 0.01 \n",
                    "  - **Analisis:** Cluster 1 adalah kelompok nasabah yang berusia sedikit lebih muda di bawah rata-rata (mean CustomerAge -0.02, rentang min -1.50 hingga max 1.99) dengan saldo yang relatif lebih rendah (mean -0.01, min -1.28, max 2.53). Namun, rata-rata jumlah transaksi yang dilakukan sedikit lebih tinggi (mean 0.01, min -1.18, max 2.90), menandakan tingkat transaksi yang lebih aktif.\n"
                ]
            elif "Menjelaskan karakteristik tiap cluster berdasarkan rentangnya setelah **Inverse**" in text:
                cell['source'] = [
                    "## Menjelaskan karakteristik tiap cluster berdasarkan rentangnya setelah **Inverse**.\n",
                    "1. **Cluster 0: (Nasabah Senior dengan Saldo Tinggi)**:\n",
                    "  - **Rata-rata (mean) CustomerAge:** 45.06 \n",
                    "  - **Rata-rata (mean) AccountBalance:** 5142.17 \n",
                    "  - **Rata-rata (mean) TransactionAmount:** 255.55 \n",
                    "  - **Analisis:** Dari data asli yang telah dikembalikan rentangnya, terlihat jelas bahwa Cluster 0 berisi nasabah dengan rata-rata umur sekitar 45.06 tahun (merentang dari nilai min 18.00 hingga max 80.00 tahun). Mereka memiliki rata-rata tabungan 5142.17 (min 117.98, max 14942.78), namun jumlah rata-rata nilai transaksinya berada di kisaran 255.55 (min 0.32, max 903.19).\n",
                    "\n",
                    "2. **Cluster 1: (Nasabah Muda dengan Transaksi Aktif)**:\n",
                    "  - **Rata-rata (mean) CustomerAge:** 44.33 \n",
                    "  - **Rata-rata (mean) AccountBalance:** 5058.81 \n",
                    "  - **Rata-rata (mean) TransactionAmount:** 258.15 \n",
                    "  - **Analisis:** Cluster 1 secara nyata memuat nasabah dengan rata-rata umur sedikit lebih muda yakni 44.33 tahun (min 18.00, max 80.00 tahun) dengan rata-rata tabungan 5058.81 (min 102.20, max 14977.99). Mereka secara riil lebih aktif bertransaksi dengan jumlah nominal rata-rata 258.15 (min 0.26, max 889.01).\n"
                ]

    with open(filename, 'w') as f:
        json.dump(nb, f, indent=1)

update_clustering('[Clustering]_Submission_Akhir_BMLP_Your_Name.ipynb')
print("Markdown updated keeping template structure intact!")
