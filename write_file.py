## belajar menulis file
text = open("belajar_python/family.txt", "a")

text.write("\naaliya - anak")

text.close()

files = open("belajar_python/family.txt", "w")

files.write("\naaliya - anak")

files.close()