# Soal Tutorial

## Bennymart’s Ultra EZ Cashiers

### Persoalan Bagian Satu

Benny yang tidak terlalu kaya, ingin menambah uang jajannya. Dikarenakan itu,
Benny membuat usaha kecil yang bernama Bennymart. Suatu ketika Benny ingin
membuat modul python untuk kasir agar dia lebih mudah untuk menghitung total
belanja pembeli. Namun karena baru, dia hanya mengetes pada 3 produk, yaitu
coklat, mie, dan roti tawar. Coklat memiliki 3 jenis, yaitu kecil, sedang, dan
besar, lalu untuk mie terdapat 2 jenis, yaitu single dan double, dan roti tawar
terdapat 3 jenis, biasa, gandum, dan kupas. Berikut rinciannya:

- Coklat
  - Kecil = 5000/pcs
  - Sedang = 8000/pcs
  - Besar = 12000/pcs
- Mie
  - Single = 2500/pcs
  - Double = 3500/pcs
- Roti Tawar
  - Biasa = 12000/pcs
  - Gandum = 15000/pcs
  - Kupas = 13500/pcs

Namun Benny sudah lupa bagaimana cara menggunakan fungsi pada python. Sebagai
mahasiswa yang baik hati, pintar, punya banyak teman, dan pastinya suka
menolong, bantulah Benny membuat modull tersebut.

Kalian dapat menggunakan template dibawah ini:

```python
def beli_coklat(jumlah_kecil, jumlah_sedang, jumlah_besar):
    # TODO print banyaknya barang dibeli beserta harga
    return  # total_harga_coklat


def beli_mie(jumlah_single, jumlah_double):
    # TODO print banyaknya barang dibeli beserta harga
    return  # total_harga_mie


def beli_roti_tawar(jumlah_biasa, jumlah_gandum, jumlah_kupas):
    # TODO print banyaknya barang dibeli beserta harga
    return  # total_harga_roti_tawar


def checkout(total_harga):
    print("Total belanja sebesar", str(total))
```

Lalu kalau kalian sudah mengimplementasikan kodingan kalian ke dalam modul,
simpanlah modul tersebut dengan nama **`bennymart.py`**

### Persoalan Bagian Dua

Tepat setelah kalian mengimplementasikan modul di atas, saudara jauh Benny,
Dedepe dan Pedede datang mengunjunginya. Mereka juga ingin membeli coklat, mie,
dan roti di tokonya. Karena Benny baru saja membuat modulnya, dia belum sempat
membuat programnya. Anda dimintai tolong untuk membuat program penghitung harga
selama Benny sedang melayani saudara jauhnya. Buatlah program yang diinginkan
Benny sebagai berikut:

#### Input

- `beli [barang] [x] [y] [z]`  
  Item `[barang]` berupa coklat, mie, atau roti, lalu `x`,`y`, dan `z` adalah
  banyaknya item yang ingin dibeli dari setiap jenisnya. Namun karena mie hanya
  memiliki dua jenis, maka tidak terdapat nilai `z`.

- exit  
  Program berhenti menghitung barang

#### Output:

- `Membeli [barang] [jenis] sebanyak [jumlah] seharga [harga]`  
  (untuk semua jenis barang yang dibeli pelanggan)

- `Total belanja sebesar [total_harga]`  
  Output berupa harga total belanjaan. Kalian dapat panggil method checkout
  pada modul yang sudah kalian buat.

#### Contoh Input

```
beli coklat 2 2 1
beli mie 5 3
beli roti 0 1 0
exit
```

#### Contoh Output

```
Membeli coklat kecil sebanyak 2 seharga 10000
Membeli coklat sedang sebanyak 2 seharga 16000
Membeli coklat besar sebanyak 1 seharga 12000
Membeli mie single sebanyak 5 seharga 12500
Membeli mie double sebanyak 3 seharga 10500
Membeli roti tawar gandum sebanyak 1 seharga 15000
Total belanja sebesar 76000
```

**Hint : Seperti saat kalian menggunakan turtle, kalian dapat mengimport modul
yang baru saja kalian buat dengan `import bennymart`, dan memanggil fungsi
dengan cara `bennymart.[nama_fungsi]([parameter])`.**

Simpanlah program kalian dengan format **`Nama_NPM.py`**

### Penilaian

- 85% Kebenaran (Program berjalan, kasus uji benar)
- 10% Kerapihan (Penamaan variabel jelas, mudah dibaca)
- 5% Dokumentasi (Comment pada bagian-bagian penting)

<br>

**ALD DHA GIL DST**

---

Diambil dari `lab_6_Senin.pdf` (Tutorial Lab 6 DDP1 C -- 2 Oktober 2017)
