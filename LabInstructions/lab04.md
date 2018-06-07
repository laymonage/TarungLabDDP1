# Tutorial 04: String dan Slicing

## Daftar Isi

- [Representasi *string*](#representasi-string)
- [*Slicing*](#slicing)
- [*String methods*](#string-methods)

<br>

## Representasi *string*

Dalam Python, sebuah objek *string* direpresentasikan sebagai untaian karakter
dalam tanda petik satu `'` atau tanda petik dua `"`. Untuk menyatakan sebuah
untaian yang mengandung tanda petik, kita dapat menggunakan *escape sequence*
*character* yaitu `\`.  
Contoh:

```python
>>> excuse = 'I am sick'
>>> excuse = "I am sick"
>>> excuse = 'I am "sick"'
>>> excuse = "I am 'sick'"
>>> excuse = 'I'm "sick"'
SyntaxError: invalid syntax
>>> excuse = 'I\'m "sick"'
>>> excuse = "I'm \"sick\""
>>> print(excuse)
I'm "sick"
```

<br>

## *Slicing*

*String* adalah untaian karakter, sehingga kita bisa mengakses
karakter-karakter yang ada di dalamnya. Untuk mengakses suatu karakter dalam
suatu string, kita bisa menggunakan operator `[indeks]`, dengan argumen nilai
`indeks` yang menyatakan posisi karakter dalam string (dimulai dari 0).  
Untuk string dengan panjang `n`:
<<<<<<< master
  - Indeks non-negatif dari kiri ke kanan: `0`, `1`, `2`, `...` , `n-1`
  - Indeks negatif dari kiri ke kanan: `-n`, `-n + 1`, `-n + 2`, `...`, `-1`
=======

- Indeks non-negatif dari kiri ke kanan: `0`, `1`, `2`, `...` , `n-1`
- Indeks negatif dari kiri ke kanan: `-n`, `-n + 1`, `-n + 2`, `...`, `-1`
>>>>>>> master

Lebih jauh lagi, kita bisa menggunakan operator `[]` untuk operasi *slicing*:
mengakses subrangkaian. Argumennya serupa dengan fungsi range, yaitu:

Bentuk umum: `[start:end:step]`
<<<<<<< master
  - `start`: nilai indeks dimulainya subrangkaian (inklusif, *default*: 0)
  - `end`: nilai indeks sesudah akhir subrangkaian (eksklusif, *default*: nilai
    indeks ujung rangkaian + 1)
  - `step`: nilai *increment/decrement* untuk membentuk subrangkaian
    (*default*: 1)
=======

- `start`: nilai indeks dimulainya subrangkaian (inklusif, *default*: 0)
- `end`: nilai indeks sesudah akhir subrangkaian (eksklusif, *default*: nilai
  indeks ujung rangkaian + 1)
- `step`: nilai *increment/decrement* untuk membentuk subrangkaian
  (*default*: 1)
>>>>>>> master

Contoh:

```python
>>> kata = "Fasilkom"
>>> kata[2]
's'
>>> kata[:2] # Melakukan slicing dari indeks ke-0 sampai ke-1
'Fa'
>>> kata[3:] # Melakukan slicing dari indeks ke-3 sampai akhir string
'ilkom'
>>> kata[::-1] # Mendapatkan kebalikan dari string
'moklisaF'
```

<br>

## *String methods*

Dalam Python, terdapat banyak *method* yang dapat digunakan untuk mengolah
string. Namun, perlu ditekankan kembali, *string* bersifat ***immutable***,
sehingga tidak ada satupun *method* yang mengubah nilai sebuah *string* yang
tersimpan dalam suatu variabel. Beberapa contoh *method* di *string* adalah:

```python
>>> s = 'http://www.main.com/smith/index.html'
>>> s.upper() # Mendapatkan string yang huruf-hurufnya diubah ke uppercase
'HTTP://WWW.MAIN.COM/SMITH/INDEX.HTML'
>> s.find('smith')
20
>>> s.capitalize()
'Http://www.main.com/smith/index.html'
>>> s.replace('smith', 'ferreira')
'http://www.main.com/ferreira/index.html'
>>> s
'http://www.main.com/smith/index.html'
>>> s.split('/')
['http:', '', 'www.main.com', 'smith', 'index.html']
>>> len(s)
36
```

Untuk mengubah nilai suatu string menjadi hasil olahan suatu *method*, kita
dapat menyimpan nilai yang dikembalikan oleh *method* tersebut ke variabel
aslinya atau ke sebuah variabel baru.

```python
>>> contoh = "FASILKOM"
>>> contoh.lower()
'fasilkom'
>>> contoh
'FASILKOM'
>>> contoh_baru = contoh.lower()
>>> contoh_baru
'fasilkom'
>>> contoh
'FASILKOM'
>>> contoh = contoh.lower()
>>> contoh
'fasilkom'
```

Untuk mengetahui *method-method* lainnya untuk tipe data *string*, kalian bisa
melihatnya di ["Python documentation: Common string operations"][python docs].

<br>

---

Diadaptasi dari:

- `Lab 3 DDP1 Lab Jumat.pdf` buatan **AA**, **END**, **KT**, dan **ZZ**
- `ddp1-17gasal-05.pdf` buatan **Adila Alfa Krisnadhi, Ph.D.**

dengan beberapa perubahan.

[python docs]: https://docs.python.org/3/library/string.html
