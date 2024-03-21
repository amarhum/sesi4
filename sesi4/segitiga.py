#Buatlah program yang menghitung luas dan keliling segitiga berdasarkan panjang sisi-sisinya. (Gunakan Rumus Heron)
a = int(input("Masukkan nilai sisi: "))
b = int(input("Masukkan nilai sisi: "))
c = int(input("Masukkan nilai sisi: "))

#Semi-perimeter
s = (a+b+c)/2

#Keliling
k = a+b+c

#Luas
l = (s * (s - a) * (s - b) * (s - c))
l1 = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("Keliling segitiga = ", k,"cm")
print("Luas segitiga = ", "√",l,"cm2 atau", "{:.2f}".format(l1), "cm2")