# Soal Tutorial

## Dunia Nokemon

Pada suatu hari, kehidupan kuliah di Fasilkom sangat tenang dan banyak waktu
luang. Kamu pun sedang bersantai dan tidur-tiduran di kamar. Beberapa saat
kemudian, tiba-tiba Ash mengetok pintu kamar kamu dengan keras dan segera masuk
ke dalam kamarmu. Ia menceritakan bahwa ia baru saja mengalami mimpi yang
memukau. Ia merasa ia telah menjelajahi sebuah dunia monster. Monster-monster
tersebut dapat ditangkap dan dipelihara. Mereka memanggil monster tersebut
dengan sebutan *Nokemon* dan mereka menggunakan Nokeball untuk menangkapnya.
Akan tetapi, bagian paling keren nya yaitu mereka mempertarungkan
*nokemon-nokemon* lucu yang mereka pelihara dari kecil demi memperoleh
kemenangan dan uang. "Wow sungguh mengasyikan? Jikalau *Nokemon* kita kalah dan
terluka, kita hanya perlu memasukkannya ke NokeCenter dan siap dipakai *tarung*
lagi!", seru Ash. Kemudian Ash dengan sangat memohon kepada kamu yang merupakan
ahli di bidang *ngoding* untuk membuatkannya sebuah *mini-game* yang
mensimulasikan dunia *Nokemon* tersebut, terutama pada bagian pertarungannya.

Berikut ini deskripsi dunia Nokemon yang diinginkan oleh Ash:

- `CAPTURE NOKEMON [Nama] [Level] [Power]`  
  Membuat seekor Nokemon yang memiliki atribut `[nama]`, `[level]`,
  `[power]`  
  Output:  
  `Berhasil menangkap Nokemon dengan nama [nama] level [level]`

- `TRAIN [Nama]`  
  Nokemon `[nama]` berlatih dan meningkatkan powernya sebesar 10%  
  Output:  
  `Berhasil melatih Nokemon [nama] , power meningkat menjadi [power]`

- `NOKECENTER [Nama]`  
  Nokemon `[nama]` dibawa ke NokeCenter untuk dipulihkan  
  Output:  
  `Nokemon [nama] telah dibawa ke NokeCenter dan dipulihkan`

- `STATS [Nama]`  
  Memperlihatkan informasi terkait dengan Nokemon `[nama]`  
  Output:  
  `Nama: [nama]`  
  `Level: [level]`  
  `Power: [power]`  
  `Health: [health]`

- `BATTLE [Nama Nokemon 1] [Nama Nokemon 2]`  
  Melakukan pertarungan antar Nokemon dengan `[nama 1]` dan `[nama 2]` dengan
  membandingkan (80% level + 20% power) dari masing-masing Nokemon. Nokemon
  yang menang akan bertambah levelnya sebanyak 1, dan Nokemon yang kalah akan
  menjadi pingsan. Nokemon yang sedang dalam keadaan pingsan tidak bisa
  melakukan pertarungan.

  Output:

  (Nokemon 1 atau Nokemon 2 dalam keadaan pingsan)  
  `[nama] tidak bisa melakukan pertarungan`

  (Nokemon 1 menang)  
  `[nama 1] menang bertarung melawan [nama 2] dengan selisih [power 1 - power 2]`

  (Nokemon 1 kalah)  
  `[nama 1] kalah bertarung melawan [nama 2] dengan selisih [power 2 - power 1]`

#### Catatan:

- Nama Nokemon hanya terdiri dari 1 kata dan dipastikan unik.
- Power yang dicetak pada Battle adalah nilai power final hasil kalkulasi level
  dan power.
- Saat ingin mencetak power, angka selalu dibulatkan menjadi 2 angka di
  belakang koma.

<br>

#### Contoh Input:

```
CAPTURE NOKEMON Pikachu 20 1000
CAPTURE NOKEMON Raichu 30 800
BATTLE Pikachu Raichu
STATS Raichu
TRAIN Raichu
TRAIN Raichu
BATTLE Raichu Pikachu
NOKECENTER Raichu
STATS Pikachu
STATS Raichu
BATTLE Raichu Pikachu
```

#### Contoh Output:

```
Berhasil menangkap Nokemon dengan nama Pikachu level 20
Berhasil menangkap Nokemon dengan nama Raichu level 30
Pikachu menang bertarung melawan Raichu dengan selisih 32.80
Nama : Raichu
Level : 30
Power : 800.00
Health : Pingsan
Berhasil melatih Nokemon Raichu, power meningkat menjadi 880.00
Berhasil melatih Nokemon Raichu, power meningkat menjadi 968.00
Raichu tidak bisa melakukan pertarungan
Nokemon Raichu telah dibawa ke NokeCenter dan dipulihkan
Nama : Pikachu
Level : 21
Power : 1000.00
Health : Sehat
Nama : Raichu
Level : 30
Power : 968.00
Health : Sehat
Raichu menang bertarung melawan Pikachu dengan selisih 1.60
```

Hints:

- Karena pemanggilan setiap perintah hanya menggunakan nama Nokemon saja,
  maka gunakan dictionary untuk menghubungkan nama tersebut dengan objek
  Nokemon nya.
- Selanjutnya telah disediakan template pengerjaan (tidak wajib pakai).

```python
class Nokemon:

    def __init__(self, nama, level, power):
        self.healthy = True

    def battle(self, other):
        # other merupakan objek Nokemon lain
        if self.healthy and other.healthy:
            if self.truePower() > other.truePower():
                # Lengkapi method bertarung
        else:
            # Jika ada Nokemon yang sedang pingsan

    def train(self):
        # Meningkatkan power Nokemon sebesar 10%

    def heal(self):
        # Memulihkan kondisi Nokemon

    def truePower(self):
        # Kalkulasi power untuk battle
        # 80% level dan 20% power

    def stats(self):
        # Print stats Nama, Level, Power, Health

# Dictionary untuk menyimpan objek menggunakan nama
daftar_nokemon = {}

while True:
    # Minta input perintah user
    perintah = input()
    # Split input
    perintah = perintah.split(' ')

    if perintah[0] == 'CAPTURE':
        # Buat objek baru, simpan ke daftar_nokemon
    elif perintah[0] == 'NOKECENTER':

    elif perintah[0] == 'TRAIN':

    elif perintah[0] == 'STATS':

    elif perintah[0] == 'BATTLE':
```

<br>

"<i>Hasil kerja keras kalian sangat kami apresiasi dibandingkan hasil yang kalian
copy dari orang lain</i>"

<br>

<p style="text-align: center;"><strong>HAPPY CODING :)</strong></p>

<br>

**RCJ WR PKF HFZ**

---

Diambil dari `Soal Tutorial Lab 8 - Kelas A.pdf` (Tutorial Lab 8 DDP1 A
\-- 08 November 2017)
