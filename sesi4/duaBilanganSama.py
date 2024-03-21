bil1 = int(input("Masukan Bilangan Pertama :"))
bil2 = int(input("Masukan Bilangan Kedua :"))
bil3 = int(input("Masukan Bilangan Keiga :"))


if (bil1 >= bil2 and bil2 > bil3):
    print("bilangan",bil3,"paling kecil")
    if bil2 == bil1:
        print("dan ada dua bilangan",bil1,"yang lebih besar dari",bil3)
elif bil3 > bil1 and bil3 > bil2:
    print("bilangan",bil3,"paling besar")
elif bil1 > bil2 and bil2 <= bil3 :
    print("bilangan",bil2,"paling kecil")
    if bil1 == bil3:
        print("dan ada 2 dua bilangan",bil1)
elif bil2 > bil1 and bil2 > bil3:
    print("bilangan",bil2,"paling besar")
elif bil3 >= bil2 and bil2 > bil1 :
    print("bilangan",bil1,"paling Kecil")
    if bil2 == bil3:
        print("dan ada 2 dua bilangan",bil2)
elif bil1 > bil2 and bil1 > bil3:
    print("bilangan",bil1,"paling besar")

else:
    print("Semua Bilangan Sama Besar atau input salah")