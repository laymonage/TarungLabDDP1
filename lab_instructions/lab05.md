# Tutorial 05: File dan Exception

## Daftar Isi

- [I/O *file* teks](#io-file-teks)
- [*Exception*](#exception)
  - [Perintah `try` dan `except`](#perintah-try-dan-except)
  - [Klausa `else` dan `finally`](#klausa-else-dan-finally)

<br>

## I/O *file* teks

Untuk dapat membaca atau menulis **berkas *(file)***, kita bisa menggunakan
fungsi `open(nama_file, mode)`.

Contoh:

```python
objek_file = open(nama_file, mode)
```

Keterangan:

- `nama_file`: ***string*** berupa nama *file* yang akan kita baca/tulis, harus
  beserta ekstensi formatnya (`input.txt`, ekstensi format: **.txt**).
- `mode`: ***string*** berupa mode membuka *file*, ini yang menentukan apakah
  kita akan membaca *(read)* atau menulis *(write)* *file*, akan dijelaskan di
  bawah.
- `objek_file`: **variabel** yang akan menyimpan file yang telah dibuka.

| Mode   | Baca/Tulis?  | Jika *file* ada | Jika *file* tidak ada | Posisi kursor |
| ------ | ------------ | --------------- | --------------------- | ------------- |
| `'r'`  | Hanya baca   | Buka file       | **Error**             | Awal          |
| `'w'`  | Hanya tulis  | Hapus isi file  | Buat dan buka baru    | Awal          |
| `'a'`  | Hanya tulis  | Isi dibiarkan   | Buat dan buka baru    | Akhir         |
| `'r+'` | Baca & tulis | Isi dibiarkan   | **Error**             | Awal          |

Untuk mode lainnya, silakan lihat di [dokumentasi fungsi `open`][open docs].

<br>

Untuk menambahkan *string* ke dalam file yang akan ditulis, kalian bisa
menggunakan fungsi `print(sebuah_string, file=objek_file)`.

Contoh:

```python
objek_file = open("ddpez.txt", 'w')
print("DDP1 terlalu mudah bagi saya", file=objek_file)
```

Jika sudah selesai berurusan dengan suatu `objek_file` (baik membaca atau
menulis), jangan lupa untuk menutup *file* tersebut dengan memanggil *method*
`close()`.

Contoh:

```python
objek_file.close()
```

**Perhatian**: jika melakukan penulisan pada suatu `objek_file`, pastikan
`objek_file` dibuka dengan mode yang memungkinkan program untuk menulis ke
`objek_file` tersebut. Selain itu, pastikan untuk memanggil *method* `close()`
jika *file* sudah selesai diakses. Jika tidak, maka *file* akan tetap terbuka
selama program masih berjalan sehingga dapat bentrok dengan program lain yang
mengakses *file* yang sama.

Berikut adalah contoh sederhana program yang menyalin isi suatu berkas ke
berkas lainnya.

```python
berkas_masukan = open("file_input.txt", 'r')
berkas_keluaran = open("file_output.txt", 'w')

for kalimat in berkas_masukan:
    print(kalimat, file=berkas_keluaran)

berkas_masukan.close()
berkas_keluaran.close()
```

<br>

## *Exception*

Dalam proses eksekusi program, sering kali ditemukan situasi yang tidak biasa
(abnormal). Misalnya, mencoba membuka *file* yang tidak ada, mencoba mengakses
elemen pada indeks yang melebihi rentang yang ada, dan lain-lain. Ketika
hal-hal tersebut terjadi, biasanya Python akan "melempar" suatu ***error***.
Setiap *error* dalam Python memiliki nama, misalnya `IOError`, `ValueError`,
`IndexError`, dan lain-lain. Untuk itu, perlu ada suatu
***exception handling*** untuk menangani *error* tersebut.

<br>

### Perintah `try` dan `except`

Berikut adalah contoh bentuk blok **`try`/`except`** yang dapat digunakan untuk
mencegah berhentinya program ketika terjadi *error*.

```python
try:
    # Kode yang mungkin menghasilkan error
except (NamaError1, NamaError2):
    # Kode untuk menangani error yang bernama NamaError1 atau NamaError2
except NamaError3:
    # Kode untuk menangani error yang bernama NamaError3
```

Keterangan:

- jika tidak terjadi *error*, semua blok `except` akan dilompati.
- jika terjadi *error*, semua perintah di dalam blok `try` di bawah terjadinya
  *error* akan dilompati, dan Python akan langsung mencari *handler* nama
  *error* yang sesuai di blok `except`.
- jika nama *error* yang dicari tidak ditemukan *handler*-nya, maka *error*
  akan dilempar ke pengguna.
- jika `NamaError` tidak disebutkan (hanya menulis `except:`, disebut
  *bare except*), program tetap bisa dijalankan dan semua macam *error* akan
  ditangani oleh blok `except:` tersebut. Meski bisa dijalankan, hal ini
  **sangat tidak disarankan** karena akan membuat *exception* sulit dilacak.
- untuk nama-nama *error* yang tersedia secara bawaan dalam Python, silakan
  cek [dokumentasi Python][exception docs].

<br>

### Klausa `else` dan `finally`

Mirip seperti pada perulangan (*loop*), klausa **`else`** dapat digunakan untuk
blok `try`/`except`, dan hanya akan dijalankan apabila tidak terjadi *error*
dalam blok `try`.

Sedangkan klausa **`finally`** akan **selalu** dijalankan, apa pun yang terjadi
dalam blok `try`. Klausa `finally` biasanya digunakan untuk *cleanup*.

Contoh:

```python
sebuah_string = "fasilkom"
objek_file = open("nama_file.txt", 'w')
try:
    print(sebuah_string[3:], file=objek_file)
    print(sebuah_string[8], file=objek_file)
except IndexError:
    print("Gagal menuliskan ke file!")
else:
    print("Semua string berhasil dituliskan ke file.")
finally:
    objek_file.close()
```

Sebagai tambahan, klausa `try` dapat dipasangkan dengan klausa `finally`
tanpa memerlukan klausa `except`. Contoh:

```python
objek_file = open("nama_file.txt")
try:
    # Lakukan sesuatu dengan objek_file
finally:
    objek_file.close()
```

Untuk memudahkan, terdapat klausa `with` yang bisa digunakan untuk mengakses
*file*. Kode di atas ekuivalen dengan kode berikut.

```python
with open("nama_file.txt") as objek_file:
    # Lakukan sesuatu dengan objek_file
```

<br>

---

Diadaptasi dari:

- `Lab 4 Dasar-Dasar Pemrograman 1 - REVISI.pdf`
  buatan **NN**, **WP**, **YE**, dan **AH**
- `ddp1-17gasal-06.pdf` dan `ddp1-17gasal-14.pdf`
  buatan **Adila Alfa Krisnadhi, Ph.D.**

dengan beberapa perubahan.

[open docs]: https://docs.python.org/3/library/functions.html#open

[exception docs]: https://docs.python.org/3/library/exceptions.html
