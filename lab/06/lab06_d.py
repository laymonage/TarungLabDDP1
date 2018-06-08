'''
Benny's Plagiarism Filter
Mengecek set-set yang berisi 64-bit hashcode dari file-file submisi tugas
pemrograman dan mencetak output berupa set yang berisi hashcode yang tidak
memiliki duplikat.
'''

set_qty = int(input("Masukkan banyaknya set yang akan diinput: "))
curr_set = set()

print("Untuk {} baris berikutnya, masukkan set yang berisi ".format(set_qty) +
      "hashcode yang akan dicek:")

'''
Meminta input berupa set sebanyak set_qty yang telah diinput oleh user.
Untuk setiap set yang diinput, hilangkan spasi untuk menyeragamkan set sehingga
setiap elemen hanya dipisahkan dengan ",". Hilangkan { dan } yang ada di awal
dan akhir input, kemudian buat menjadi set baru a_set dengan setiap elemennya
dipisahkan oleh ", ". Simpan elemen-elemen yang ada di a_set ke dalam
curr_set, dan simpan irisan curr_set dengan a_set berikutnya di intersections.
Setelah semua set masuk ke curr_set, hilangkan elemen-elemen yang ada di
intersections dari curr_set.
'''

intersections = set()
for i in range(set_qty):
    a_set = input().replace(' ', '').strip('{}')
    a_set = set(a_set.split(','))
    if i > 0:
        intersections |= curr_set & a_set
    curr_set |= a_set
curr_set -= intersections

'''
Menghilangkan string kosong yang mungkin ada di curr_set jika ada tepat satu
set yang diinput yang hanya memiliki tepat satu elemen (tidak ada ", ").
Kemudian menghilangkan tanda ' karena elemen-elemen curr_set masih bertipe
string.
'''
curr_set.discard('')
print(str(curr_set).replace("'", ""))
