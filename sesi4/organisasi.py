#Buatlah program untuk menghitung kelayakan orang lulus organisasi X. Organisasi X memiliki kriteria untuk Anggota
#1. Perempuan dengan berat badan minimal 45kilo gram, maks 50 kilogram dan Tingginya minimal 165 cm dan Usianya kurang dari 20 tahun
#2. Laki-laki dengan berat badan maks 70 kilo dan Tingginya minimal 170 cm dan usianya maks 25 tahun
#3. Laki-laki dan Perempuan dengan nilai rata-rata Akademis 90 dan usianya kurang dari 30 tahun
#4. Laki-laki dan Perempuan yang Memiliki Skill Menembak, Memanah atau Berkuda
#Ke 4 Kriteria diatas akan diterima hanya dan hanya jika tidak memiliki anggota tubuh yang cacat.

def cek_kelayakan (jenis_kelamin, berat_badan, tinggi_badan, usia, memiliki_skill, nilai_ratarata):
    if jenis_kelamin == "perempuan":
        if berat_badan >=45 <=50 and tinggi_badan >= 165 and usia < 20:
            return True
    elif jenis_kelamin == "laki-laki":
        if berat_badan <= 70 and tinggi_badan >=170 and usia <= 25:
            return True
    elif nilai_ratarata >= 90 and usia < 30:
        return True
    elif memiliki_skill in ["Menembak", "Memanah", "Berkuda"]:
        return True
    else:
        return False

jenis_kelamin = input("Jenis kelamin anda (laki-laki/perempuan): ")
berat_badan = float(input("Berat badan: "))
tinggi_badan = float(input("Tinggi badan: "))
usia = int(input("Usia: "))
memiliki_skill = input("Skill yang anda miliki (Memanah/Menembak/Berkuda): ")
memiliki_cacat = input("Apakah anda memiliki cacat (ya/tidak): ")
nilai_ratarata = float(input("rata-rata nilai akademis: "))

if memiliki_cacat == "ya":
    print("Maaf, anda tidak lolos karena cacat")
elif cek_kelayakan (jenis_kelamin, berat_badan, tinggi_badan, usia, memiliki_skill, nilai_ratarata):
    print("Selamat anda lolos")
else:
    print("Maaf, anda tidak lolos karena tidak memenuhi syarat")
