# Soal Tutorial

## Perbedaan Sahabat dan Teman

Pada suatu hari, di sebuah tempat kursus belajar terdapat sebuah permasalahan
yang cukup unik. Anak - anak yang kursus di tempat tersebut diwajibkan untuk mengetahui
apa perbedaan dari **persahabatan** dan **pertemanan** . Setiap anak yang masuk ke kursus
tersebut akan selalu diberi tutorial terkait persahabatan dan pertemanan. Pada akhirnya,
kursus tersebut sendiri menemukan sebuah masalah yang cukup berat karena tutorial yang
diajarkan. Ketika ada salah satu orang tua yang ingin menjemput anaknya dan bertanya
kepada salah satu anak apakah mengenal si “X” temannya si “Y”, seringkali terjadi
miskomunikasi karena perbedaan kata ‘teman’ dan ‘sahabat’ tersebut. Tutorial yang
disampaikan kepada setiap anak di tempat kursus tersebut adalah.

- Apabila X ber SAHABAT dengan Y, maka X sudah pasti ber TEMAN dengan Y.
- Apabila X ber TEMAN dengan Y, maka X belum tentu ber SAHABAT dengan Y.

Tempat kursus itu pun akhirnya kebingungan untuk mengatasi hal tersebut. Mereka tidak
dapat menghapus tradisi tutorial tersebut karena hal ini sudah menjadi tradisi tempat
tersebut sejak lama dan tidak boleh diubah. Akhirnya, setelah pemilik dari tempat
tersebut mengetahui bahwa kamu merupakan salah satu mahasiswa Fasilkom UI, maka ia
meminta kamu untuk membuat sebuah program untuk **mengetahui apakah si X dan Y
berteman atau bersahabat.** Bantulah pemilik tempat tersebut!

Hint : Gunakan tiga buah list yang menyimpan nama setiap anak, teman setiap anak,
dan sahabat setiap anak. Gunakan indexing pada list.

#### Format Input :
Input diminta hingga End-Of-File.

- TAMBAH \<nama>
    
    Menambahkan seorang anak ke dalam tempat kursus.\
    Output : 
    > “\<nama> berhasil ditambahkan”
    
    Jika \<nama> sudah ada dalam daftar, maka cetak keluaran :
    > “\<nama> sudah ada”

- \<nama1> \<nama2> BERTEMAN\
    Membuat \<nama1> dan \<nama2> berteman

- \<nama1> \<nama2> BERSAHABAT
    Membuat \<nama1> dan \<nama2> bersahabat

- SAHABAT \<nama1> BUKAN \< nama2 >
    Mencetak seluruh nama sahabat dari \<nama1> yang bukan sahabat dari \<nama2>\
    Output : 
    > “\<nama1>, \<nama2>, … , \<namaN>”

    dengan N merupakan jumlah sahabat dari \<nama> tersebut.\
    Jika tidak memiliki sahabat, tidak usah mencetak keluaran apapun.

- TEMAN \<nama1> \<nama2>
    Mencetak seluruh nama teman yang sama dari \<nama1> dan \<nama2>\
    Output : 
    > “ Teman dari \<nama1> dan \<nama2> adalah \<nama1>, \<nama2>, …
    \<namaN>”

    dengan N merupakan jumlah sahabat dari <nama> tersebut.\
    Jika tidak memiliki teman, cetak keluaran :
    > “\<nama1> dan \<nama2> tidak memiliki teman yang sama”

- END
    Mengakhiri program.
    Hint : Gunakan perintah “exit(None)”
    
Catatan :\
Untuk semua operasi, kecuali TAMBAH, jika nama anak yang diminta tidak terdapat pada
daftar anak di tempat kursus tersebut, maka cetak keluaran “ Nama tidak ditemukan” dan
operasi tidak dilaksanakan.

#### Contoh Input :
> TAMBAH Andi\
> TAMBAH Bayu\
> TAMBAH Coki\
> TAMBAH Dodi\
> TAMBAH Elia\
> Ani Andi BERTEMAN\
> Andi Bayu BERTEMAN\
> Bayu Dodi BERSAHABAT\
> Bayu Elia BERTEMAN\
> Elia Dodi BERSAHABAT\
> Andi Dodi BERTEMAN\
> Andi Elia BERSAHABAT\
> TEMAN Bayu Elia\
> TEMAN Andi Elia\
> SAHABAT Andi BUKAN Elia\
> SAHABAT Dodi BUKAN Elia

#### Contoh Output :
> Andi berhasil ditambahkan\
> Bayu berhasil ditambahkan\
> Coki berhasil ditambahkan\
> Dodi berhasil ditambahkan\
> Elia berhasil ditambahkan\
> Nama tidak ditemukan\
> Teman dari Bayu dan Elia adalah Andi, Dodi\
> Teman dari Andi dan Elia adalah Bayu, Dodi\
> Elia\
> Bayu, Elia

“<i>Hasil kerja keras kalian sangat kami apresiasi dibandingkan hasil yang kalian
copy dari orang lain</i>”

<br>

<p style="text-align: center; font-size: 1.5em;"><strong>SELAMAT MENGERJAKAN
DAN HAPPY CODING 😊</strong></p>

<br>

**PKF - HFZ - RCJ - WR**

---

Diambil dari `Soal Tutorial Lab 7 - Kelas A.pdf` (Tutorial Lab 7 DDP1 A
\-- 25 Oktober 2017)