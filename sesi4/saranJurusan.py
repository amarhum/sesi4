nama = str(input("Masukan Nama anda : "))
tmptLahir = str(input("Tempat Lahir :"))
tglLahir = int(input("tanggal lahir :"))
thnLahir = int(input("tahun lahir : "))
jnsKelamin = str(input("Jenis Kelamin Anda :"))
print("=== Masukan 3 Nilat Mata Kuliah === ")
english = float(input("Masukan Nila English :"))
mtk = float(input("Masukan Nila Mtk :"))
indonesia = float(input("Masukan Nila Indonesia :"))

rata = (english + mtk + indonesia)/3

def jenis(jk):
    if(jk == "laki laki"):
        return 1
    elif(jk == "perempuan"):
        return 2
    else:
        return 3

def umur(tahun):
    if(2024 - tahun ) < 25 and (2024 - tahun ) >= 18:
        return 1
    elif(2024 - tahun) >= 25:
        return 4
    else:
        return 5
    
def saran():
    if(jenis(jnsKelamin) + umur(thnLahir)) == 2:
        return 1
    elif(jenis(jnsKelamin) + umur(thnLahir)) == 3:
        return 2
    elif(jenis(jnsKelamin) + umur(thnLahir)) == 5:
        return 3
    elif(jenis(jnsKelamin) + umur(thnLahir)) == 6:
        return 4
    else:
        return "salah"
    

if(rata >= 80  and saran() == 1):
    print("anda disarankan masuk jurusan Teknik Informatika")
elif(rata >= 80 and saran() == 2):
    print("Anda disarankan Masuk Jurusan Sistem Informasi")
elif(rata >= 80 and saran() == 3):
    print("anda tidak di terima karna umur anda 25 thn atau kurang dari 18 thn")
elif(rata >= 80 and saran() == 4):
    print("anda tidak di terima karna umur anda 25 thn atau kurang dari 18 thn")
elif(rata >= 80 and jenis(jnsKelamin) == 3):
    print("Input jenis kelamin harus ==laki laki== atau ==perempuan== ")
elif(rata < 80 and saran() == 1):
    print("anda disarankan masuk jurusan DKV")
elif(rata < 80 and saran() == 2):
    print("anda disarankan masuk jurusan DKV")
elif(rata < 80 and jenis(jnsKelamin) == 3):
    print("Input jenis kelamin harus ==laki laki== atau ==perempuan== ")
    