# Soal Tutorial

## Palindrom

**Palindrom** adalah sebuah kata, frasa, angka maupun susunan lainnya yang
dapat dibaca dengan sama baik dari depan maupun belakang (spasi antara
huruf-huruf biasanya diperbolehkan). Kata **"palindrom"** berasal dari bahasa
Yunani: palin (πάλιν; "lagi") and dromos (δρóμος; "arah").

Buatlah sebuah fungsi **rekursif** yang menerima satu parameter string berupa
sebuah kata yang mana fungsi tersebut akan me-*return* `True` apabila kata
tersebut adalah sebuah palindrom, return `False` apabila sebaliknya.

#### Contoh Input dan Output:

<pre>
Masukkan kata : <b>abc</b>
>> Kata 'abc' bukan palindrom

Masukkan kata : <b>kasurrusak</b>
>> Kata 'kasurrusak' adalah palindrom

Masukkan kata : <b>''</b>
>> String kosong adalah palindrom

Masukkan kata : <b>a</b>
>> Huruf 'a' adalah palindrom

Masukkan kata : <b>kasurRUSAK</b>
>> Kata 'kasurRUSAK' adalah palindrom
</pre>

#### Note:

Fungsi checkPalindrom yang dibuat berlaku case-insensitive, sehingga karakter
`'a'` dengan `'A'` dianggap sama. Jangan lupa output program disesuaikan dengan
contoh. Solusi harus dibuat dengan menggunakan rekursif. Selain itu, jawaban
tidak akan dinilai.

<br>

---

## Amoeba

*Amoeba, kadang disebut juga sebagai Ameba, ialah genus yang dimiliki protozoa,
yang eukariota uniseluler (organisme dengan organel sel terikat membran).
Amoeba terkenal berkembang biak dengan cara membelah diri.*

Pada suatu hari, kamu mengetahui bahwa terdapat sebuah tempat yang terdiri dari
sangat banyak amoeba. Saat berkunjung ke tempat tersebut, penjaga tempat
tersebut menceritakan bahwa terdapat satu amoeba yang mulai berkembang biak
sejak pertama kali ditemukan. Pada awalnya, jumlah amoeba di tempat tersebut
hanya satu. **Hari setelah amoeba tersebut ditemukan disebut sebagai sebagai
hari pertama, dan seterusnya. Amoeba tersebut dapat membelah diri menjadi dua
jenis amoeba, yakni amoeba aktif dan amoeba pasif.** Amoeba awal yang terdapat
di tempat tersebut diketahui sebagai amoeba aktif. Pada hari pertama, amoeba
tersebut membelah diri menjadi 2 amoeba aktif. Pada hari kedua dan seterusnya,
diketahui bahwa **setiap amoeba aktif** pada tempat tersebut membentuk **tiga
kloning amoeba aktif lainnya dan satu kloning amoeba pasif.** Buatlah sebuah
program yang dapat menghitung jumlah amoeba aktif pada tempat tersebut pada
hari ke x.

#### Contoh input dan output:

<pre>
Cek amoeba aktif pada hari ke : <b>3</b>
>> 32

Cek amoeba aktif pada hari ke : <b>5</b>
>> 512
</pre>

#### Keterangan:

Pada hari pertama, amoeba aktif bertambah menjadi dua buah. Pada hari kedua,
setiap amoeba aktif mengkloning dirinya menjadi 3 amoeba aktif dan 1 amoeba
pasif. Amoeba aktif menjadi 6 hasil kloning dan **2** amoeba aktif lama,
totalnya menjadi 8. Pada hari ketiga, 8 amoeba aktif yang ada mengkloning 3
amoeba aktif baru masing-masingnya sehingga total amoeba aktif hasil kloning
pada hari ketiga menjadi **24** amoeba dan amoeba aktif lama sebanyak 8 amoeba.
Oleh karena itu, solusi pada case pertama adalah 32. Setelah dihitung, pada
hari ke 5, amoeba aktif terdiri dari 512 amoeba.

#### Catatan:

**Pengerjaan soal harus menggunakan metode rekursif. Selain itu tidak akan
dinilai.**

<br>

**RCJ WR PKF HFZ**

---

Diambil dari `Soal Tutorial Lab 10 - Kelas A.pdf` (Tutorial Lab 10 DDP1 A
\-- 22 November 2017)
