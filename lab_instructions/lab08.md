# Tutorial 08: Class dan Pemrograman Berorientasi Objek (OOP)

## Daftar Isi

- [*Class*](#class)
  - [Definisi *class*](#definisi-class)
  - [Mendefinisikan suatu *class*](#mendefinisikan-suatu-class)
  - [Fungsi *constructor*](#fungsi-constructor)
  - [Atribut](#atribut)
    - [*Data attributes*](#data-attributes)
    - [*Methods*](#methods)
    - [*Static attributes*](#static-attributes)
  - [Objek *(instance)*](#objek-instance)
  - [Beda *class* dengan objek *(instance)*](#beda-class-dengan-objek-instance)
- [Pemrograman Berorientasi Objek (OOP)](#pemrograman-berorientasi-objek-oop)
  - [Definisi OOP](#definisi-oop)
  - [OOP dan *Software Engineering*](#oop-dan-software-engineering)

<br>

## *Class*

### Definisi *class*

***Class*** adalah sebuah prototipe yang merupakan dasar untuk pembuatan objek.
Prototipe ini mendefinisikan ciri-ciri objek, yang kemudian dapat digunakan ke
depannya.

<br>

### Mendefinisikan suatu *class*

Kita bisa **mendefinisikan sebuah *class*** baru dengan menulis seperti
berikut:

```python
class ClassName:
    # Isi dari class
```

Dalam Python, perlu dicatat bahwa **nama *class* sebaiknya ditulis dalam bentuk
CapWords (varian dari [camel case][camel case]), yang berarti huruf kapital
digunakan untuk setiap awal kata**.

<br>

### Fungsi *constructor*

Sebuah fungsi yang dipanggil untuk membuat suatu objek *(instance)* dari sebuah
*class* disebut ***constructor***. Dalam Python, *constructor* memiliki nama
tersendiri yaitu `__init__`. Kita dapat mendefinisikan fungsi `__init__` dalam
sebuah *class*, yang merupakan fungsi paling pertama yang dipanggil ketika
membuat suatu objek *(instance)* dari *class* tersebut. Jika tidak
didefinisikan, maka fungsi `__init__` secara *default* tidak akan melakukan
apa-apa selain membuat objek baru.

Kita bisa mendefinisikan fungsi `__init__` seperti berikut.

```python
class ClassName:
    def __init__(self):
        # Hal-hal yang ingin dilakukan ketika objek dibuat
```

<br>

### Atribut

**Atribut** dari suatu *class* terdiri dari ***data attributes*** dan
***methods***.

#### *Data attributes*

***Data attribute*** adalah atribut berupa variabel yang khusus terhadap sebuah
objek. Perhatikan contoh pembuatan *data attribute* pada *class* `Mobil`
berikut.

```python
class Mobil:
    def __init__(self):
        self.merek = 'BMW'
        self.pemilik = 'Paman'
        self.menyala = False
```

Pada contoh di atas, kita membuat 3 variabel yang bernama `merek`, `pemilik`,
dan `menyala`. Apabila kita ingin supaya sebuah objek `Mobil` langsung memiliki
ketiga ciri-ciri tersebut, kita masukkan hal tersebut ke dalam fungsi
`__init__`.

Perhatikan bahwa untuk setiap penulisan variabel, kita menulis `self.` terlebih
dahulu. Ini menandakan bahwa variabel tersebut merupakan bagian dari objek
`Mobil`, bukan variabel dalam fungsi `__init__`.

Tentunya, kita juga dapat membuat *class* `Mobil` sedemikian hingga beberapa
variabel ditentukan ketika membuat objek. Perhatikan modifikasi contoh pada
*class* `Mobil` berikut:

```python
class Mobil:
    def __init__(self, merek, pemilik):
        self.merek = merek
        self.pemilik = pemilik
        self.menyala = False
```

Pada modifikasi di atas, kita membuat *class* `Mobil` sedemikian hingga
variabel `merek` dan `pemilik` bebas ditentukan ketika objek dibuat, dan objek
`Mobil` dipastikan tidak `menyala` pada awal pembuatan.

#### *Methods*

***Method*** adalah atribut yang berupa fungsi. Perhatikan contoh *method*
`klakson()` pada class `Mobil` berikut.

```python
class Mobil:
    def klakson(self):
        print('TIN TIN')
```

Pada contoh di atas, kita membuat fungsi `klakson()` yang hanya akan melakukan
`print('TIN TIN')`. Perhatikan bahwa setiap *method* harus memiliki suatu
parameter sebagai parameter pertama, biasanya `self`. Parameter ini merupakan
*reference* ke objek yang memanggil *method* tersebut.  
Perhatikan contoh penggunaan `self` pada *class* `Mobil` berikut.

```python
class Mobil:
    def __init__(self, merek, pemilik):
        self.merek = merek
        self.pemilik = pemilik
        self.menyala = False

    def ganti_pemilik(self, pemilik_baru):
        self.pemilik = pemilik_baru
```

Pada contoh di atas, kita membuat sebuah fungsi `ganti_pemilik` yang akan
mengubah *data attribute* `pemilik` dari objeknya.

#### *Static attributes*

Atribut tidak harus terikat pada suatu objek *(instance)*. Ada kalanya kita
tidak memerlukan suatu *instance* untuk suatu atribut, baik *data attribute*
maupun *method*, tetapi atribut tersebut masih berkaitan dengan *class*-nya.
Perhatikan contoh berikut.

```python
class Mobil:
    BANYAK_RODA = 4

    def __init__(self, merek, pemilik):
        self.merek = merek
        self.pemilik = pemilik
        self.menyala = False

    def ganti_pemilik(self, pemilik_baru):
        self.pemilik = pemilik_baru

print("Sebuah mobil memiliki", Mobil.BANYAK_RODA, "roda")
```

Pada contoh di atas, kita dapat mengakses atribut `BANYAK_RODA` tanpa perlu
membuat *instance* dari `Mobil`. Kita dapat mengakses atribut `BANYAK_RODA`
dengan `Mobil.BANYAK_RODA`. Dalam kasus ini, atribut `BANYAK_RODA` bersifat
*static*. ***Static attribute*** pada suatu *class* dimiliki oleh *class*
tersebut, bukan *instance*-nya.

Untuk membuat atribut yang *static*, cukup deklarasikan di dalam pendefinisian
*class*. Untuk konstanta, biasakan untuk menggunakan huruf kapital dengan
*underscore* sebagai pemisah kata.

Untuk *static method*, ada cara tersendiri yang digunakan untuk
mendefinisikannya. Biasanya, *function decorator* seperti
[`@staticmethod`][@staticmethod docs] atau [`@classmethod`][@classmethod docs]
digunakan untuk mendefinisikan *static method*. Namun, kalian bisa
mempelajarinya sendiri karena hal tersebut tidak dibahas di dalam mata kuliah
ini.

<br>

### Objek *(instance)*

Sebuah **objek** atau ***instance*** adalah perwujudan dari suatu *class*.
Setiap objek mempunyai nilai masing-masing untuk *data attributes*-nya. Untuk
membuat suatu objek dari suatu *class*, kita dapat memanggil *constructor*
pada *class*-nya. Untuk memanggil *constructor*, kita tidak perlu memanggil
fungsi `__init__` secara eksplisit, tetapi kita bisa memanggilnya dengan nama
dari *class* itu sendiri.  
Perhatikan contoh *class* `Mobil` dan cara bekerja dengan objeknya pada kode
berikut.

```python
class Mobil:
    def __init__(self, merek, pemilik):
        self.merek = merek
        self.pemilik = pemilik
        self.menyala = False

    def klakson(self):
        print('TIN TIN')

    def ganti_pemilik(self, pemilik_baru):
        self.pemilik = pemilik_baru

    def nyalakan(self):
        self.menyala = True
        print("Mobil menyala, BRUM BRUM")

    def matikan(self):
        self.menyala = False
        print("Mobil dimatikan")

    def is_mahal(self):
        return self.merek == 'BMW'


sebuah_mobil = Mobil('BMW', 'Paman')
sebuah_mobil.ganti_pemilik('Saya sendiri')
sebuah_mobil.nyalakan()
sebuah_mobil.klakson()
sebuah_mobil.matikan()

if sebuah_mobil.is_mahal():
    print("WoOoW, mobil ini mahal!")
else:
    print("Hah, mobil pecundang.")

print("Mobil", sebuah_mobil.merek, "milik", sebuah_mobil.pemilik)
```

Coba jalankan kode di atas dan lihat keluarannya.

<br>

### Beda *class* dengan objek *(instance)*

Perhatikan analogi berikut.

> Beda *class* dengan objek *(instance)* kurang lebih sama dengan bedanya
> cetakan kue dengan kue yang dibuat.

*Class* bertindak sebagai ***template*** yang dipakai saat membuat *instance*
yang konkret. Struktur dari suatu *instance* pada mulanya akan sama dengan
struktur yang ditentukan oleh *class* yang bersangkutan. Biasanya, sebuah
*instance* disebut juga dengan objek.

<sup><sub>Namun, dalam Python, **SEMUA** hal adalah objek, termasuk tipe data
(*integer*, *boolean*, dsb.), fungsi, **bahkan *class* itu sendiri**, dan
*instance* dari semua hal tersebut. Hal ini **tidak** seperti bahasa
pemrograman lain pada umumnya.</sub></sup>

<br>

## Pemrograman Berorientasi Objek (OOP)

### Definisi OOP

**Pemrograman Berorientasi Objek** atau ***Object-Oriented Programming (OOP)***
adalah paradigma pemrograman yang memandang setiap program sebagai kumpulan
objek serta interaksi di antara mereka. Program dalam OOP tidak dipandang hanya
sebagai kumpulan perintah.

Dalam OOP, setiap objek merespon "pesan" yang dikirim ke objek tersebut.
Interaksi antar objek melalui pesan antar objek menggambarkan apa yang
dikerjakan di dalam program.

Dalam Python, tipe data dari sebuah objek atau nilai bisa dipandang sebagai
*class*, dan nilai tersebut merupakan *instance* dari *class*-nya, contohnya:
`list`, `dict`, `str`, dan sebagainya. Setiap *class* tersebut digunakan untuk
merepresentasikan data dengan sifat yang berbeda, dan akan merespon pesan yang
berbeda-beda untuk melakukan manipulasi data.

<br>

### OOP dan *Software Engineering*

***Software engineering*** adalah disiplin ilmu yang mempelajari cara merancang
dan mengelola kode program (yang membentuk perangkat lunak) demi menjamin
penggunaannya dalam jangka panjang.

Dalam *software engineering*, kita akan sering melakukan ***refactoring***.
*Refactoring* merupakan proses:

- mengambil kode program yang sudah ada, lalu memodifikasinya.
- membuat kode program secara keseluruhan menjadi lebih sederhana dan mudah
  dipahami.
- tidak mengubah fungsionalitas (hal sesungguhnya yang dikerjakan program),
  dan hanya mengatur wujudnya.

Dalam melakukan *refactoring* pada program yang menerapkan paradigma OOP,
biasanya diterapkan prinsip-prinsip berikut:

- ***encapsulation***: menyembunyikan detail implementasi demi membuat program
  lebih jelas dan memudahkan modifikasi di masa datang.
- ***modularity***: membuat objek secara utuh berdiri sendiri sehingga bisa
  digunakan kembali. Contoh: *module* `math`
- ***inheritance***: membuat objek baru dengan mewarisi karakteristik objek
  yang sudah ada.
- ***polymorphism***: memungkinkan suatu pesan dikirim ke sembarang objek dan
  menjadikan respons atas pesan tersebut disesuaikan dengan tipe objek yang
  dikirimi.

Kalian akan mempelajari lebih lanjut mengenai prinsip-prinsip di atas dalam
mata kuliah **Dasar-Dasar Pemrograman 2**.

<br>

---

Diadaptasi dari:

- `Lab 8 Senin.pdf` buatan **ALD**, **DHA**, **GIL**, dan **DST**
- `ddp1-17gasal-11.pdf` buatan **Adila Alfa Krisnadhi, Ph.D.**

dengan beberapa perubahan.

[camel case]: https://en.wikipedia.org/wiki/Camel_case

[@staticmethod docs]: https://docs.python.org/3/library/functions.html#staticmethod

[@classmethod docs]: https://docs.python.org/3/library/functions.html#classmethod
