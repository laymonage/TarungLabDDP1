# Soal Tutorial

## Benny’s EZ* Number Converter™
###### \*Syarat dan Ketentuan Berlaku

Benny adalah mahasiswa DDP1 yang telah belajar Number Systems di kelasnya.
Pada suatu hari, Benny yang sedang gabut mengakses SCELE dan terkejut setelah melihat
bahwa ada tugas tentang Number System. Benny pun makin terkejut setelah mengetahui
bahwa deadlinenya adalah seminggu dari tanggal diberinya soal, dan untuk ketiga kalinya
Benny sangat terkejut setelah mengetahui bahwa soalnya sudah di post dari 6 hari yang
lalu.

*Moral of the Story: Rajin-rajinlah cek SCELE*

Akhirnya Benny berinisiatif untuk membuat program sederhana yang bisa
mengerjakan tugasnya dengan lebih cepat, dengan kriteria sebagai berikut:

- Programnya akan menerima input angka serta basisnya (2/8/16) dan mengubahnya
  ke dalam bentuk desimal (basis 10).

- Input memiliki format:\
  **\[basis awal]\[angkanya]**\
  Contoh: ```hexal A10```
  
  Format basis awal: **binary**, **octal**, atau **hexal** (basis 2, 8, atau 16)

- Output hanya menampilkan angka hasilnya saja, untuk contoh diatas hasilnya :
  ```2576```

- Asumsikan bahwa (tidak perlu dicek):
    - Angka input bilangan positif ril.
    - Angka input **tidak** melebihi basenya. (e.g input **hexal WXYZ**, **binary 4567**, dsb.).
    - Angka input **tidak** bisa overflow (melebihi batas).

- Disediakan **template** untuk meminta input sebaris, silakan lihat templatenya
  dibawah dan sesuaikan penggunaannya dengan program kalian.

- **Tidak boleh** menggunakan built-in konverter dari python, saatnya kalian ngoding
  nguli !!!! :D
    - Forbidden functions : **bin()**, **oct()**, **hex()**
    - Dan fungsi konversi lainnya
    - Penggunaan int() **hanya boleh** untuk merubah string menjadi int saja ( “1”
      menjadi 1 ) **tidak boleh** untuk mengkonversi nilai.

- Input bisa berupa floating number **(bin 1101110.11001, oct 345.337, hex 345.0)**
    - Program akan terus meminta input, dan program akan berakhir saat user
      memberi input **"keluar"** (tanpa tanda kutip)

### Template:

```python
# Gunakan isi template ini, dan sesuaikan dengan kodingan kalian
# Kalian boleh tidak menggunakan beberapa / semua bagian dari template
# dan menggunakan versi kalian sendiri
masukan = # minta input disini
masukan_split = masukan.split(" ") #split antara [base] dan [angka]
baseInput = masukkan_split[0] # [base]
numberInput = masukkan_split[1] # [angka]
# [angka] tanpa bagian pecahannya, bisa digunakan untuk mencari pangkat
numberWithoutFraction = (numberInput.split(".")[0]
numberInputClean = numberInput.replace(".","") #[angka] tanpa titik
```

Fungsi yang dapat membantu kalian :
- **len(x)** : Fungsi untuk mendapatkan panjang dari suatu variable seperti string, list,
  dsb. Dimana x adalah variable itu yang dijadikan parameter

**Penting** : Silakan baca kembali materi base conversion agar paham mengenai apa yang
harus dilakukan

Berikut contoh jalannya program:

<pre>
Selamat datang di Benny™ EZ Converter
Format input [base] [angka]
ketik keluar untuk keluar program
>>> binary 1101.1
13.5
>>> octal 4437.1234
2335.1630859375
>>> hexal FFFF.FFFF
65535.99998474121
>>> keluar


================
Program Berhenti
>>>
</pre>

**Keterangan:** Pesan di 3 line pertama dan 2 line terakhir program tidak wajib dilakukan.

**Jika program kalian telah selesai, coba test case dibawah ini untuk mengecek
kebenaran program kalian:**

| Basis | Input              | Output 
| ----- | ------------------ | -------------------
| 2     | 11101111.110011111 | 239.810546875
| 8     | 772113.77777777    | 259147.9999999404
| 16    | FFFFFFFF.FFFF      | 4294967295.9999847
| 16    | 45AF3756.FD4713    | 1169110870.9893658
| 8     | 3546621.776351     | 970129.9969825745

### Penilaian

- Program 85%
- Kerapihan (contoh: penamaan variabel, readability ) 10%
- Dokumentasi (comment yang menjelaskan program) 5% **(untuk lab kali ini wajib
  pakai comments ya! :D)**
  
<br>

**FDL IF PDD SAT**

---

Diambil dari `lab03_senin.pdf` (Tutorial Lab 3 DDP1 C --
11 September 2017)

