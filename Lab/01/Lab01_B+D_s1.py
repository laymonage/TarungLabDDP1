# Program gambar bentuk anak tangga

# Menggambar 3 buah anak tangga
# dengan panjang anak tangga berdasarkan
# input dari user.

# Inisialisasi
# Mengimpor modul turtle
import turtle

# Menginstansiasi objek turtle "kura"
kura = turtle.Turtle()

# Meminta input untuk menentukan
# panjang sisi anak tangga
sisi = int(input("Masukkan panjang sisi anak tangga: "))

# Mengaktifkan pena
kura.pendown()

# Penggambaran
# Menggunakan tinta kuning
kura.color('yellow')

# Memutar pena ke kiri sebesar 90 derajat
# sehingga pena menghadap ke atas
kura.left(90)

# Bergerak maju sebesar panjang sisi
# yang telah ditentukan
kura.forward(sisi)

# Memutar pena ke kanan sebesar 90 derajat
# sehingga pena menghadap ke kanan
kura.right(90)

# Bergerak maju sebesar panjang sisi
kura.forward(sisi)

# Mengulang langkah-langkah di atas
# untuk kedua anak tangga yang lain
kura.color('blue')
kura.left(90)
kura.forward(sisi)
kura.right(90)
kura.forward(sisi)

kura.color('red')
kura.left(90)
kura.forward(sisi)
kura.right(90)
kura.forward(sisi)

# Menutup anak tangga

# Menggunakan tinta hijau
kura.color('green')

# Memutar pena ke kanan sebesar 90 derajat
# sehingga pena menghadap ke bawah
kura.right(90)

# Bergerak maju sebesar tiga kali
# panjang sisi yang telah ditentukan
kura.forward(3 * sisi)

# Memutar pena ke kanan sebesar 90 derajat
# sehingga pena menghadap ke kiri
kura.right(90)

# Bergerak maju sebesar tiga kali
# panjang sisi yang telah ditentukan
kura.forward(3 * sisi)

# Menonaktifkan pena
kura.pendown()

# Menutup turtle setelah diklik
turtle.exitonclick()
