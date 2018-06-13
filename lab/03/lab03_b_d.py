'''
Program dekripsi pesan dengan Caesar cipher
https://en.wikipedia.org/wiki/Caesar_cipher

Program menerima input berupa kunci cipher dan pesan yang sudah dienkripsi,
dipisahkan dengan tanda spasi. Pesan yang dienkripsi hanya dapat terdiri atas
huruf kecil dan spasi.
'''

# Meminta input "mentah"
rawinput = input("Masukkan operasi: ")

# Memecah input menjadi 2, untuk kunci cipher dan pesan yang masih terenkripsi
key = int(rawinput.split(" ", 1)[0])
encrypted = rawinput.split(" ", 1)[1]

# Inisialisasi pesan yang sudah didekripsi dengan string kosong
decrypted = ""

for char in encrypted:
    # Jika spasi, tetap tulis
    if char == " ":
        decrypted += char
    # Jika huruf setelah digeser ke kiri dengan key ternyata lewat dari "a"
    elif ord(char) - key < ord("a"):
        # Ambil orde huruf yang sedang dicek, kemudian modulo dengan orde "a"
        # untuk mendapatkan indeks huruf dalam susunan alfabet (mulai dari 0).
        # Kurangi dengan key, kemudian modulo dengan orde "z" sehingga didapat
        # orde "z" dikurangi indeks huruf. Kemudian, tambahkan + 1 karena
        # indeks huruf tadi dimulai dari 0.
        decrypted += chr((ord(char) % ord("a") - key) % ord("z") + 1)
    # Jika orde dikurangi key tidak kurang dari orde "a" (normal)
    else:
        decrypted += chr(ord(char) - key)

# Print hasil
print("Kalimat aslinya adalah:", decrypted)
