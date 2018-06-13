# Soal Tutorial

## PARDEDE PRODUCTIONS

*"Karena Because Always Selalu"*

Benny merupakan pemilik Pardede Productions, sebuah channel di Youtube yang
terkenal dengan video clickbait dan video provokatif, Channel tersebut sudah
sangat besar namanya dikarenakan banyaknya orang Indonesia yang gampang
terpicu. Oleh karena itu, wajar jika karyawan di Pardede Productions cukup
banyak.

Suatu hari Benny mengalami kesulitan dalam manajemen karyawan, Benny butuh
suatu solusi untuk mempermudah dalam manajemen channelnya, Ia pun meminta Anda,
Programmer handal kecintaan ibu dan ayah, untuk membuat prototip program
manajemen karyawan Pardede Productions!

**Tugas:**  
Membuat program untuk organisasi karyawan berdasarkan divisinya, lalu membuat
operasi untuk karyawan tersebut dalam melakukan pekerjaan sesuai divisinya.
Akan ada 3 divisi yaitu **`Staff`**, **`Filmmaker`**, dan **`Marketing`** .
Program akan meminta input terus sampai user memberikan input **`GAJIAN`**.

### Format Masukan:

1. **`REKRUT;Nama Karyawan;Divisi`**  
   Melakukan rekrutmen pegawai baru dengan divisi sesuai masukan.

2. **`INFO;Nama Karyawan`**  
   Memberikan informasi berupa divisi dan jumlah jam kerja karyawan tersebut

3. **`NGANTOR;Nama Karyawan;Jam`**  
   Seorang pegawai melakukan pekerjaannya sebagai seorang **`Staff`** dengan
   lama waktu sesuai masukan

4. **`PRODUKSI;Nama Karyawan;Jam`**  
   Seorang pegawai melakukan pekerjaannya sebagai seorang **`Filmmaker`**
   dengan lama waktu sesuai masukan

5. **`PROMOSI;Nama Karyawan;Jam`**  
   Seorang pegawai melakukan pekerjaannya sebagai seorang **`Marketing`**
   dengan lama waktu sesuai masukan

6. **`GAJIAN`**  
   Semua karyawan mendapat gaji sejumlah **`jam kerja`** \*
   **`rate per jam`**, dengan rate per jam sesuai divisinya

### Format Output

Format Keluaran:

1. **`REKRUT;Nama Karyawan;Divisi`**  
   Pegawai dengan nama `Nama Karyawan` bergabung dengan Pardede Productions
   sebagai `Divisi`

2. **`INFO;Nama Karyawan`**  
   `Nama Karyawan` seorang `Divisi` , jam kerja : `jam kerja`

3. **`NGANTOR;Nama Karyawan;Jam`**  
   `Nama Karyawan` bekerja di kantor selama `Jam` jam

4. **`PRODUKSI;Nama Karyawan;Jam`**  
   `Nama Karyawan` membuat konten video baru selama `Jam` jam

5. **`PROMOSI;Nama Karyawan;Jam`**  
   `Nama Karyawan` mempromosikan channel Pardede Productions selama `Jam` jam

6. **GAJIAN**  
   `Nama Karyawan` menerima gaji sebanyak Rp. `<jam kerja * rate per jam>`

### Keterangan:

- Karyawan yang di REKRUT **tidak** akan memiliki nama yang sama.
- Nama Karyawan di operasi NGANTOR, PRODUKSI, dan PROMOSI adalah
  nama karyawan yang **sudah terdaftar**
- Satu karyawan hanya bisa terdaftar di **salah satu** divisi saja
- **Rate Per Jam** :
  - Staff = 75.000
  - Filmmaker = 100.000
  - Marketing = 50.000
- Jika memanggil Pegawai yang **bukan** divisinya (misalnya memanggil nama
  seorang Filmmaker di operasi NGANTOR), berikan output :  
  Pegawai dengan nama `Nama Karyawan` bukan seorang `Divisi Tujuan`
- Terapkan prinsip-prinsip **Inheritance**

#### Contoh Input:

```
REKRUT;Arturia Pendragon;Staff
REKRUT;Master Gudako;Filmmaker
REKRUT;Gilgamesh;Marketing
REKRUT;Jyanu;Filmmaker
NGANTOR;Arturia Pendragon;8
NGANTOR;Jyanu;5
PRODUKSI;Master Gudako;13
PROMOSI;Gilgamesh;5
INFO;Arturia Pendragon
NGANTOR;Arturia Pendragon;10
GAJIAN
```

#### Contoh Output:

```
Pegawai dengan nama Arturia Pendragon bergabung dengan Pardede Productions sebagai Staff
Pegawai dengan nama Master Gudako bergabung dengan Pardede Productions sebagai Filmmaker
Pegawai dengan nama Gilgamesh bergabung dengan Pardede Productions sebagai Marketing
Pegawai dengan nama Jyanu bergabung dengan Pardede Productions sebagai Filmmaker
Arturia Pendragon bekerja di kantor selama 8 jam
Pegawai dengan nama Jyanu bukan seorang Staff
Master Gudako membuat konten video baru selama 13 jam
Gilgamesh mempromosikan channel Pardede Productions selama 5 jam
Arturia Pendragon seorang Staff, jam kerja : 8
Arturia Pendragon bekerja di kantor selama 10 jam
Arturia Pendragon menerima gaji sebanyak Rp.1350000
Master Gudako menerima gaji sebanyak Rp.1300000
Gilgamesh menerima gaji sebanyak Rp.250000
Jyanu menerima gaji sebanyak Rp.0
```

**Disediakan Template untuk mengerjakan Program diatas pada file
`template_09_c.py`. Kriteria penilaian berdasarkan seberapa dalam Anda
menerapkan teknik inheritance (superclasses, subclasses,variable & function
overriding, dsb).**

<br>

**FDL IF PDD SAT**

---

Diambil dari `Soal Tutorial Lab 9 - Kelas C` (Tutorial Lab 9 DDP1 C
\-- 13 Oktober 2017)
