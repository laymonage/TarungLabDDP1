'''
Program pengekstrak informasi rahasia Agen Benny.

Program yang menerima input berupa pesan yang dibaca terbalik setiap 
panjang karakter 'key'. 

'''
input_pesan = input("Pesan: ")
key = int(input("Key: "))
hasil = ''                              # Hasil dari string split akan di simpan ke variabel ini
banyak_loop = len(input_pesan)//key     # Menentukan banyaknya iterasi yang perlu dilakukan
for i in range(banyak_loop):            # Iterasi setiap panjang karakter = key
    hasil += input_pesan[key-1::-1]     # Mengambil string dari index ke key hingga 0
    input_pesan = input_pesan[key:]     # Menghapus karakter yang sudah diperbaiki

hasil += input_pesan[::-1]              # Sisa dari karakter yang belum diperbaiki ditambahkan ke hasil
print(hasil)