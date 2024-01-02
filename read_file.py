## membaca isi file dengan python
users = open("belajar_python/family.txt", "r")

array = users.readlines()

print(array)

users.close()
