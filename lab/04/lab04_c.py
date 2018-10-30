'''
Program pengekstrak informasi rahasia Agen Benny.

Program yang menerima input berupa pesan yang dibaca
terbalik setiap panjang karakter 'key'.
'''
input_pesan = input("Pesan: ")
key = int(input("Key: "))
hasil = ''
# Menentukan banyaknya iterasi yang perlu dilakukan
banyak_loop = len(input_pesan)//key
for i in range(banyak_loop):
    # Mengambil string dari index ke key hingga 0
    hasil += input_pesan[key-1::-1]
    # Menghapus karakter yang sudah diperbaiki
    input_pesan = input_pesan[key:]
hasil += input_pesan[::-1]
print(hasil)
