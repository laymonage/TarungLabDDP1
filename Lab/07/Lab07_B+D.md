# Soal Tutorial

## BenJek™ (Benny Ojek)

<h5>"<i>Dari tadi belom nyampe Gerbatama juga? BenJek-in aja!</i>"</h5>

Peminat transportasi *online* sekarang ini semakin bertambah. Hampir setiap hari,
jalanan di ibukota selalu dipenuhi oleh transportasi *online*. Melihat peluang
yang sangat besar itu, Benny pun berniat untuk membuat sebuah transportasi
*online* terbaru, yaitu BenJek, tentunya dengan dukungan dari pendahulunya yang
sudah terjun di dunia transportasi *online*, yaitu Nadiem Makara, pendiri Ow-Jek.

Pada tahap pertama peluncuran BenJek, Benny merekrut sejumlah **driver**, dengan
ketentuan pendaftaran sebagai berikut:

- BenJek membuka 2 tipe layanan, yaitu “Normal Ojek” dan “Sport Ojek”.
- Setiap calon pendaftar diminta untuk melampirkan nama dan layanan BenJek yang
  ingin diikuti.

Jika calon pendaftar sudah diterima sebagai *driver* BenJek, mereka sudah bisa
mulai untuk melayani penumpang, dengan ketentuan-ketentuan sebagai berikut
(disesuaikan dengan tipe layanan yang dimiliki oleh *driver*):

| No  | Layanan Ojek | Ketentuan                                                                  |
| --- | ------------ | -------------------------------------------------------------------------- |
| 1.  | Normal Ojek  | - Tidak ada batas minimum perjalanan <br> - Tarif per KM sebesar Rp. 1.000 |
| 2.  | Sport Ojek   | - Minimal perjalanan sejauh 10 KM <br> - Tarif per KM sebesar Rp. 2.500    |

Setiap akhir bulan, bagian keuangan BenJek memulai perhitungan untuk membagi
pendapatan yang diperoleh *driver* BenJek. Adapun ketentuan pembagian pendapatan
adalah sebagai berikut:  
***Driver dari layanan manapun akan mendapatkan 80% dari total pendapatan mereka, BenJek
akan mendapatkan 20% dari total pendapatan mereka.***

Untuk mempermudah kinerja dari BenJek, Benny memintamu untuk membuat
sebuah program yang bekerja sesuai dengan ketentuan-ketentuan yang sudah dijabarkan
di atas.

<br>

### ASUMSI

- Nama *driver* yang akan mendaftar dijamin unik, sehingga calon *driver* yang
  memiliki nama yang sama dengan salah satu *driver* yang sudah mendaftar, maka
  calon *driver* tersebut tidak dapat mendaftar.
- Satu *driver* hanya bisa punya satu jenis layanan ojek (salah satu dari
  NORMAL atau SPORT).

<br>

### FORMAT INPUT

- `DAFTAR <nama_driver> <NORMAL/SPORT>`  
   Mendaftarkan `<nama_driver>` ke dalam sistem BenJek dan akan melayani
   NORMAL/SPORT Ojek.


- `MULAI PERJALANAN <nama_driver> <jarak_ditempuh_km>`  
  `<nama_driver>` melakukan perjalanan sejauh `<jarak_ditempuh_km>`.
  Hasil yang diperoleh akan dimasukkan ke dalam pendapatan *driver*.


- `CEK PENDAPATAN <nama_driver>`  
  Command ini mengecek jumlah pendapatan sementara yang diperoleh oleh
  &lt;nama_driver>.


- `AKHIR BULAN`  
  Command ini akan mengakhiri program (exit program).
  Membagi pendapatan antara *driver* dengan BenJek.

<br>

### FORMAT OUTPUT

- `DAFTAR <nama_driver> <NORMAL/SPORT>`  
    ● **Jika *driver* belum ada di dalam sistem:**  
    `<nama_driver> berhasil mendaftar sebagai driver BenJek layanan
    <NORMAL/SPORT>`  
    ● **Jika *driver* sudah ada di dalam sistem:**  
    `<nama_driver> gagal mendaftar sebagai driver BenJek`

<br>

- `MULAI PERJALANAN <nama_driver> <jarak_ditempuh_km>`  
    ● **Jika *driver* sudah ada di dalam sistem dan bisa melakukan
    perjalanan:**  
    `<nama_driver> melakukan perjalanan sejauh <jarak_ditempuh_km> dan
    mendapatkan pendapatan sebesar <pendapatan_diperoleh>`  
    ● ** Jika *driver* sudah ada di dalam sistem dan tidak bisa melakukan
    perjalanan:**  
    `<nama_driver> tidak bisa melakukan perjalanan`  
    ● **Jika *driver* tidak ada di dalam sistem:**  
    `<nama_driver> tidak ada di dalam sistem`

<br>

- `CEK PENDAPATAN <nama_driver>`  
    ● **Jika *driver* sudah ada di dalam sistem**  
    `<nama_driver> memiliki pendapatan sebesar Rp.<pendapatan_diperoleh>`  
    ● **Jika *driver* tidak ada di dalam sistem**  
    `<nama_driver> tidak ada di dalam sistem`

<br>

- `AKHIR BULAN`


```
Sudah akhir bulan! Pendapatan BenJek bulan ini adalah Rp.<pendapatan_BenJek>
Daftar pendapatan pengemudi:
<nama_driver_1>: Rp.<pendapatan_diperoleh_1>
<nama_driver_2>: Rp.<pendapatan_diperoleh_2>
...
<nama_driver_n>: Rp.<pendapatan_diperoleh_n>
```

<br>

### BONUS (?)

Setelah Benny sukses meluncurkan layanan BenJek dengan Normal Ojek dan Sport
Ojek, Benny berencana untuk membuka layanan baru dengan nama Cruiser Ojek.
Adapun ketentuan untuk Cruiser Ojek adalah sebagai berikut:

- Minimal perjalanan sejauh 25 KM
- Tarif per KM sebesar Rp. 7.500

Silakan implementasikan layanan Cruiser Ojek di dalam kalian untuk
menyelesaikan soal bonus!

<br>

**AA - END - KT - ZZ**

---

Diambil dari `LAB 7 DDP-1 KELAS B DAN D.pdf` (Tutorial Lab 7 DDP1 B dan D
\-- 10 November 2017)
