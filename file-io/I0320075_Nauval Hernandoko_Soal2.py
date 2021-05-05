print("Selamat Datang di Program Biodata Trah Keluarga")
print("=================================")

#Ambil input dari user
nama = input("Nama : ")
nama_ortu = input("Nama ortu: ")
umur = input("Umur : ")
alamat = input("Alamat : ")
noHP = input("no HP : ")
Masuk_grup = input("sudah masuk grup keluarga?sudah/belum : ")
if Masuk_grup == "sudah":
    print("makasih telah mengisi biodata keluarga")
else:
    print("mohon masuk ke link berikut: http//whatssapp.com")

#format teks
teks = "Nama : {}\nnama_ortu : {}\numur : {}\nalamat : {}\nnoHP : {}\nMasuk_grup".format(nama, nama_ortu,umur, alamat, noHP, Masuk_grup)

#Buka file untuk ditulis
file_bio = open("biodata keluarga.txt", "w")

#tulis teks ke file
file_bio.write(teks)

#tutup file
file_bio.close()