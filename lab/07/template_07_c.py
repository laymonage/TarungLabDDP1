'''
Template untuk solusi Lab 07 kelas C.
'''

def main():
    '''
    Main program.
    '''
    # matkul = {} # Buat sebuah dictionary

    while True:
        masukan = input(">>> ")

        ######

        # Buat agar program berhenti saat masukan adalah "selesai"

        ######

        masukan_split = masukan.split(" ")

        if masukan_split[0] == "tambah":
            # nama_matkul = masukan_split[1]
            # npm_semua = masukan_split[2:]

            # Buat sebuah set untuk menampung NPM-NPM diatas
            # Masukan ke dictionary yang telah dibuat diatas

            print(masukan_split[1], "berhasil ditambahkan!")

        # Gunakan method yang dimiliki set
        # untuk melakukan 3 operasi di bawah ini
        elif masukan_split[0] == "gabungan":
            pass

        elif masukan_split[0] == "pengambil":
            pass

        elif masukan_split[0] == "hanya":
            pass

        # ------------------------------------------------------------
        elif masukan_split[0] == "cetak":
            pass

            # Lakukan selection, apakah cetak sebuah matkul, atau semuanya
            # dan lakukan operasi print sesuai format

        else:
            print("Perintah salah!")

main()
