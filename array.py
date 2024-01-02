# belajar array di python
nama = ["haidar", "ali", "akbar", "syifa"]
print(nama[0])
print(nama[1:3])

for name in nama:
    print(f"nama : {name}")

# belajar method array di python
angka = [5, 6, 7, 8, 1]
print(angka)

angka.append(99)
print(angka)

angka.insert(2, 1500)
print(angka)

angka.pop(5)
print(angka)

angka.remove(5)
print(angka)

angka.sort()
print(angka)

# belajar menjumlahkan list

numbers = [5, 6, 7, 8, 11]

init_number = 0

for number in numbers:
    init_number = init_number + number
    print(init_number)