def celsiusToFahrenheit(cc):
    return (cc * 9/5) + 32

def fahrenheitToCelsius(fh):
    return (fh - 32) * 5/9

print("Konversi Suhu")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")

pilih = input("Masukkan pilihan (1/2): ")

if pilih == '1':
    celsius = float(input("Masukkan suhu dalam Celsius: "))
    fahrenheit = celsiusToFahrenheit(celsius)
    print(celsius,"derajat Celsius sama dengan",fahrenheit,"derajat Fahrenheit")
elif pilih == '2':
    fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
    celsius = fahrenheitToCelsius(fahrenheit)
    print(fahrenheit ,"derajat Fahrenheit sama dengan", celsius, "derajat Celsius")
else:
    print("Input salah")
