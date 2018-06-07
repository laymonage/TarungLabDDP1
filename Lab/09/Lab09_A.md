# Soal Tutorial

## Ahli Waris

Pada suatu hari, X sedang berjalan pulang menuju rumahnya usai menjalani kehidupan kuliah
yang menyenangkan. Di perjalanan pulang X melihat banyak bangunan-bangunan mulai dari
restoran, hotel, dan juga rumah sakit.

Format Masukkan & keluaran:

- **BANGUN \<space> \<NAMA> \<space> \<JENIS BANGUNAN>**
    
    Keluarkan string dengan format:
    > “Gedung untuk \<JENIS BANGUNAN> bernama \<NAMA> telah dibangun.”

- **INFO \<space> \<NAMA>**
    
    Jika terdapat bangunan untuk \<NAMA> keluarkan string dengan format:
    > “\<JENIS BANGUNAN> dengan nama \<NAMA> telah menyewa bangunan selama N
      tahun”
    
    Dengan N merupakan lama bangunan tersebut telah disewa.\
    Jika bangunan untuk \<NAMA> belum dibangun, maka keluarkan string:
    > “Belum ada bangunan untuk \<NAMA> ”

- **JUALMAKANAN \<space> \<NAMA> \<space> \<LAMA WAKTU>**

    Jika terdapat restoran dengan nama tersebut, keluarkan:
    > “Restoran \<NAMA> menjual makanan kepada masyarakat selama \<LAMA WAKTU>
      tahun.”

    Jika tidak ada restoran dengan nama tersebut, keluarkan:
    > “Tidak ada restoran dengan nama \<NAMA> .”

- **TERIMATAMU \<space> \<NAMA> \<space> \<LAMA WAKTU>**

    Jika terdapat hotel dengan nama tersebut, keluarkan:
    > “Hotel \<NAMA> menerima tamu selama \<LAMA WAKTU> tahun.”
    
    Jika tidak ada hotel dengan nama tersebut, keluarkan:
    > “Tidak ada hotel dengan nama \<NAMA>.”

- **OBATIPASIEN \<space> \<NAMA> \<space> \<LAMA WAKTU>**

    Jika terdapat rumah sakitl dengan nama tersebut, keluarkan:
    > “Rumah sakit \<NAMA> mengobati pasien selama \<LAMA WAKTU> tahun.”

    Jika tidak ada rumah sakit dengan nama tersebut, keluarkan:
    > “Tidak ada rumah sakit dengan nama \<NAMA>.”
 
- **HITUNG UANG**
 
    Keluarkan string:
    > “Total aset kekayaan anda adalah Rp. N rupiah”
 
    Dengan N adalah total akumulasi biaya sewa dari setiap bangunan.

#### Catatan:
- Nama bangunan yang akan dibangun bersifat unik
- Lama waktu sewa dihitung pertahun, dengan ketentuan biaya sewa:
    - Rumah Sakit : Rp. 70.000.000,- / tahun
    - Hotel : Rp. 60.000.000,-/tahun
    - Restoran : Rp. 30.000.000,-/tahun
- Jangan lupa gunakan prinsip inheritance :)

#### Contoh input:
> BANGUN Margo HOTEL\
> BANGUN Solaria RESTORAN\
> BANGUN Bunda RUMAHSAKIT\
> JUALMAKANAN Solaria 3\
> OBATIPASIEN Bunda 2\
> JUALMAKANAN Margo 3\
> INFO Margo\
> HITUNG UANG\
> OBATIPASIEN Cipto 4\
> HITUNG UANG

#### Contoh output:
> Gedung untuk hotel bernama Margo telah dibangun.\
> Gedung untuk restoran bernama Solaria telah dibangun.\
> Gedung untuk rumah sakit bernama Bunda telah dibangun.\
> Restoran Solaria menjual makanan kepada masyarakat selama 3 tahun.\
> Rumah sakit Bunda mengobati pasien selama 2 tahun.\
> Tidak ada restoran dengan nama Margo.\
> Hotel dengan nama Margo telah menyewa bangunan selama 0 tahun.\
> Total aset kekayaan anda adalah Rp. 230000000 rupiah\
> Tidak ada rumah sakit dengan nama Cipto.\
> Total aset kekayaan anda adalah Rp. 230000000 rupiah

<br>

<p style="text-align: center; font-size: 1.5em;"><strong>SELAMAT MENGERJAKAN
DAN HAPPY CODING 😊</strong></p>

<br>

**PKF - HFZ - RCJ - WR**

---

Diambil dari `Soal Tutorial Lab 9 - Kelas A.pdf` (Tutorial Lab 9 DDP1 A
\-- 15 November 2017)