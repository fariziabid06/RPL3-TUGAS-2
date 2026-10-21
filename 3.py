kategori = ["atk", "elektronik", "makanan"]

kategori[1] = "Gadget"
kategori.append("Kebersihan")
kategori.insert(1, "Furnitur")
kategori.remove("makanan")
terakhir = kategori.pop()
del kategori[0]

print(kategori)