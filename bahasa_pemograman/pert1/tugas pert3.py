from calendar import prweek
from builtin import float, input, print


Nama=input("Masukkan Nama:")
Nim=input("Masukkan Nim:")
Mata_kuliah=input("Masukkan Mata Kuliah:")
Absen=float(input("Masukkan Nilai Absensi:"))
Tugas=float(input("Masukkan Nilai Tugas:"))
UTS=float(input("Masukkan Nilai UTS:"))
UAS=float(input("Masukkan Nilai UAS:"))

R_absen = (Absen *20/100)
R_Tugas = (Tugas *25/100)
R_UTS = (UTS *25/100)
R_UTS = (UAS *30/100)

nilai_akhir = R_absen + R_Tugas + R_UTS + R_Tugas

print("Nama: "+Nama)
print("Nim: "+Nim)
print("Matkul:"+(Mata_kuliah))
print("Nilai Akhir:",(nilai_akhir))

if nilai_akhir >= 80:
    print("Grade : A")
elif nilai_akhir >= 75:
    print("Grade : B")
elif nilai_akhir >= 60:
     print("Grade : C")
elif nilai_akhir >= 41:
    print("Grade : D")
elif nilai_akhir >= 0:
     print("Grade : E")

if nilai_akhir >=60:
    print("Keterangan : LULUS")
else:
    print("Keterangan : Tidak LULUS")