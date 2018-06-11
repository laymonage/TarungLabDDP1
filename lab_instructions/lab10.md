# Tutorial 10: Rekursi

## Daftar Isi

- [Definisi rekursi](#definisi-rekursi)
- [Mendefinisikan fungsi rekursif](#mendefinisikan-fungsi-rekursif)
  - [Faktorial](#faktorial)
  - [Fibonacci](#fibonacci)
- [Iterasi versus rekursi](#iterasi-versus-rekursi)

<br>

## Definisi rekursi

[**Rekursi**][recursion] adalah [**rekursi**][recursion].

Rekursi dalam ilmu komputer adalah cara untuk menyelesaikan masalah dengan
memecah masalah tersebut menjadi masalah-masalah lebih kecil **yang serupa**.

Dalam pemrograman, biasanya rekursi berkaitan dengan suatu fungsi yang
**memanggil dirinya sendiri** hingga mencapai suatu kasus dasar *(base case)*.
***Base case*** adalah kasus di mana fungsi sudah dapat selesai secara langsung
(misal: nilai `return` sudah diketahui) tanpa harus memanggil dirinya kembali.
Kasus di mana fungsi belum dapat selesai secara langsung dan masih perlu
memanggil dirinya kembali disebut *recursive case*.

Perlu diingat bahwa setiap kasus rekursif harus mencapai kasus dasar pada
suatu saat. Jika tidak, akan terjadi rekursi berulang yang tidak berhenti
*(infinite recursion)*. Jadi, setiap kasus rekursif harus memecah kasus yang
sedang dikerjakan menjadi kasus yang lebih kecil (lebih dekat ke kasus dasar).

<br>

## Mendefinisikan fungsi rekursif

Dalam **mendefinisikan fungsi rekursif**, kita perlu melakukan dua hal, yaitu:

- mendefinisikan ***base case***, yaitu kasus yang solusinya didapat tanpa
  panggilan rekursif, dan
- mendefinisikan ***recursive case***, yaitu kasus yang solusinya didapat
  dengan memecahkan masalah serupa dengan kasus yang lebih sederhana
  (rekursif).

### Faktorial

Salah satu masalah yang bisa diselesaikan secara rekursif adalah **faktorial**.
Kita dapat memformulasikan faktorial seperti berikut.

```
faktorial(0) = 1
faktorial(1) = 1
faktorial(2) = 2 * 1 = 2
faktorial(3) = 3 * 2 * 1 = 6
faktorial(4) = 4 * 3 * 2 * 1 = 24
faktorial(5) = 5 * 4 * 3 * 2 * 1 = 120
...
faktorial(n) = n * (n - 1) * ... * 2 * 1
```

Sehingga, kita bisa memecah masalah faktorial menjadi dua kasus, yaitu kasus
dasar dan kasus rekursif seperti berikut.

```
faktorial(n) = 1, jika n <= 1 (kasus dasar)
             = n * faktorial(n - 1), jika n > 1 (kasus rekursif)
```

Dalam Python, fungsi di atas dapat ditulis seperti berikut.

```python
def faktorial(n):
    if n <= 1:  # base case
        return 1
    else:  # recursive case
        return n * faktorial(n - 1)
```

### Fibonacci

Contoh lain dari fungsi rekursif adalah fungsi untuk bilangan **Fibonacci**.
Pada barisan Fibonacci, berlaku hal berikut.

- Dua bilangan pertama adalah 0 dan 1
- Bilangan-bilangan berikutnya dalam barisan adalah hasil penjumlahan dua
  bilangan sebelumnya.


```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

Untuk menentukan bilangan Fibonacci ke-n (dimulai dari 0), kita dapat membuat
sebuah fungsi rekursif dengan formulasi berikut.

```
fibonacci(0) = 0  # base case 1
fibonacci(1) = 1  # base case 2
fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)  # recursive case
```

Dalam Python, kita dapat mendefinisikan fungsi sederhana berikut untuk
formulasi di atas.

```python
def fibonacci(n):
    if n == 0 or n == 1:  # base case
        return n
    else:  # recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)
```

<sup><sub>Hati-hati, fungsi di atas dapat menjadi *infinite* jika `n < 0`!
Coba atasi sendiri masalah tersebut sebagai latihan.</sub></sup>

<br>

## Iterasi versus rekursi

Jika dilihat, rekursi mirip dengan iterasi (perulangan). *Base case* mirip
dengan kondisi akhir perulangan, dan setiap langkah rekursif harus membawa kita
ke kondisi tersebut. Beberapa **perbedaan di antara keduanya** adalah sebagai
berikut.

**Iterasi:**

- Memakai struktur perulangan (`for` atau `while`) secara eksplisit.
- Berhenti jika kondisi perulangan bernilai `False`, atau elemen yang diiterasi
  sudah tidak ada.
- Kontrol perulangan menggunakan *counter* atau kondisi Boolean.

**Rekursi:**

- Memakai struktur percabangan (`if`, `if/else`, atau `if/elif/else`).
- Perulangan melalui pemanggilan fungsi berulang.
- Berhenti jika *base case* terpenuhi.
- Kontrol repetisi dengan membagi masalah menjadi kasus yang lebih sederhana
  dari masalah yang serupa.

**Setiap masalah yang bisa diselesaikan dengan cara iterasi pasti bisa
diselesaikan dengan cara rekursi, dan sebaliknya.** Hanya saja, ada
masalah-masalah tertentu yang lebih mudah diselesaikan dengan salah satu di
antara keduanya.

<br>

---

Diadaptasi dari:

- `Soal Tutorial Lab 10 - Kelas A.pdf`
  buatan **RCJ**, **WR**, **PKF**, dan **HFZ**
- `ddp1-17gasal-12.pdf` buatan **Adila Alfa Krisnadhi, Ph.D.**

dengan beberapa perubahan.

[recursion]: https://google.com/#q=recursion
