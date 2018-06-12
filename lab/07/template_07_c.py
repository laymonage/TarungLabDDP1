def main():
    matkul = #buat sebuah dictionary

    while #buat agar meminta input terus :
        masukkan = input(">>> ")

        ######
        
        #buat agar program berhenti saat masukkan adalah "selesai"

        ######

        masukkan_split = masukkan.split(" ")

        if (masukkan_split[0] == "tambah"):
            nama_matkul = masukkan_split[1]
            npm_semua = masukkan_split[2:]

            # buat sebuah set untuk menampung NPM-NPM diatas
            # masukkan ke dictionary yang telah dibuat diatas

            print(masukkan_split[1],"Berhasil Ditambahkan !")

        # Gunakan method yang dimiliki set untuk melakukan 3 operasi di bawah ini
        elif (masukkan_split[0] == "gabungan"):


        elif (masukkan_split[0] == "pengambil"):


        elif(masukkan_split[0] == "hanya"):


        # ------------------------------------------------------------
        elif (masukkan_split[0] == "cetak"):

            # Lakukan selection, apakah cetak sebuah matkul, atau semuanya
            # dan lakukan operasi print sesuai format
            

        else:
            print("Perintah salah !")


main()
