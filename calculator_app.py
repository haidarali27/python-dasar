# belajar membuat app calculator

perintah = ""

while perintah != "exit":
    perintah = input("Perintah : ")


    if perintah == "exit":
        break

    if perintah != "+" and perintah != "-" and perintah != "/" and perintah != "*":
        print("perintah tidak dikenali")
        continue

    a = int(input("masukkan angka pertama : "))
    b = int(input("masukkan angka kedua : "))

    if perintah == "+":
        hasil = a + b
    elif perintah == "-":
        hasil = a - b
    elif perintah == "/":
        hasil = a / b
    elif perintah == "*":
        hasil = a * b

    print(f"hasil : {hasil}")

print("terimakasih sudah mau bermain")