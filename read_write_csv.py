import csv


with open("belajar_python/csv.csv", "r") as users:
    users = csv.reader(users, delimiter=";")

    for row in users:
        print(f"Name : {row[0]}. Role : {row[1]}")

