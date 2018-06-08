# Soal Tutorial

## Secret Agent 069 Benny

<h5>"<i>Kriptografi caesar cipher terlalu sulit untuk diimplementasikan, aku
pilih cara yang lebih mudah saja</i>" -Agen Benny</h5>

Agen rahasia Benny menyembunyikan beberapa informasi rahasia di dalam suatu
file yang tampak normal. Rahasia tersebut berada diantara sebuah tag `<start>`
dan sebuah tag `<end>`. Karena Anda tidak suka Benny, maka Anda akan membuat
program yang mengekstrak informasi yang dirahasiakan oleh Benny untuk
kemudian dibocorkan ke pihak yang melawan Benny. Agen Lesa, musuh Benny, akan
membantu Anda.

Agen Lesa memberikan Anda sebuah file berupa transkrip komunikasi agen Benny,
program kalian harus bisa memindahkan semua string yang berada di antara tag
`<start>` dan tag `<end>` ke sebuah file lain. Dijamin bahwa setiap tag
`<start>`, tag yang selanjutnya akan muncul adalah tag `<end>`, jadi tidak
akan ada semacam `...<start>...<start>...<end>...<end>...`.

#### Contoh input stdin:

```
Masukkan nama file input dan output: input101.txt output66.txt
```

#### Contoh output stdout:

```
Rahasia telah terbongkar, silakan cek file output66.txt
```

#### Contoh isi file input:

```
Selamat siang pak, saya ingin menginformasikan <start>Target<end>
Pengumpulan Dana sebesar<start>550<end>0000 sudah tercapai! Uangnya
sebagian besar<start> sudah di <end> tangan saya, sekarang kita hanya
perlu menentukan <start>lokasi<end> acara. Terima Kasih
```

#### Contoh isi file output:

```
Target 550 sudah di lokasi
```

<br>

### BONUS! (yeay ada bonus)

Agen Lesa sebagai manusia tidak luput dari salah, jika nama file yang
diberikan oleh agen Lesa salah, sehingga bisa jadi tidak ada atau terdapat
masalah lainnya, batalkan eksekusi, dan laporkan pada standard output.

#### Contoh output stdout:

```
File input65536.txt bermasalah! Benny lolos kali ini.
```

<br>

**NN - WP - YE - AH**

---

Diambil dari `Lab 4 Dasar-Dasar Pemrograman 1 - REVISI.pdf` (Tutorial Lab 4
DDP1 B dan D -- 29 September 2017)
