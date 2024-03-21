#Program yang mensimulasikan permainan batu-gunting-kertas antara dua pemain dan menentukan pemenangnya.
p1 = input("Pemain ke 1 masukkan pilihan (batu/gunting/kertas): ")
p2 = input("Pemain ke 1 masukkan pilihan (batu/gunting/kertas): ")

if p1==p2:
    print("Kedua pemain seri")
elif (p1=="batu" and p2=="gunting") or (p1=="gunting" and p2=="kertas") or (p1=="kertas" and p2=="batu"):
    print("p1 menang")
else:
    print("p2 menang")