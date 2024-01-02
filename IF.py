# belajar if di python

is_day = False
is_night = False

if is_day:
    print("selamat siang ali")
elif is_night:
    print("selamat malam ali")
else :
    print("selamat suka-suka ali")

print("selamat menikmati hari")

# belajar kondisi operator perbandingan

nilai = 5

if nilai >= 8:
    print("nilai kamu A")
elif nilai >= 7:
    print("nilai kamu adalah B")
elif nilai >= 6:
    print("nilai kamu adalah C")
else :
    print("silahkan belajar dengan giat")


# operator logika

nama = "haidar ali akbar"

if len(nama) > 3 or True:
    print("selamat datang")
else:
    print("nama terlalu pendek")