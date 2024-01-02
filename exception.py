try:

    level = input("masukin level kamu : ")
    level = int(level)
    print(level)

except ValueError:
    print("yang diinput bukanlah angka")