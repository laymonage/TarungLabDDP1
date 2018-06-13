'''
Program translasi kalimat surgawi ke kalimat duniawi

Pada dasarnya, kalimat surgawi adalah suatu bilangan dalam basis 10
dan kalimat duniawi adalah representasi kalimat surgawi dalam basis 2,
namun huruf B dan P digunakan untuk menyatakan 1 dan 0 berturut-turut.

Program akan meminta input dalam kalimat surgawi, dan mengeluarkan
output berupa translasi kalimat surgawi ke kalimat duniawi.
'''


# Meminta input dari user berupa kalimat surgawi
surgawi = int(input("Masukkan kalimat surgawi: "))

# Menginisialisasi string duniawi yang masih kosong
duniawi = ""

# Pengulangan untuk konversi dari kalimat surgawi ke duniawi,
# menggunakan konsep konversi bilangan desimal ke bilangan biner
while surgawi != 0:                   # Diteruskan hingga bilangan habis
    if surgawi % 2 == 0:              # Jika bilangan genap, maka
        duniawi = 'P' + duniawi       # Tambahkan P di depan string
    else:                             # Jika ganjil, maka
        duniawi = 'B' + duniawi       # Tambahkan B di depan string
    surgawi //= 2                     # Bagi bilangan dengan 2, ulangi proses

# Cetak hasil akhir string duniawi
print("Makna duniawi:", duniawi)
