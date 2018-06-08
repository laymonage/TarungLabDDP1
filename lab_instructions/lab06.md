# Tutorial 06: Fungsi

## Daftar Isi

- [Definisi](#definisi)
- [Parameter](#parameter)
  - [Parameter *default*](#parameter-default)
  - [Pemberian argumen](#pemberian-argumen)
  - [Argumen yang banyaknya bebas](#argumen-yang-banyaknya-bebas)
- [Pengembalian nilai (`return`)](#pengembalian-nilai-return)

<br>

## Definisi

Kita sudah sering menggunakan fungsi di lab-lab sebelumnya, seperti  `print()`,
`input()`, `len()`, dan `range()`. Fungsi merupakan salah satu bagian dari
pemrograman yang paling fundamental, jadi pastikan kalian mengerti
penggunaannya. Fungsi merupakan salah satu cara mudah untuk membagi program
menjadi bagian-bagian yang berguna, memungkinkan untuk mengurutkan kode menjadi
lebih baik, membuatnya lebih mudah dibaca, lebih mudah digunakan kembali, dan
menghemat waktu. Fungsi juga merupakan salah satu cara utama untuk
mendefinisikan suatu hal sehingga antara programmer dapat berbagi kode mereka.

Untuk mendefinisikan sebuah fungsi, kita menggunakan *keyword* `def`. Fungsi
dapat menerima parameter dan dapat mengembalikan suatu nilai, tetapi fungsi
tidak harus memiliki kedua ciri tersebut. Berikut adalah contoh pendefinisian
dan pemanggilan sebuah fungsi dalam bahasa Python.

```python
def kuadrat(x):
    return x**2

a = kuadrat(3)
print(a)
# Output: 9
```

Pada contoh di atas, kita mendefinisikan suatu fungsi bernama `kuadrat`, yang
menerima parameter `x` dan mengembalikan nilai `x**2`.

<br>

## Parameter

Parameter pada fungsi adalah variabel-variabel yang diperlukan dalam fungsi.
Seperti contoh di atas, fungsi `kuadrat` memerlukan suatu variabel `x` untuk
menghitung `x`<sup>`2`</sup>.

Ketika kita memanggil suatu fungsi yang memiliki parameter, kita memberikan
nilai yang akan digunakan sebagai parameter di dalam fungsi. Nilai yang kita
berikan ketika memanggil suatu fungsi dinamakan argumen.  
Contoh: pada pemanggilan `kuadrat(3)`, argumennya adalah `3`.

Tentunya, jika fungsi kita tidak memerlukan variabel apapun, kita dapat
mendefinisikan fungsi tanpa parameter, seperti pada contoh berikut.

```python
def intro():
    print("Selamat datang di program tercanggih di abad ini!")
    print("Silakan tekan masukkan sesuatu dan tekan Enter, "
          "kemudian lihat apa yang terjadi.")
    return 42 * sesuatu()

sesuatu = intro()  # Dapat dipanggil tanpa parameter
```

<br>

### Parameter *default*

Kita juga bisa mendefinisikan nilai *default* untuk suatu parameter. Parameter
yang memiliki nilai *default* tidak harus diberi nilai ketika dipanggil. Jika
suatu fungsi memiliki parameter *default* dan parameter non-*default*, maka
parameter yang non-*default* harus diletakkan lebih awal. Berikut adalah contoh
pendefinisian fungsi yang memiliki *default* parameter.

```python
def hitung_volume_balok(panjang, lebar=5, tinggi=7):
    return panjang * lebar * tinggi

print(hitung_volume_balok(10))  # Output: 350
print(hitung_volume_balok(5, 3, 2))  # Output: 30
print(hitung_volume_balok(2, 3))  # Output: 42
print(hitung_volume_balok(tinggi=5, panjang=9))  # Output: 225
```

<br>

### Pemberian argumen

Pada contoh sebelum-sebelumnya, kita memberikan argumen dengan memberikan
nilainya secara langsung. Argumen yang seperti ini dinamakan *positional*
*argument*. Pada contoh terakhir yang di atas, kita melihat bahwa kita juga
bisa memberikan argumen dengan menyebutkan nama parameternya secara eksplisit.
Ini disebut dengan *keyword argument*.

Jika kita menggunakan *keyword argument*, urutan bisa diabaikan. Namun, jika
kita ingin mencampurkan *keyword argument* dengan *positional argument*, maka
*positional argument* harus dituliskan lebih awal.

<br>

### Argumen yang banyaknya bebas

Selain itu, kita juga bisa mendefinisikan sebuah fungsi yang memiliki parameter
yang bisa diisi dengan argumen sebanyak apa pun. Terdapat beberapa ketentuan
untuk hal ini:

- parameter dengan argumen yang banyaknya bebas ditandai dengan memberi
  karakter `*` di depan nama parameter.
- hanya ada satu parameter yang banyak argumennya bisa bebas.
- posisi parameter tersebut harus di paling belakang.
- argumennya tidak bisa diberikan dengan *keyword argument*

Perhatikan contoh berikut.

```python
def a_function(fixed_param, *tuple_param):
    print("fixed =", fixed_param)
    print("tuple =", tuple_param)

a_function(1, 2, 3, 4)
a_function(1)
a_function(fixed_param=4)
a_function(tuple_param=(1,2,3), fixed_param=1)
```

Bagaimanakah outputnya?

<br>

## Pengembalian nilai (`return`)

Suatu fungsi dapat mengembalikan nilai, seperti fungsi `len(x)` yang
mengembalikan panjang dari suatu *container* `x` yang diberikan, dan fungsi
`input()` yang mengembalikan input dari pengguna. Namun, fungsi juga bisa tidak
mengembalikan nilai, seperti fungsi `print()`.

Kita dapat mendefinisikan cara fungsi mengembalikan nilai dengan *keyword*
`return`. Seperti pada contoh fungsi `kuadrat(x)`, setelah nilai
`x`<sup>`2`</sup> dihitung, fungsi tersebut mengembalikan hasilnya. Fungsi yang
tidak mengembalikan nilai juga disebut prosedur. Untuk membuat fungsi yang
tidak mengembalikan nilai, kita dapat menggunakan `return None`, `return` saja,
atau menghilangkan keyword `return`.

```python
def tambah_satu(sebuah_list):
    sebuah_list.add(1)
    return None

def ucap_selamat(nama):
    print("Selamat", nama + "!")
    return

def berapa_panjang(sesuatu):
    print("Panjangnya adalah", len(sesuatu))
```

Ketiga fungsi di atas mengembalikan `None` ketika dipanggil.

**PENTING**: perlu diketahui bahwa sesudah perintah `return` dijalankan, maka
kontrol akan keluar dari fungsi tersebut (fungsi berhenti dijalankan). Artinya,
semua perintah di bawah `return` tidak akan dijalankan ketika perintah `return`
sudah dijalankan. <sup><sub>Namun, apa yang terjadi ketika ada `return` di
dalam blok `try` yang memiliki klausa `finally`?</sub></sup>

<br>

Masih banyak yang dapat dipelajari mengenai fungsi dalam Python. Untuk
mempelajari lebih lanjut, kalian bisa membuka dokumentasi Python untuk
[fungsi][fungsi], [parameter][parameter], dan [argumen][argumen].

<br>

---

Diadaptasi dari:

- `lab_6_Senin.pdf` buatan **ALD**, **DHA**, **GIL**, dan **DST**
- `ddp1-17gasal-07.pdf` buatan **Adila Alfa Krisnadhi, Ph.D.**

dengan beberapa perubahan.

[fungsi]: https://docs.python.org/3/reference/compound_stmts.html#function

[parameter]: https://docs.python.org/3/glossary.html#term-parameter

[argumen]: https://docs.python.org/3/glossary.html#term-argument
