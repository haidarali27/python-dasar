# belajar membuat app angka terbilang

angka = input("masukkan angka : ")

angka_mapping = {
    "1" : "satu",
    "2" : "dua",
    "3" : "tiga",
    "4" : "empat",
    "5" : "lima",
    "6" : "enam",
    "7" : "tujuh",
    "8" : "delapan",
    "9" : "sembilan",
}

output = ""

for n in angka:
    terbilang = angka_mapping.get(n, "invalid")
output = output + terbilang + " "

print(output)