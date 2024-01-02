# belajar string

nama = "haidar ali akbar"
print(nama[0:6])

name = "haidar ali akbar"
print(name[-2])

# belajar formatted string
first_name = "haidar ali"
last_name = "akbar"

pesan = f"{first_name} [{last_name}]"
print(pesan)

umur = 24
umur_kamu = f"umur kamu {umur}"
print(umur_kamu)


# string method

kursus = "belajar python bareng haidar ali akbar"
bahasa = "javascript"
panjang = len(kursus)
print(panjang)

jeneng = "Haidar Ali Akbar"
jeneng_besar = jeneng.upper()
jeneng_kecil = jeneng.lower()
print(jeneng_besar)
print(jeneng_kecil)

print(bahasa in kursus)


