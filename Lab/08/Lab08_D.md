# Soal Tutorial

## Pardede Festival

<h5>"<i>Demi target 50 jam bulan ini</i>"</h5>

Benny Pardede maju sebagai project officer PARFEST X, dia punya ide radikal
untuk mendorong performa tiap panitia Parfest agar dapat bekerja secara
optimal. Benny ingin mengelola staf-stafnya dengan mudah, maka dari itu ia
ingin membentuk suatu sistem log panitia yang dapat mengevaluasi pekerjaan para
panitia - panitia tiap divisi. Benny akan menghargai hasil kerja para panitia
berupa BenCoin sesuai hasil jerih payah mereka dan berapa lama pekerjaannya,
tetapi karena dia sedang sibuk, dia meminta kalian para Petarung Koder untuk
membuat sistem tersebut.

### Spesifikasi:

- Template program sudah ada, kalian harus mengimplementasikan class
  `StaffAcara`, `StaffPartnership`, `StaffPublikasi` yang menginherit
  class `Staff`
- Kalian dilarang mengubah class `Staff` dan class `Manager` template
- Kalian dilarang membuat instance variable (bukan local variable) baru dalam
  class `StaffAcara`, `StaffPartnership`, `StaffPublikasi`
- Kalian dilarang membuat dict, set baru di seluruh program selain yang sudah
  ada di template
- REVISI: Penggunaan list untuk split input diperbolehkan
- Program menerima input berupa text berupa perintah dari user
- Program akan menerima input terus sehingga menerima perintah untuk berhenti
  (***EXIT***)

#### Jenis Perintah:

1. Rekrut staf
   Rekrut seseorang untuk menjadi sebuah staf divisi
2. Catat pekerjaan staf
   Setiap divisi punya cara kerja yang berbeda-beda, ada divisi yang bekerja
   dengan cepat ada juga yang membutuhkan waktu lama. Setiap staf punya
   progress masing-masing dan jika seorang staf progress nya sudah lebih dari
   atau sama dengan 100% maka dia tidak perlu bekerja lagi
3. Tampilkan informasi staf
   Output ke layar nama staf, jumlah jam kerja, jumlah penghasilan sementara
   dalam BenCoin, dan juga progress staf

#### Divisi-divisi:

<table>
  <tr>
    <th>Nama Divisi</th>
    <th>Cara Kerja</th>
    <th>Cara Perhitungan Gaji</th>
  </tr>
  <tr>
    <td>Acara</td>
    <td>Progres pekerjaan akan bertambah sebanyak 4% / jam</td>
    <td>Staf akan dibayar sejumlah 2000 BenCoin x persentase progressnya</td>
  </tr>
  <tr>
    <td>Partnership</td>
    <td>Progres pekerjaan akan bertambah sebanyak 1% / jam</td>
    <td>Staf akan dibayar sejumlah 4000 BenCoin x jam kerja x persentase
    progressnya</td>
  </tr>
  <tr>
    <td>Publikasi</td>
    <td>Progres pekerjaan akan bertambah sebanyak 20% / jam</td>
    <td>Staf akan dibayar sejumlah 1500 BenCoin x jam kerja</td>
  </tr>
</table>

<br>

#### Format Masukan:

1. `REKRUT;Nama staf;Divisi`  
   Rekrut staf baru. Tidak boleh merekrut seorang staf dua kali.
   Nama case insensitive

2. `KERJA;Nama staf;Jam`  
   Staf bekerja selama jam kerja yg diinput.  
   **Diasumsikan nama staf yang dimasukkan pada input ini telah menjadi staff
   dari PARFEST X.**

3. `LOG;Nama staf`  
   Menampilkan informasi staf.  
   **Diasumsikan nama staf yang dimasukkan pada input ini telah menjadi staff
   dari PARFEST X.**

4. `EXIT`  
   Program berhenti.

<br>

#### Format Keluaran:

1. `REKRUT`

   - Jika orang tersebut belum
     <pre><i><b>Nama</b> direkrut</i></pre>
   - Jika orang tersebut sudah menjadi bagian dari PARFEST X
     <pre><i><b>Nama</b> sudah direkrut sebelumnya</i></pre>

2. `KERJA`

   - Jika progress staf belum 100%
     <pre><i><b>Nama</b> bekerja selama <b>x</b> jam</i></pre>
   - Jika progress sudah 100% keatas
     <pre><i><b>Nama</b> sudah mencapai <b>x</b> % progress</i></pre>

3. `LOG`

<pre><i>>> <b>Nama</b>
Telah bekerja selama: <b>x</b> jam
Progress: <b>y</b> persen
Gaji sementara: <b>z</b> bencoin
</i></pre>

<br>

Note:  
Kalian tidak perlu menangani case - case yang tidak disebutkan
(e.g. input tidak sesuai format)

<br>

#### Contoh Input:

```
REKRUT;Yudhistira Khairunnisa;PUBLIKASI
REKRUT;Nabila Wisesa;PARTNERSHIP
REKRUT;Asel Ridwan;ACARA
REKRUT;Ahmad Tegar;PUBLIKASI
REKRUT;Asel Ridwan;PARTNERSHIP
KERJA;Yudhistira Khairunnisa;6
KERJA;Nabila Wisesa;6
KERJA;Nabila Wisesa;6
KERJA;Ahmad Tegar;4
KERJA;Asel Ridwan;5
KERJA;Nabila Wisesa;2
KERJA;Ahmad Tegar;6
KERJA;Yudhistira Khairunnisa;8
LOG;Yudhistira Khairunnisa
LOG;Nabila Wisesa
LOG;Asel Ridwan
LOG;Ahmad Tegar
EXIT
```

<br>

#### Contoh Output:

```
Yudhistira Khairunnisa direcruit
Nabila Wisesa direcruit
Asel Ridwan direcruit
Ahmad Tegar direcruit
Asel Ridwan sudah direkrut sebelumnya
Yudhistira Khairunnisa bekerja selama 6 jam
Nabila Wisesa bekerja selama 6 jam
Nabila Wisesa bekerja selama 6 jam
Ahmad Tegar bekerja selama 4 jam
Asel Ridwan bekerja selama 5 jam
Nabila Wisesa bekerja selama 2 jam
NN - YE - AHAhmad Tegar bekerja selama 6 jam
Yudhistira Khairunnisa sudah mencapai 120 % progress
>> Yudhistira Khairunnisa
Telah bekerja selama: 6 jam
Progress: 120 persen
Gaji Sementara: 9000 bencoin
>> Nabila Wisesa
Telah bekerja selama: 14 jam
Progress: 14 persen
Gaji Sementara: 784000 bencoin
>> Asel Ridwan
Telah bekerja selama: 5 jam
Progress: 20 persen
Gaji Sementara: 40000 bencoin
>> Ahmad Tegar
Telah bekerja selama: 10 jam
Progress: 200 persen
Gaji Sementara: 15000 bencoin
```

Penjelasan:

- Yudhistira Khairunnisa berhasil menjadi staff Publikasi.
- Nabila Wisesa berhasil menjadi staff Partnership.
- Asel Ridwan berhasil menjadi staff Acara.
- Ahmad Tegar berhasil menjadi staff Publikasi.
- Asel Ridwan gagal menjadi staff Partnership dikarenakan sudah menjadi staff Acara.
- Yudhistira Khairunnisa berhasil bekerja selama 6 jam.
- Nabila Wisesa berhasil bekerja selama 6 jam.
- Nabila Wisesa berhasil bekerja selama 6 jam.
- Ahmad Tegar berhasil bekerja selama 4 jam.
- Asel Ridwan berhasil bekerja selama 5 jam.
- Nabila Wisesa berhasil bekerja selama 2 jam.
- Ahmad Tegar bekerja selama 6 jam.
- Yudhistira Khairunnisa tidak dapat bekerja lagi dikarenakan telah memiliki
  progress `120% (6 jam * 20%)`.
- Yudhistira Khairunnisa adalah staff Publikasi. Dia berhasil bekerja selama
  6 jam. Progress yang telah dia lakukan adalah `6 * 20% = 120%`. Gaji yang dia
  dapatkan adalah `6 * 1500 = 9000` BenCoin.
- Nabila Wisesa adalah staff Partnership. Dia berhasil bekerja selama 14 jam.
  Progress yang telah dia lakukan adalah `14 * 1% = 14%`. Gaji yang dia
  dapatkan adalah `14 * 14 * 4000 = 784000` BenCoin.
- Asel Ridwan adalah staff Acara. Dia berhasil bekerja selama 5 jam. Progress
  yang telah dia lakukan adalah `5 * 4% = 20%`. Gaji yang dia dapatkan adalah
  `20 * 2000 = 40000` BenCoin.
- Ahmad Tega adalah staff Publikasi. Dia berhasil bekerja selama 10 jam.
  Progress yang telah dia lakukan adalah `10 * 20% = 200%`. Gaji yang dia
  dapatkan `10 * 1500 = 15000` BenCoin.

<br>

**NN - YE - AH**

---

Diambil dari `Soal Tutorial Lab 8 - Kelas D (Revisi 1).pdf` (Tutorial Lab 8
DDP1 D -- 17 November 2017)
