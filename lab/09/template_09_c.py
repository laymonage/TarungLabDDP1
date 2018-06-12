class Pegawai():
    def __init__(self,nama,rate_gaji):
        # ganti None dan assign nilai dari objek Pegawai
        self.nama = None
        self.rate_gaji = None
        self.jam_kerja = 0

    def __str__(self,divisi):
        return # return sebuah pesan sesuai format

    def tambah_jam_kerja(self,jam_kerja):
        # tambah jam_kerja nya pegawai dengan jam_kerja dari parameter
        pass

    def gajian(self):
        #hitung gaji, lalu print sesuai format
        pass


class Staff(object):
    def __init__(self,nama):
        # panggil __init__ dari class Pegawai untuk inisiasi nilai awal
        # masukkan nilai yang dibutuhkan sesuai fungsi di parent class
        pass

    def __str__(self):
        # panggil fungsi __str__ di parent class, sesuaikan parameter nya
        pass

    def kerja(self, jam_kerja):
        # panggil fungsi tambah_jam_kerja milik parent class untuk menambah jam kerja pegawai
        # lalu cetak sesuai format
        pass

# BUAT CLASS UNTUK DUA DIVISI LAINNYA

def main():

    # Buat sebuah dictionary
    # ini berguna untuk mendapatkan Objek Pegawai dengan nama yang spesifik
    daftar_pegawai = None

    while True:
        masukan = input()

        if(masukan == "GAJIAN"):
            # akses semua pegawai satu per satu,
            # lalu panggil fungsi untuk melakukan gajian
            break

        masukan_split = masukan.split(";")


        if(masukan_split[0] == "REKRUT"):
            # dapatkan nilai ini dari masukan_split sesuai indexnya (lihat format input)
            nama = None
            divisi = None

            # lakukan selection untuk menentukan tipe Pegawai
            if(divisi == "Staff"):
                pegawai = Staff(nama) #instansiasi objek
            elif(divisi == "Filmmaker"):
                pegawai = None
            elif(divisi == "Promoter"):
                pegawai = None

            # masukan pegawai yang sudah dibuat ke dalam dictionary
            # cetak pesan sesuai format

        elif(masukan_split[0] == "INFO"):
            nama = None
            pegawai = None #dapatkan objek pegawai berdasarkan namanya
            print(pegawai)

        else:
            # Jika masuk ke bagian ini, artinya input berupa NGANTOR,PRODUKSI, atau PROMOSI


            # dapatkan atribut dan objek yang diperlukan
            nama = None
            jam_kerja = None # jam_kerja dalam int
            pegawai = None # objek pegawai

            # lakukan selection menentukan perintah tipe apa
            if(masukan_split[0] == "NGANTOR"): # STAFF
                # ganti True dengan suatu pengecekan apakah pegawai merupakan instance dari Staff
                if(True):
                    # jika benar, maka pegawai tersebut bekerja
                    pass
                else:
                    #jika bukan, maka berikan pesan error sesuai format
                    pass

            # lakukan hal sama untuk FILMMAKER
            elif(masukan_split[0] == "PRODUKSI"): # FILMMAKER
                pass

            # lakukan hal sama untuk PROMOTER

if __name__ == "__main__":
    main()