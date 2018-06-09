# Tutorial 07: Set dan Dictionary

## Daftar Isi

- [*Set*](#set)
  - [Definisi *set*](#definisi-set)
  - [Inisialisasi *set*](#inisialisasi-set)
  - [Fungsi dan operasi pada *set*](#fungsi-dan-operasi-pada-set)
- [*Dictionary*](#dictionary)
  - [Definisi *dictionary*](#definisi-dictionary)
  - [Inisialisasi dan akses *dictionary*](#inisialisasi-dan-akses-dictionary)
  - [Fungsi dan operasi pada *dictionary*](#fungsi-dan-operasi-pada-dictionary)

<br>

## *Set*

### Definisi *set*

***Set*** (himpunan) merupakan salah satu struktur data yang berisi kumpulan
objek. *Set* sering kali dipakai untuk mengumpulkan data-data dalam jumlah
tertentu/banyak menjadi sebuah kumpulan data yang unik dan memiliki elemen yang
berbeda beda. *Set* pada Python dapat menampung objek yang tipenya berbeda-beda
dan **urutan elemen pada *set* akan acak**.

Ciri-ciri *set*, antara lain:

- Elemen-elemen yang berada di dalam *set* bersifat *hashable*.
- Setiap elemen di dalam *set* adalah unik/tidak sama.
- *Set* merupakan sebuah kumpulan elemen yang tidak memiliki urutan tertentu.
- *Set* bersifat *mutable*. Elemen di dalamnya bisa dibuang/diganti.

<br>

### Inisialisasi *set*

Terdapat dua jenis cara untuk menginisialisasi/membuat sebuah *set*.

**1. Menginisialisasi sebuah *set* kosong terlebih dahulu,**
**kemudian menambahkan elemen-elemennya satu per satu**

```python
>>> a_set = set()  # Inisialisasi set kosong
>>> a_set.add(1)  # Menambahkan 1 ke dalam set
>>> a_set.add('a')  # Menambahkan 'a' ke dalam set
>>> print(a_set)
{1, 'a'}
```

**2. Menginisialisasi sebuah *set* langsung dengan isi dari *set* tersebut**

  a. Daftar elemen didefinisikan secara eksplisit di dalam *set*

```python
>>> a_set = {'a', 'n', 4, 2.0, 4, 2.0}
>>> print(a_set)
{'n', 2.0, 4, 'a'}
```

  b. Menggunakan `set(iterable)`

```python
>>> a_set = set('ano')
>>> print(a_set)
{'o' , 'a' , 'n'}
```

  c. *Set comprehension*

```python
>>> a_set = {element for element in 'this is tutorial lab 7'
...          if element.isalpha()}
>>> print(a_set)
{'u', 'o', 'a', 'r', 's', 'h', 't', 'l', 'b', 'i'}
```

**Perhatikan bahwa hasil masukan elemen-elemen di dalam *set* adalah acak.**

<br>

### Fungsi dan operasi pada *set*

| Fungsi/operasi            | Keterangan                                              |
| ------------------------- | ------------------------------------------------------- |
| `len(set_a)`              | mengembalikan banyaknya elemen dari set_a               |
| `x in set_a`              | memeriksa apakah x ada di dalam set_a                   |
| `x not in set_a`          | sama dengan `not (x in set_a)`                          |
| `set_a.pop(elem)`         | buang `elem` dari `set_a`, mengembalikan `elem`         |
| `min(set_a)`              | mengembalikan nilai terkecil dalam `set_a`              |
| `max(set_a)`              | mengembalikan nilai terbesar dalam `set_a`              |
| `sum(set_a)`              | mengembalikan hasil penjumlahan semua elemen di `set_a` |
| `set_a.isdisjoint(set_b)` | memeriksa apakah `set_a` saling lepas dengan `set_b`    |
| `set_a.issubset(set_b)`   | memeriksa apakah setiap elemen `set_a` ada di `set_b`   |
| `set_a.issuperset(set_b)` | memeriksa apakah setiap elemen `set_b` ada di `set_a`   |
| `for elem in set_a`       | mengiterasi seluruh elemen `set_a` secara acak          |

Selain yang ada di atas, ada beberapa operasi penting yang harus dipahami
mengenai *set*, yaitu ***copy***, ***union***, ***intersection***,
***difference***, dan ***symmetric difference***.

1. *Copy* (salin)

```python
>>> set_a = set('Matematika')  # Set berisi karakter-karakter pada 'Matematika'
>>> print(set_a)
{'e', 'a', 'k', 'M', 'i', 'm', 't'}
>>>
>>> set_b = set_a.copy()  # Menyalin isi set_a ke set_b
>>> print(set_b)
{'e', 'a', 'k', 'M', 'i', 'm', 't'}
>>>
>>> set_a.remove('M')  # Menghapus elemen 'M' di dalam set_a
>>> print(set_a)
{'e', 'a', 'k', 'i', 'm', 't'}
>>> print(set_b)
{'e', 'a', 'k', 'M', 'i', 'm', 't'}  # Elemen 'M' tetap ada di set_b
```

2. *Union* (gabungan)

```python
>>> set_a = {1, 2}
>>> set_b = {2, 4, 5}
>>> set_c = set_a.union(set_b)
>>> set_d = set_a | set_b
>>> print(set_c)
{1, 2, 4, 5}  # Gabungan elemen-elemen pada set_a dan set_b, tanpa duplikasi
>>> print(set_d)
{1, 2, 4, 5}
```

3. *Intersection* (irisan)

```python
>>> set_a = {1, 2}
>>> set_b = {2, 4, 5}
>>> set_c = set_a.intersection(set_b)
>>> set_d = set_a & set_b
>>> print(set_c)
{2}  # Irisan elemen-elemen pada set_a dan set_b
>>> print(set_d)
{2}
```

4. *Difference* (beda)

```python
>>> set_a = {1, 2}
>>> set_b = {2, 4, 5}
>>> set_c = set_a.difference(set_b)
>>> set_d = set_a - set_b
>>> print(set_c)
{1}  # Elemen pada set_a yang tidak terdapat pada set_b
>>> print(set_d)
{1}
```

5. *Symmetric difference* (beda simetris)

```python
>>> set_a = {1, 2}
>>> set_b = {2, 4, 5}
>>> set_c = set_a.symmetric_difference(set_b)
>>> set_d = set_a ^ set_b
>>> print(set_c)
{1, 4, 5}  # Gabungan elemen-elemen set_a yang tidak ada di set_b dan
           # elemen-elemen set_b yang tidak ada pada set_a
>>> print(set_d)
{1, 4, 5}
```

Perhatikan bahwa setiap *method* untuk lima operasi di atas mempunyai tanda
operator biner yang mewakili setiap operasi. Meski begitu, keduanya tidak
persis sama. Jika kalian menggunakan *method*, kalian bisa menggunakan
*iterable* lain sebagai argumennya (tidak harus *set*), misalnya *list*,
*tuple*, *string*, dan sebagainya. Sedangkan jika kalian menggunakan operator
biner (seperti `|`, `&`, `-`, dan `^`), kedua operan harus bertipe data sama
(dalam kasus ini, sama-sama *set*).

<br>

## *Dictionary*

### Definisi *dictionary*

***Dictionary*** merupakan sebuah struktur data untuk menyimpan sepasang data
yang disebut *key* dan *value*. Kita dapat membayangkan *dictionary* sebagai
*list of pairs*, di mana *key* digunakan untuk mengakses suatu value (jika
dibayangkan seperti *list/array*, *key* adalah indeks dan *value* adalah
nilai pada indeks tersebut).

Key yang disimpan pada *dictionary* adalah unik (seperti *set*, hanya saja
terdapat *value* yang ditunjuk oleh *key*), sedangkan *value* tidak harus
bersifat unik dan dapat diisi dengan apapun.

<br>

### Inisialisasi dan akses *dictionary*

Inisialisasi sebuah *dictionary* dapat dilakukan dengan cara berikut.

```python
>>> contacts = {}  # Inisialisasi dictionary kosong
>>> print(contacts)
{}
>>> contacts = {'bill': '353-1234', 'rich': '269-1234', 'jane': '352-1234'}
               # Inisialisasi dictionary langsung dengan isinya
>>> print(contacts)
{'bill': '353-1234', 'rich': '269-1234', 'jane': '352-1234'}
```

<br>

Untuk menambahkan dan mengakses isi dari sebuah *dictionary*, kita bisa
melakukan hal berikut.

```python
>>> contacts = {}
>>> contacts['bill'] = '353-1234'
>>> contacts['rich'] = '269-1234'
>>> contacts['jane'] = '352-1234'
>>> print(contacts)
{'bill': '353-1234', 'rich': '269-1234', 'jane': '352-1234'}
>>> print(contacts['bill'])
'353-1234'
```

```python
>>> name = ['bill', 'rich', 'jane']
>>> number = ['353-1234', '269-1234', '352-1234']
>>> contacts_a = {}
>>>
>>> for i, name in enumerate(name):
...     contacts_a[name] = number[i]
...
>>> print(contacts_a)
{'bill': '353-1234', 'rich': '269-1234', 'jane': '352-1234'}
>>>
>>> new_name = ['ali', 'bill']
>>> new_number = ['239-1234', '277-1234']
>>> contacts_b = dict(zip(new_name, new_number))
>>> print(contacts_b)
{'ali': '239-1234', 'bill': '277-1234'}
>>> contacts_a.update(contacts_b)
{'bill': '277-1234', 'rich': '269-1234', 'jane': '352-1234', 'ali': '239-1234'}
```

<br>

### Fungsi dan operasi pada *dictionary*

Berikut adalah beberapa fungsi dan operasi yang berguna pada *dictionary*.

| Fungsi/operasi    | Keterangan                                              |
| ----------------- | ------------------------------------------------------- |
| `len(dict_a)`     | mengembalikan banyaknya pasangan pada `dict_a`          |
| `k in dict_a`     | memeriksa apakah *key* `k` ada di dalam `dict_a`        |
| `k not in dict_a` | sama dengan `not (k in dict_a)`                         |
| `for k in dict_a` | mengiterasi seluruh elemen `dict_a` secara acak         |
| `dict_a.pop(k)`   | membuang *key* `k` dari `dict_a`, mengembalikan *value* |
| `dict_a.clear()`  | mengosongkan `dict_a`                                   |
| `dict_a.copy()`   | mengembalikan salinan `dict_a`                          |

Contoh lain operasi pada sebuah *dictionary*:

```python
>>> dict_a = {'satu': 1, 'dua': 2, 'empatpuluh': 40, 'haha': {'h', "a"}}
>>> dict_b = dict_a
>>> dict_a["baru nih"] = {'b', 'a', 'r', 'u'}
>>> print(dict_b)
{'satu': 1, 'dua': 2, 'empatpuluh': 40, 'haha': {'h', "a"},
 'baru nih': {'b', 'a', 'r', 'u'}}
>>> print(dict_a)
{'satu': 1, 'dua': 2, 'empatpuluh': 40, 'haha': {'h', "a"},
 'baru nih': {'b', 'a', 'r', 'u'}}
```

Perhatikan bahwa `dict_b = dict_a` berbeda dengan `dict_b = dict_a.copy()`.
Pada `dict_b = dict_a`, `dict_b` menunjuk ke objek *dictionary* yang sama
dengan `dict_a`. Sedangkan pada `dict_b = dict_a.copy()`, `dict_b` menunjuk
ke objek *dictionary* baru yang isinya merupakan salinan dari isi `dict_a`.

Hal ini juga berlaku untuk objek-objek *mutable* lainnya. Untuk memeriksa
apakah dua variabel menunjuk ke objek yang sama, kalian bisa menggunakan fungsi
`id(object)`.

Selain yang ada di atas, ada beberapa method yang berguna untuk mendapatkan
konten dari suatu *dictionary*, seperti pada contoh berikut.

```python
>>> dict_a = {'satu': 1, 'dua': 2, 'empatpuluh': 40, 'haha': {'h', "a"}}
>>> all_items = dict_a.items()
>>> 
>>> for each_tuple in all_items:
...     print("key:", each_tuple[0], "| value:", each_tuple[1])
... 
key: satu | value: 1
key: dua | value: 2
key: empatpuluh | value: 40
key: haha | value: {'h', 'a'}
>>>
>>> all_keys = dict_a.keys()
>>> print(all_keys)
dict_keys(['satu', 'dua', 'empatpuluh', 'haha'])
>>> all_keys = list(all_keys)
>>> print(all_keys)
['satu', 'dua', 'empatpuluh', 'haha']
>>>
>>> all_values = dict_a.values()
>>> print(all_values)
dict_values([1, 2, 40, {'a', 'h'}])
>>> all_values = list(all_values)
>>> print(all_values)
[1, 2, 40, {'a', 'h'}]
```

<br>

Untuk lebih lanjut mengenai *set* dan *dictionary*, silakan buka dokumentasi
Python untuk [*set*][set] dan [*dictionary*][dictionary].

<br>

---

Diadaptasi dari:

- `Soal Tutorial Lab 7 - Kelas C.pdf` buatan
  **FDL**, **IF**, **PDD**, dan **SAT**
- `ddp1-17gasal-09.pdf` buatan **Adila Alfa Krisnadhi, Ph.D.**

dengan beberapa perubahan.

[set]: https://docs.python.org/3/library/stdtypes.html#set

[dictionary]: https://docs.python.org/3/library/stdtypes.html#dict
