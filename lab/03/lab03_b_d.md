# Soal Tutorial

## Classic Cryptography

Benny dan Ibnu merupakan dua orang sahabat karib. Mereka suka bertukar pesan
satu sama lain. Namun, mereka tidak ingin pesan mereka dapat diketahui oleh
orang lain, apalagi jika mereka sedang membicarakan wanita idaman mereka,
sehingga mereka menggunakan enkripsi pada pesan mereka. Suatu hari, Anda tidak
sengaja mengetahui teknik enkripsi mereka, karena Anda menguping pembicaraan
mereka. Mereka menggunakan teknik
"[Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher)" dalam
melakukan enkripsi pesan.

Teknik enkripsi mereka adalah untuk setiap huruf pada pesan, dilakukan operasi:
Diketahui K, maka lakukan pergeseran ke arah kanan sebesar K (Misal `K = 1`,
`"a"` menjadi `"b"`, `"j"` menjadi `"k"`, dan `"z"` menjadi `"a"`).
Anda sebagai orang yang ingin mengetahui pesan apa yang dikirimkan oleh Benny
dan Ibnu mencoba untuk membuat program agar tidak perlu melakukan dekripsi
secara manual.

Dewa Cenna memberikan contoh translasi dari ajarannya sebagai berikut:

#### Format Masukan

Masukan berupa satu baris yang menunjukkan berapa banyak pergeseran ke arah
kanan `(0 <= K < 26)` dan pesan yang telah dienkripsi (pesan yang telah
dienkripsi dipastikan huruf kecil semua).

Format masukan adalah sebagai berikut:

```
K encrypted_text
```

#### Format Keluaran

Keluaran berupa satu baris yang menunjukkan pesan awal sebelum dienkripsi.

###### Hint #1

<sub><sup>Kamu bisa menggunakan import string untuk mendapatkan seluruh
alfabet huruf kecil tanpa harus mengetikannya secara manual.</sup></sub>

Contoh Input/Output (bagian input yang diketikkan oleh user **ditebalkan**)

<pre>
Masukkan operasi: <b>1 plf</b>
Kalimat aslinya adalah: oke
</pre>

###### Hint #2

<sub><sup>Kamu dapat menggunakan sebuah method untuk memisahkan antara K dan
kalimat yang sudah dienkripsi. Method apakah itu?</sup></sub>

<pre>
Masukkan operasi: <b>12 mwg nuem ppb</b>
Kalimat aslinya adalah: aku bisa ddp

Masukkan operasi: <b>24 kclhybg kyfyqgquy dyqgjimk kcpsnyiyl qsyrs iczyleeyyl</b>
Kalimat aslinya adalah: menjadi mahasiswa fasilkom merupakan suatu kebanggaan

Masukkan operasi: <b>15 sse tphn etphn atbdc hfjtton</b>
Kalimat aslinya adalah: ddp easy peasy lemon squeezy
</pre>

<br>

### Soal Bonus (Yey... ada bonus!)

Selain menggunakan teknik yang standar, kamu juga bisa memanfaatkan `chr()`
dan `ord()` dalam program-mu. Cobalah buat teknik dekripsi Caesar cipher dengan
memanfaatkan `chr()` dan `ord()`. Ketikkan program bonus-mu di dalam file yang
sama.

<br>

### Penilaian

**80%** Kebenaran (Program berjalan dan berhasil menyelesaikan uji kasus),  
**10%** Kerapihan (Penamaan variabel jelas, mudah dibaca),  
**05%** Dokumentasi (Dokumentasi jelas, comment di bagian-bagian yang penting),  
**05%** Kesesuaian penamaan file submisi, kesesuaian output sesuai permintaan
soal.

<br>

<p style="text-align: center; font-size: 1.5em;"><strong>SELAMAT MENGERJAKAN
DAN HAPPY CODING 😊</strong></p>

<br>

**AA - END - KT - ZZ**

---

Diambil dari `Lab 3 DDP1 Lab Jumat.pdf` (Tutorial Lab 3 DDP1 B dan D
\-- 22 September 2017)
