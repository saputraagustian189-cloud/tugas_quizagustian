
nama = input("Nama : ")

if nama == "Andi":
    target = 70
elif nama == "Budi":
    target = 75
elif nama == "Citra":
    target = 80

print("Target nilai", nama, ":", target)

percobaan = 0
lulus = False

while percobaan < 3 and lulus == False:
    percobaan = percobaan + 1
    nilai = int(input("Nilai " + str(percobaan) + " : "))
    if nilai >= target:
        lulus = True

if lulus == True:
    print(nama, "berhasil lulus setelah", percobaan, "kali percobaan!")
else:
    print(nama, "tidak lulus setelah", percobaan, "kali percobaan!")