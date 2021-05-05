#membaca teks per baris
# buka file
file_puisi = open("puisi.txt", "r")

# baca isi file
print(file_puisi.readlines())

# tutup file
file_puisi.close()

#membaca semua teks
# buka file
file_puisi = open("puisi.txt", "r")

# baca isi file
puisi = file_puisi.read()

# cetak isi file
print(puisi)

# tutup file
file_puisi.close()

#menulis dengan metode 'w'
print("Selamat Datang di Program Biodata")
print("=================================")

#Ambil input dari user
nama = input("Nama : ")
umur = input("Umur : ")
alamat = input("Alamat : ")

#format teks
teks = "Nama : {}\nUmur : {}\nAlamat : {}".format(nama, umur, alamat)

#Buka file untuk ditulis
file_bio = open("biodata.txt", "w")

#tulis teks ke file
file_bio.write(teks)

#tutup file
file_bio.close()

#menyisipkan data ke file
print("Selamat Datang di Program Biodata")
print("=================================")

#Ambil input dari user
nama = input("Nama : ")
umur = input("Umur : ")
alamat = input("Alamat : ")

#format teks
teks = "Nama : {}\nUmur : {}\nAlamat : {}".format(nama, umur, alamat)

#Buka file untuk ditulis
file_bio = open("biodata.txt", "a")

#tulis teks ke file
file_bio.write(teks)

#membuat direktori
#Nama_File: mkdir.py

import os

def main():
    os.mkdir("unit")

ifname = 'main'

main()