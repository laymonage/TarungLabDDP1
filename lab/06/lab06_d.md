# Soal Tutorial

## Benny’s Plagiarism Filter

Benny membutuhkan bantuan kalian untuk membuat plagiarism check/flter untuk
TP 3 dan TP 4! Benny mempunyai N set (S1, S2, .., SN) yang masing-masing
berisi file-file submisi tugas pemrograman, untuk mempermudah tugas kalian,
masing-masing submisi tugas sudah direpresentasikan oleh hashcode 64 bit!

Setiap submisi tugas yang berbeda akan memiliki hashcode yang berbeda dan dua
submisi tugas yang memiliki hashcode sama berarti memiliki konten yang sama
persis (plagiat). Benny menginginkan agar dari semua set submisi tugas, kalian
membuat sebuah set baru yang berisi submisi tugas yang tidak plagiat.

Dengan kata lain kalian harus membuat sebuah set S dimana setiap elemen pada S
hanya muncul satu kali pada semua set yang Benny berikan. Benny menjamin bahwa
pada setiap set yang ia berikan (S1, S2, .., SN) sudah memenuhi properti dari
set.

Format input:  
Baris pertama input berisi sebuah bilangan bulat `N`.
Untuk setiap `N` baris selanjutnya, terdapat sebuah set of 64 bit hashcode
(integer 64 bit)

Format output:  
Output hanya terdiri dari satu baris yaitu set yang berisi submisi tugas yang
tidak plagiat

#### Contoh input 1:

```
2
{41251512, 25151512}
{25151512, 54676367}
```

#### Contoh output 1:

```
{41251512, 54676367}
```

#### Contoh input 2:

```
3
{127461734, 491273471, 328947101}
{162349322, 328947101, 234784376}
{213434432, 123432429, 127461734}
```

#### Contoh output 2:

```
{491273471, 162349322, 234784376, 213434432, 123432429}
```

<br>

Hint:
Gunakan method `str.replace(find, replacement)` dan
method `str.split(splitter)`

<br>

**YE AHS**

---

Diambil dari `DDP1_D_Lab06.pdf` (Tutorial Lab 6 DDP1 D -- 27 Oktober 2017)
