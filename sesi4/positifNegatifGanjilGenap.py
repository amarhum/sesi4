angka = float(input("masukan angka :"))


if angka < 0:
    print(angka,"itu bilangan negatif")
    if angka %2 == 0:
        print("dan",angka,"itu bilangan genap")
    else:
        print("itu bilangan ganjil")
elif angka > 0:
    print(angka,"itu bilangan positif")
    if angka %2 == 0:
        print("dan",angka,"itu bilangan genap")
    else:
        print("dan",angka,"itu bilangan ganjil")
else:
    print(angka,"adalah bilangan netral")