# Soal Tutorial

## UNIVERSITAS PARDEDE

Universitas Pardede merupakan sebuah universitas baru yang berfokus pada Ilmu
Komputer Aplikatif, yang diantaranya mengajari Dasar-Dasar Powerpoint,
Photoshop: Seni dan Desain, Pengembangan Pengoperasian Warnet, dsb.

Suatu hari, Univ. Pardede kewalahan karena management mahasiswanya masih
belum dibuat, sehingga UP mengadakan sayembara yang bernama “PLS BUILD OUR
DATABASE 2K17”, Benny sebagai mahasiswa Ilmu Komputer merasa tertarik mengikuti
lomba ini bukan karena tertantang kemampuan programmingnya, namun karena
hadiahnya yang berupa stok mie instan untuk 4 tahun. Oleh karena itu Benny
mengajak anda, mahasiswa Ilmu Komputer UI yang berdedikasi di dunia
programming, untuk membantunya membuat program sederhana untuk management data
mahasiswa Universitas Pardede.

**Tugas:**

Membuat program yang berguna untuk memasukkan data berupa matkul dan
pesertanya, serta beberapa operasi terkait matkul-matkul tersebut.

### Format masukkan:

1. `tambah <matkul> <npm1> <npm2> . . . <npmX>`  
   Menambahkan matkul baru dengan nama `<matkul>`, yang beranggotakan
   mahasiswa yang direpresentasikan dengan NPM, dari `<npm1>` hingga `<npmX>`.

2. `gabungan <matkul1> <matkul2>`  
   Mencetak NPM-NPM mahasiswa yang mengambil `<matkul1>` **ATAU** `<matkul2>`.

3. `pengambil <matkul1> <matkul2>`  
   Mencetak NPM-NPM mahasiswa yang mengambil `<matkul1>` **DAN** `<matkul2>`.

4. `hanya <matkul1> <matkul2>`  
   Mencetak NPM-NPM mahasiswa yang mengambil `<matkul1>` tetapi **TIDAK**
   mengambil `<matkul2>`.

5. `cetak <matkul>`  
   Mencetak NPM-NPM mahasiswa yang mengambil `<matkul>`.

6. `cetak matkul`  
   Mencetak NPM-NPM mahasiswa terdaftar di semua matkul yang ada.

7. `selesai`  
   Memberhentikan / keluar dari program

### Format Keluaran :

1. `tambah`:  
   `<matkul> berhasil ditambahkan!`

2. `gabungan`/`pengambil`/`hanya`:  
   **Ket : cetak NPM-NPM nya saja yang sesuai dengan kriteria perintahnya**

3. `cetak <matkul>`:  
   `<matkul> : <NPM tiap tiap peserta>`

4. `cetak matkul`:  
   **Ket : Untuk setiap matkul, print dengan format :**  
   `<matkul> : <NPM tiap-tiap peserta>`

5. `selesai`:  
   `Program berhenti!`

**Untuk lebih mengerti input dan output, coba lihat contoh di bawah.  
Contoh Jalannya Program:**

```
tambah DDP 12345 14045 15680 12345 65789
DDP berhasil ditambahkan!

cetak DDP
DDP : {15680, 12345, 14045, 65789}

tambah PPW 48224 12345 16898 14045
PPW berhasil ditambahkan!

tambah PSD 55668
PSD berhasil ditambahkan!

cetak matkul
DDP : {15680, 12345, 14045, 65789}
PPW : {48224, 12345, 16898, 14045}
PSD : {55668}

gabungan DDP PSD
{15680, 55668, 12345, 14045, 65789}

pengambil DDP PPW
{12345, 14045}

hanya DDP PPW
{15680, 65789}

hanya PPW DDP
{48224, 16898}

selesai
Program berhenti!
```

Dibawah ini disediakan *template* code untuk membantu kalian.  
**PERHATIAN : Penggunaan template ini tidak wajib, jika kalian memiliki solusi
sendiri yang lebih kalian mengerti, gunakan solusi kalian sendiri.**

```python
def main():
    matkul =  # Buat sebuah dictionary
    while  # Buat agar meminta input terus :
        masukan = input(">>> ")
        '''
        Buat agar program berhenti saat masukan adalah "selesai"
        '''

    masukan_split = masukan.split(" ")

    if masukan_split[0] == "tambah":
        nama_matkul = masukan_split[1]
        npm_semua = masukan_split[2:]
        # Buat sebuah set untuk menampung NPM-NPM diatas
        # Masukan ke dictionary yang telah dibuat diatas
        print(masukan_split[1],"berhasil ditambahkan!")

    # Gunakan method yang dimiliki set untuk melakukan 3 operasi di bawah ini
    elif masukan_split[0] == "gabungan":
    
    elif masukan_split[0] == "pengambil":
    
    elif masukan_split[0] == "hanya":
    
    # ------------------------------------------------------
    elif masukan_split[0] == "cetak":
        # Lakukan selection, apakah cetak salah satu matkul, atau semuanya
        # dan lakukan operasi print sesuai format
    else:
        print("Perintah salah !")
        
main()
```

<br>

**FDL IF PDD SAT**

---

Diambil dari `Soal Tutorial Lab 7 - Kelas C.pdf` (Tutorial Lab 7 DDP1 C
\-- 30 Oktober 2017)
