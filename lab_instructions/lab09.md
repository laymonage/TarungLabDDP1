# Tutorial 09: Inheritance

## Daftar Isi

- [Definisi *inheritance*](#definisi-inheritance)
- [*Parent class*](#parent-class)
- [*Child class*](#child-class)
- [*Method overriding*](#method-overriding)
- [Fungsi `super()`](#fungsi-super)
- [*Multiple inheritance*](#multiple-inheritance)
- [Karakteristik *inheritance*](#karakteristik-inheritance)

<br>

## Definisi *inheritance*

***Inheritance*** merupakan sebuah konsep pewarisan atribut, baik *data*
*attributes* maupun *methods* yang dimiliki oleh sebuah *class* kepada *class*
turunannya. *Class* yang mewarisi dapat mendeskripsikan atribut yang lebih
spesifik di dalamnya, sedangkan atribut yang lebih umum akan diperoleh dari
*class* yang menjadi induknya.

Dengan konsep *inheritance*, kita dapat mendefinisikan beberapa *class* yang
mempunyai kemiripan, tetapi tetap mempunyai ciri khasnya masing-masing.

<br>

## *Parent class*

***Parent class*** merupakan sebuah *class* yang menjadi induk bagi *class*
lain. *Parent class* ini biasa disebut ***superclass*** atau *base class*.
*Class* ini memiliki ciri yang lebih umum daripada *class* yang mewarisinya.  
Perhatikan contoh berikut.

```python
class Fish:
    def __init__(self, first_name, last_name="Fish"):
        self.first_name = first_name
        self.last_name = last_name

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")
```

<br>

## *Child class*

***Child class*** merupakan sebuah *class* yang mewarisi atribut-atribut
*class* lain. *Child class* biasa disebut ***subclass*** atau *derived class*.
*Class* ini dapat mengakses atribut *class* lain yang menjadi induknya, baik
*data attributes* maupun *methods*.

```python
class ClownFish(Fish):
    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone.")

casey = ClownFish("Casey")
print(casey.first_name, casey.last_name)
casey.swim()
casey.live_with_anemone()
```

*Output:*

```
Casey Fish
The fish is swimming.
The clownfish is coexisting with sea anemone.
```

<br>

## *Method overriding*

Sebuah *subclass* juga dapat mendefinisikan kembali sebuah method yang sama
seperti di *superclass*-nya dengan definisi yang berbeda. Hal ini dinamakan
***overriding***.  
Perhatikan contoh berikut.

```python
class Shark(Fish):
    def __init__(self, first_name, last_name="Shark", skeleton="cartilage",
                 eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

sammy = Shark("Sammy")
print(sammy.first_name, sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)
```

*Output:*

```
Sammy Shark
The fish is swimming.
The shark cannot swim backwards, but can sink backwards.
True
cartilage
```

<br>

## Fungsi `super()`

**Fungsi `super()`** memungkinkan kita untuk mengakses isi *superclass* secara
utuh sebelum di-*override* oleh *subclass*.  
Perhatikan contoh berikut.

```python
class Trout(Fish):
    def __init__(self, first_name, water="freshwater"):
        super().__init__(first_name)
        self.water = water

    def swim_fabulously(self):
        super().swim()
        print("The fish swam fabulously.")

    def swim_backwards(self):
        super().swim_backwards()
        print("...and so it did.")

terry = Trout("Terry")
print(terry.first_name, terry.last_name)
terry.swim_fabulously()
terry.swim_backwards()
```

*Output:*

```
Terry Fish
The fish is swimming.
The fish swam fabulously.
The fish can swim backwards.
...and so it did.
```

<br>

## *Multiple inheritance*

Sebuah *class* dapat **mewarisi sifat dari lebih dari satu *superclass***.  
Perhatikan contoh berikut.

```python
class Coral:
    def community(self):
        print("Coral lives in a community.")

class Anemone:
    def protect_clownfish(self):
        print("The anemone is protecting the clownfish.")

class CoralReef(Coral, Anemone):
    pass

great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()
```

*Output:*

```
Coral lives in a community.
The anemone is protecting the clownfish.
```

<br>

## Karakteristik *inheritance*

Ketika mengakses nilai dalam sebuah atribut (misal: `instance_a.nama_atribut`),
Python mengikuti prinsip berikut:

- Cari atribut dalam *instance*.
- Jika tidak ditemukan, cari atribut dalam *class* dari *instance* tersebut.
- Jika tidak ditemukan juga, cari atribut dalam *superclass* dari *class*
  milik *instance* tersebut.

*Inheritance* membentuk relasi ***is-a***, contoh: `Shark` *is-a* `Fish`.

Inheritance berguna untuk:

- Spesialisasi
- *Overriding*
- Penggunaan ulang (*reuse*)

<br>

---

Diadaptasi dari:

- `Lab 09.pdf` buatan beberapa asisten dosen DDP1 2017 semester ganjil
- `ddp1-17gasal-11.pdf` buatan **Adila Alfa Krisnadhi, Ph.D.**

dengan beberapa perubahan.
