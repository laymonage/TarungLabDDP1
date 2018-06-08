# Soal Tutorial

## Ujian Sebentar Lagi

Ujian Tengah Semester di Fasilkom tinggal sebentar lagi. Agar seluruh mahasiswa
di kelas bisa semakin paham dengan materi yang sudah diajarkan, Pak Dosen Cenna
meminta Benny sebagai salah satu asisten dosen DDP-1 untuk membuat sebuah
program mini kuis DDP-1 tentang konversi sistem bilangan desimal dan biner.
Karena batas waktu yang terlalu singkat disertai dengan banyaknya deadline yang
mengantri, Benny pun kewalahan membuat programnya. Benny pun akhirnya meminta
bantuanmu untuk membuat programnya. Karena kamu merupakan teman yang baik,
murah hati, dan tidak sombong, kamu pun setuju untuk membantu Benny.

**Ketentuan Mini Kuis DDP-1:**

- Soal yang disediakan dalam bentuk bilangan biner, dan dijawab dalam bentuk
  bilangan desimal.
- Jumlah soal terdiri dari 4 soal, masing-masing soal memiliki skor 25.
- Koleksi angka biner untuk soal bersifat ***hardcoded***. Untuk soal lab kali
  ini, kamu diharapkan untuk memasukkan angka biner berikut untuk dijadikan
  soal:
       ○ Soal no.1 = "11111100001"
       ○ Soal no.2 = "11111001111"
       ○ Soal no.3 = "10001100"
       ○ Soal no.4 = "100011101"

Setelah mengetahui ketentuan mini kuis DDP-1 yang diberitahu oleh Benny, kamu
mengingat salah satu materi kuliah DDP, yaitu function. Kamu akan membuat
program dengan menggunakan beberapa function sesuai dengan kebutuhan.

<br>

### Function pada Lab 5

Pada sesi lab kali ini, kamu akan diberikan template code oleh Benny, dan kamu
diharapkan untuk melengkapi beberapa function yang sudah diberikan oleh Benny.
Template code yang diberikan oleh Benny adalah sebagai berikut:

```python
def cetak_pertanyaan(urutan, angka_biner):
    #lengkapi function cetak_pertanyaan

def cek_jawaban(jawaban, angka_biner):
    #lengkapi function cek_jawaban

def main():
    print("Selamat datang di Mini Kuis DDP-1: Sistem Bilangan!")
    soal1 = "11111100001"
    soal2 = "11111001111"
    soal3 = "10001100"
    soal4 = "100011101"
    counter_soal = 1
    skor = 0

    while counter_soal <= 4:
        # di sini cetak pertanyaan sesuai dgn
        # counter soal dan angka biner untuk counter tsb

        # di sini minta input jawaban,
        # format output: "Jawab: (di sini input dimasukkan)"

        # di sini cek apakah jawabannya benar

        # counter soal bertambah

    #cetak skor akhir disini, format output: "Skor akhir: <skor>

if __name__ == '__main__':
    main()
```

<br>

### Penjelasan Function

- Function `cetak_pertanyaan(urutan, angka_biner)`  
  Format output:  
  `Soal <urutan>: Berapakah angka desimal dari bilangan biner <angka_biner>?`

  Contoh:  
    `cetak_pertanyaan(1, "10")`, akan mencetak:  
    `Soal 1: Berapakah angka desimal dari bilangan biner 10?`

<br>

- Function `cek_jawaban(jawaban, angka_biner)`  
  digunakan untuk mengecek jawaban dengan parameter
  `jawaban` dan `angka_biner`,  
  `return True` bila jawaban benar, dan `return False` bila jawaban salah.

  Contoh:  
  `cek_jawaban(2, "11")`, maka akan mengembalikan `False`.

###### Hint:

<sub><sup>Untuk konversi dari biner ke desimal, pakai fungsi:
`int(angka_biner_dalam_tipe_string, 2)`,
contoh: `int("10", 2)` => `2`.</sup></sub>

<br>

### Contoh sesi program berjalan (huruf tebal == masukan dari user)

<pre>
Selamat datang di Mini Kuis DDP-1: Sistem Bilangan!
Soal 1: Berapakah angka desimal dari bilangan biner 11111100001?
Jawab: <b>2017</b>
Soal 2: Berapakah angka desimal dari bilangan biner 11111001111?
Jawab: <b>1999</b>
Soal 3: Berapakah angka desimal dari bilangan biner 10001100?
Jawab: <b>142</b>
Soal 4: Berapakah angka desimal dari bilangan biner 100011101?
Jawab: <b>285</b>
Skor akhir: 75
</pre>

<br>

## Soal Bonus (Yey... ada bonus!)

Jika pertanyaan-pertanyaan pada mini kuis DDP-1 di atas bersifat
***hardcoded***, cobalah kamu buat jalannya program, di mana saat program
pertama kali dijalankan, program akan meminta masukkan dari user mengenai
soal-soal yang akan ditanyakan. Jadi saat program dijalankan, program akan
meminta 4 soal yang akan dikerjakan dan diinput oleh user, lalu 4 soal tersebut
disimpan untuk kemudian dikerjakan seperti soal yang biasa.

#### Contoh sesi program bonus berjalan (huruf tebal == masukan dari user)

<pre>
Selamat datang di Mini Kuis DDP-1: Sistem Bilangan!
Masukkan 4 soal: <b>11111100001 11111001111 10001100 100011101</b>
Soal 1: Berapakah angka desimal dari bilangan biner 11111100001?
Jawab: <b>2017</b>
Soal 2: Berapakah angka desimal dari bilangan biner 11111001111?
Jawab: <b>1999</b>
Soal 3: Berapakah angka desimal dari bilangan biner 10001100?
Jawab: <b>142</b>
Soal 4: Berapakah angka desimal dari bilangan biner 100011101?
Jawab: <b>285</b>
Skor akhir: 75
</pre>

<br>

## Penilaian

**80%** Kebenaran (Program berjalan dan berhasil menyelesaikan uji kasus),  
**10%** Kerapihan (Penamaan variabel jelas, mudah dibaca),  
**05%** Dokumentasi (Dokumentasi jelas, comment di bagian-bagian yang penting),  
**05%** Kesesuaian penamaan file submisi, kesesuaian output sesuai permintaan soal.

<br>

<p style="text-align: center; font-size: 1.5em;"><strong>SELAMAT MENGERJAKAN
DAN HAPPY CODING 😊</strong></p>

<br>

**AA - END - KT - ZZ**

---

Diambil dari `Lab 5 DDP1 Lab Jumat.pdf` (Tutorial Lab 5 DDP1 B dan D
\-- 6 Oktober 2017)
