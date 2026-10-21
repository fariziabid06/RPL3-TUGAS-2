kategori = ["atk", "elektronik", "makanan"]

for k in kategori:
    print(k)

for nomor, k in enumerate(kategori, start=1):
    print(f"{nomor}.{k}")