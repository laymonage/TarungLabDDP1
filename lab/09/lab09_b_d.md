# Paket Soal "MK Sebentar Lagi"

<h5>"<i>Besok MK cuy! Semangat semuanya!</i>"</h5>
<h5>- Tim Asdos DDP 1 (termasuk Benny, yang selalu ada di setiap soal buatan
asdos lainnya) -</h5>

<br>

## Soal Tutorial 1

### Kompresi Benny

Benny suka membuat teka-teki. Kali ini, Benny membuat sebuah teka-teki dan
diberikan nama "Kompresi Benny". Tujuan dari teka-teki ini adalah
menyederhanakan sebuah kata dengan membuat beberapa karakter yang sama dan
berurutan hanya akan menjadi satu karakter saja. Cukup mudah bukan?

***Anda wajib mengimplementasikan algoritma kompresi Benny ini dengan
menggunakan rekursif! Apabila tidak menggunakan rekursif, maka nilai tidak akan
maksimal.***

**Input:**  
Input berupa satu baris karakter-karakter tanpa spasi. Karakter-karakter tersebut adalah
karakter ASCII.

**Output:**  
Output berupa satu baris karakter-karakter yang sudah dikompresi.

#### Contoh input-output:

```
>>> aaaaa
Hasil kompresinya adalah a
>>> aabbbbaaacddeae
Hasil kompresinya adalah abacdeae
>>> abcde
Hasil kompresinya adalah abcde
```

<br>

## Soal Tutorial 2

### Angka Cantik Versi Benny (bukan Benny-nya yang cantik)

Benny sangat benci melihat bilangan yang lebih dari satu digit, menurutnya,
sebuah bilangan yang lebih dari satu digit (lebih dari atau sama dengan 10)
adalah bilangan yang tidak cantik. Oleh karena itu, anda, diminta membantu
Benny untuk mencari bilangan cantik dari suatu bilangan.

Bilangan cantik dari sebuah bilangan x adalah sebagai berikut:

- Apabila x hanya terdiri satu digit, bilangan cantiknya adalah x.
- Apabila tidak, bilangan cantik dari x adalah bilangan cantik dari penjumlahan
  digit-digitnya.

Contoh:

```
angka_cantik(12345) = angka_cantik(1+2+3+4+5)
                    = angka_cantik(15)
                    = angka_cantik(1+5)
                    = angka_cantik(6)
                    = 6
```

***Anda wajib mengimplementasikan algoritma pencarian angka cantik versi Benny
ini dengan menggunakan rekursif. Apabila tidak menggunakan rekursif, maka nilai
tidak akan maksimal.***

**Input:**  
Input berupa suatu bilangan bulat n

**Output:**  
Outputkan bilangan cantik dari bilangan n

#### Contoh input-output:

```
>>> 123
6
>>> 12345
6
```

<br>

### Penilaian

**50%** Soal Tutorial 1  
**50%** Soal Tutorial 2

<br>

---

Diambil dari `Lab9 DDP1 Jumat.pdf` (Tutorial Lab 9 DDP1 B dan D
\-- 24 November 2017)
