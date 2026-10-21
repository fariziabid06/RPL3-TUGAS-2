jumlah_stok = [25, 8, 0, 12, 40, 4]

print(sum(jumlah_stok))
print(min(jumlah_stok))
print(max(jumlah_stok))

jumlah_stok.sort(reverse=True)
print(jumlah_stok[:3])
stok2 = [x for x in jumlah_stok if x < 10]
print(stok2)