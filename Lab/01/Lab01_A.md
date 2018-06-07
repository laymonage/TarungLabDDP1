# Soal Tutorial

### Turtle

Benny dan Ibnu merupakan mahasiswa baru Fasilkom UI, setelah mempelajari cara
penggunaan IDLE, cara membuat program sederhana, dan cara menggambar dengan Turtle,
kini Ibnu dapat menulis program untuk membuat bentuk segitiga dengan turtle.

#### Contoh program:

```python
import turtle

# Instansiasi objek turtle
t = turtle.Turtle()

# Mengaktifkan pena
t.pendown()

# Memakai tinta biru
t.color('blue')

# Bergerak maju sejauh 100 satuan
t.forward(100)

# Memutar ke arah kiri sebesar 120 derajat
t.left(120)

t.forward(100)
t.left(120)
t.forward(100)

# Menon-aktifkan pena
t.penup()

# Menutup turtle setelah di- click
turtle.exitonclick()
```
![segitiga](image02.jpg)

Benny sebagai sesama mahasiswa baru tidak ingin kalah dengan Ibnu. Ia pun berniat membuat
bentuk yang lebih rumit dari Ibnu, yaitu bentuk segi empat . Sebagai mahasiswa Fasilkom UI
yang baik hati dan tidak sombong, Bantulah keinginan Benny!
- Buatlah program seperti diatas, tetapi sekarang dengan bentuk segi empat berwarna
  orange!
- Setelah itu, coba mintalah input dari user untuk digunakan sebagai panjang dari
  segi-segi nya
- Simpanlah file kalian dengan nama lab01_[nama kalian]_[npm].py

Hint: Pahamilah program Ibnu untuk mengerjakan soal ini

<br>

<p style="text-align: center; font-size: 1.5em;"><strong>SELAMAT MENGERJAKAN
DAN HAPPY CODING 😊</strong></p>

<br>

**IF - SAT - KF - PDD**

---

Diambil dari `lab01_ddp1_rev3.pdf` (Tutorial Lab 1 DDP1 A --
28 Agustus 2017)
