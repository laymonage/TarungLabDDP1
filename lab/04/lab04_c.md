# Soal Tutorial

## Benny’s Message Decryptor

Benny adalah seorang mahasiswa Fasilkom yang gemar mengirim pesan random. Suatu
ketika temannya mengirim pesan, namun karena tidak ingin pesannya dimengerti
oleh orang lain, pesan tersebut dikirim sudah dalam keadaan terenkripsi. Benny
sudah tahu bagaimana cara mendekripsi pesan tersebut. Namun lama kelamaan,
Benny jadi lelah untuk mendekripsi pesan tersebut. Anda sebagai mahasiswa
Fasilkom juga, bantulah Benny untuk membuat program untuk decrypt pesan
tersebut.

Benny memberikan spesifikasi enkripsi pesan tersebut sebagai berikut:

- Pesan tersebut memiliki key yang bernilai K

- Lalu pesan yang diterima di slice setiap K huruf  
  Contoh : “ayaskanaisafmoklsnadbayajaleddrap” dengan key bernilai 4  
  ayas | kana | isaf | mokl | snad | baya | jale | ddra | p

- Setelah itu pesan yang telah di slice setiap K huruf, dibalik per kelompok  
  Contoh : saya | anak | fasi | lkom | dans | ayab | elaj | ardd | p

- Semua string yang telah dibalik, selanjutnya digabung  
  Dalam contoh ini, hasilnya adalah “sayaanakfasilkomdansayabelajarddp”

#### Contoh Input

```
Pesan : ayaskanaisafmoklsnadbayajaleddrap
Key : 4
```

#### Contoh Output

```
sayaanakfasilkomdansayabelajarddp
```

**Hint : Gunakan Looping dan Slicing yang sudah diajarkan!**

#### Kasus Uji

Jika kalian telah selesai mengimplementasikan soal di atas ke dalam kodingan,
kalian bisa coba kasus uji ini:

| Input                       | Output yang diharapkan      |
| --------------------------- | --------------------------- |
| uratafgnklis02mo71          | tarungfasilkom2017          |
| 4                           |                             |
| salekf1pddklisaiumo         | kelasddp1fasilkomui         |
| 5                           |                             |
| rebmasemaggngnemagsamedanap | bersamamenggenggammasadepan |
| 3                           |                             |
| ulebesmayasmafkusamoklis    | sebelumsayamasukfasilkom    |
| 6                           |                             |

##### Catatan

- Panjang string belum pasti habis dibagi dengan key.

## Soal Latihan Bonus

Akhirnya Benny telah mampu melakukan decrypt pesan yang dikirim temannya.
Sekarang Benny ingin membalas pesan tersebut, namun pesan tersebut harus di
encrypt terlebih dahulu. Bantulah Benny membuat program untuk melakukan
enkripsi pesan tersebut!

Soal ini tidak perlu dikumpulkan, tetapi kami sarankan untuk mencoba
mengerjakannya jika soal sebelumnya sudah selesai.

### Penilaian

- 85% Kebenaran (Program berjalan, kasus uji benar)
- 10% Kerapihan (Penamaan variabel jelas, mudah dibaca)
- 5% Dokumentasi (Comment pada bagian-bagian penting)

<br>

**ALD DHA GIL DST**

---

Diambil dari `Lab 4 Senin.pdf` (Tutorial Lab 4 DDP1 C -- 18 September 2017)
