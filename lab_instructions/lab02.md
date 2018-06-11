# Tutorial 02: Variabel, Tipe Data, dan Operator

## Daftar Isi

- [Variabel](#variabel)
- [Tipe data](#tipe-data)
- [Operator](#operator)
- [*Type casting* (mengubah tipe data)](#type-casting-mengubah-tipe-data)

<br>

## Variabel

**Variabel** bisa dianggap sebagai alokasi memori di dalam komputer yang
digunakan untuk menyimpan suatu nilai. Nilai tersebut dapat berupa bilangan,
karakter, dan lain sebagainya yang akan dibahas selanjutnya di bagian tipe
data.  
Contoh pembuatan dan penggunaan variabel:

```python
>>> nilai_kuis_terakhir = 70 # Membuat variabel bernilai 70, tipe data integer
>>> print(nilai_kuis_terakhir) # Mencetak nilai variabel tersebut
70
>>> nilai_kuis_terakhir = 100 # Mengubah nilai variabel tersebut
>>> print(nilai_kuis_terakhir) # Mencetak nilai variabel tersebut
100
>>> nilai_kuis_terakhir = 'A' # Variabel di Python bersifat dinamis,
                              # tipe datanya bisa berubah-ubah sesuai nilainya
>>> print(nilai_kuis_terakhir) # Mencetak nilai variabel tersebut
A
```

Untuk membuat suatu variabel, kita harus mengerti aturan penamaan dalam Python.
Berikut adalah aturan penamaan secara umum dalam Python:

- **diawali dengan huruf atau *underscore*** `_`, dan sisanya bisa terdiri dari
  **huruf**, **angka/digit**, dan ***underscore***.  
  Contoh:
  - <span style="color: blue">OK: `abc`, `AbC`, `a12`, `BC_12`, `_ab12`</span>
  - <span style="color: red">NOT OK: `123_AbC`, `ab$C`, `ab&@#c`</span>
- panjang nama bisa **berapa pun**.
- huruf besar dan kecil dianggap **beda** (***case-sensitive***).  
  Contoh: `Panjang_Sisi` beda dengan `panjang_sisi`
- pada umumnya, nama di Python menggunakan konvensi [`snake_case`][snake case],
  yang berarti menggunakan huruf kecil dan menggunakan *underscore* sebagai
  pemisah kata.  
  Contoh: `ini_variabel`, `sebuah_daftar`, `sebuah_fungsi`
- nama yang diawali dengan *underscore* biasanya punya makna khusus --
  **hati-hati**!
- ada aturan-aturan penamaan yang lebih spesifik untuk hal-hal lain seperti
  fungsi, kelas, dan lain-lain yang akan kalian pelajari nanti.

Penamaan variabel sebaiknya dilakukan sejelas mungkin (misal: `count` dibanding
`c`), agar kode kalian mudah dibaca dan mempermudah proses *debugging* (proses
menemukan dan memperbaiki kesalahan dalam kode). Sebisa mungkin, ikuti
*best practice* untuk gaya penulisan kode Python yang dapat dibaca di
[**PEP 8**][pep 8].

<br>

## Tipe data

**Tipe data (*data type*)** adalah jenis dari suatu nilai (*value*), contohnya
seperti *integer* (bilangan bulat), *string* (untaian karakter), atau *float*
(bilangan riil).

Dalam bahasa Python, beberapa tipe data yang biasa digunakan adalah sebagai
berikut.

1. **Integer**, contoh: `42`, `123`
2. **String**, contoh: `"Qerja lembur bagai quda"`, `'DDP ez pz lemon squeezy'`  
   <span style="color: red">**Catatan**</span>: penggunaan tanda petik dua `"`
   maupun tanda petik satu `'` sama saja, asalkan dibuka dan ditutup
   menggunakan tanda yang sama.
3. **Float**, contoh: `0.25`, `22.07`
4. **Boolean**, hanya memiliki dua kemungkinan nilai, yaitu `True` atau `False`
5. **List**, contoh: `[1, 2, 2, 3, 4, 5]`
6. **Tuple**, contoh: `(1, 2, 3, 3, 4, 5)`
7. **Set**, contoh: `{1, 2, 3, 4, 5}`
8. **Dictionary**, contoh: `{"nama": "Dek Depe", "umur": 13, 2: 42, 7: "hehe"}`

Kalian dapat menggunakan fungsi `type(nilai)` untuk mengetahui jenis tipe
data dari suatu nilai. Berikut adalah contoh penggunaannya.

```python
>>> angka = 1000
>>> type(angka)
<class 'int'>
>>> type('kalimat')
<class 'str'>
```

Memahami tipe data dalam Python sangat penting karena tipe data mendefinisikan
operasi-operasi apa saja yang bisa dilakukan terhadap nilai tersebut.
**Perlu diketahui bahwa di Python, tipe data nilai suatu variabel
<span style="color:red">dapat berubah-ubah (dinamis)</span>, jadi kalian harus
berhati-hati.**

<br>

## Operator

**Operator** adalah sebuah simbol yang digunakan untuk mengubah nilai operan
(sesuatu yang dioperasikan). Ada banyak operator yang dapat kita gunakan,
misalnya operator-operator aritmetika seperti berikut.

| Nama operasi                | Contoh                        |
| --------------------------- | ----------------------------- |
| Penjumlahan (`+`)           | `x = 7 + 2  # x bernilai 9`   |
| Pengurangan (`-`)           | `x = 7 - 2  # x bernilai 5`   |
| Perkalian (`*`)             | `x = 7 * 2  # x bernilai 14`  |
| Pembagian (`/`)             | `x = 7 / 2  # x bernilai 3.5` |
| Modulo/sisa pembagian (`%`) | `x = 7 % 2  # x bernilai 1`   |
| Pemangkatan (`**`)          | `x = 7 ** 2  # x bernilai 49` |
| Pembagian integer (`//`)    | `x = 7 // 2  # x bernilai 3`  |

Meski operator-operator di atas merupakan operator aritmetika yang biasanya
hanya bisa dioperasikan pada operan dengan tipe data bilangan (*integer*
atau *float*), ada beberapa operator yang bisa digunakan untuk tipe data yang
lain pula, contohnya adalah *string*.

```python
>>> hehe = 'hehe'
>>> angka = '123'
>>> print(hehe + angka + '.') # Penjumlahan string dengan string
hehe123.
>>> print(angka * 5) # Perkalian string dengan integer,
                     # string '123' diulang 5 kali.
123123123123123
```

Masih terdapat banyak operator lain seperti operator logika (`and`, `or`, `>`,
`<`, `==`) dan operator *bitwise* (`<<`, `>>`, `&`, `|`, `~`, `^`) yang kalian
bisa pelajari sendiri (atau sudah pelajari di kelas), tetapi tidak akan dibahas
di tutorial kali ini.

<br>

## *Type casting* (mengubah tipe data)

Dalam bahasa Python, sangat penting untuk mengetahui cara mengubah tipe data
sebuah nilai ke tipe data yang lain. Khususnya karena dalam bahasa Python,
apabila kita menerima masukan dari pengguna menggunakan fungsi `input()`, maka
nilai yang akan dikembalikan pasti bertipe data *string*. Sedangkan, terkadang
kita memerlukan masukan berupa bilangan bulat, bilangan riil, atau lainnya.

Perlu diketahui bahwa untuk sebagian besar operasi biner (operasi dengan dua
operan), tipe data kedua operan harus sama. Ekspresi seperti `'1' + 1` tidak
akan menghasilkan `2`, tetapi akan menghasilkan
<span style="color: red">***error***</span>. Oleh karena itu, kita perlu
mengetahui cara untuk mengubah suatu tipe data menjadi tipe data yang lain.

Beberapa cara untuk mengubah tipe data:

- `int(sesuatu)` akan menghasilkan sesuatu bertipe data ***integer***
- `float(sesuatu)` akan menghasilkan sesuatu bertipe data ***float***
- `str(sesuatu)` akan menghasilkan sesuatu bertipe data ***string***

**Catatan**: `sesuatu` di sini bisa merupakan variabel atau suatu nilai

Saat mengubah tipe data, kita harus berhati-hati karena operasi pengubahan
tipe data bisa menghasilkan suatu ***exception*** (akan kalian pelajari nanti),
misalnya ketika kalian mencoba melakukan `int("hehe")`.

<br>

---

Diadaptasi dari:

- `DDP1_KelasBD_Lab01_7Sep2017.pdf` buatan **AA**, **END**, **KT**, dan **ZZ**
- `ddp1-17gasal-03.pdf` buatan **Adila Alfa Krisnadhi, Ph.D.**

dengan beberapa perubahan.

[snake case]: https://en.wikipedia.org/wiki/Snake_case

[pep 8]: https://www.python.org/dev/peps/pep-0008
