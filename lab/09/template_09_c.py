'''
Template untuk solusi Lab 09 kelas C.
'''

class Pegawai():
    '''
    Seorang pegawai.
    '''

    def __init__(self, nama, rate_gaji):
        # Ganti None dan assign nilai dari objek Pegawai
        self.nama = nama
        self.rate_gaji = rate_gaji
        self.jam_kerja = 0

    def __str__(self, divisi=None):
        return  # Return sebuah pesan sesuai format

    def tambah_jam_kerja(self, jam_kerja):
        '''
        Tambah jam_kerja nya pegawai dengan jam_kerja dari parameter.
        '''
        pass

    def gajian(self):
        '''
        Hitung gaji, lalu print sesuai format.
        '''
        pass


class Staff(object):
    '''
    Seorang staf.
    '''

    def __init__(self, nama):
        # Panggil __init__ dari class Pegawai untuk inisiasi nilai awal
        # Masukkan nilai yang dibutuhkan sesuai fungsi di parent class
        pass

    def __str__(self):
        # Panggil fungsi __str__ di parent class, sesuaikan parameter nya
        pass

    def kerja(self, jam_kerja):
        '''
        Panggil fungsi tambah_jam_kerja milik parent class untuk menambah
        jam kerja pegawai, lalu cetak sesuai format
        '''
        pass

# BUAT CLASS UNTUK DUA DIVISI LAINNYA

def main():
    '''
    Program utama.
    '''

    # Buat sebuah dictionary
    # Ini berguna untuk mendapatkan Objek Pegawai dengan nama yang spesifik
    # daftar_pegawai = {}

    while True:
        masukan = input()

        if masukan == "GAJIAN":
            # Akses semua pegawai satu per satu,
            # Lalu panggil fungsi untuk melakukan gajian
            break

        masukan_split = masukan.split(";")


        if masukan_split[0] == "REKRUT":
            # Dapatkan nilai ini dari masukan_split sesuai indexnya
            # (lihat format input)
            nama = None
            divisi = None

            # Lakukan selection untuk menentukan tipe Pegawai
            if divisi == "Staff":
                pegawai = Staff(nama)  # Instansiasi objek
            elif divisi == "Filmmaker":
                pegawai = None
            elif divisi == "Promoter":
                pegawai = None

            # Masukan pegawai yang sudah dibuat ke dalam dictionary
            # Cetak pesan sesuai format

        elif masukan_split[0] == "INFO":
            nama = None
            pegawai = None  # Dapatkan objek pegawai berdasarkan namanya
            print(pegawai)

        else:
            # Jika masuk ke bagian ini, artinya input berupa
            # NGANTOR,PRODUKSI, atau PROMOSI


            # Dapatkan atribut dan objek yang diperlukan
            # nama = None
            # jam_kerja = None # jam_kerja dalam int
            # pegawai = None # objek pegawai

            # Lakukan selection menentukan perintah tipe apa
            if masukan_split[0] == "NGANTOR": # STAFF
                pass
                # Ganti True dengan suatu pengecekan apakah
                # pegawai merupakan instance dari Staff
                # if True:
                    # Jika benar, maka pegawai tersebut bekerja
                # else:
                    # Jika bukan, maka berikan pesan error sesuai format

            # Lakukan hal sama untuk FILMMAKER
            elif masukan_split[0] == "PRODUKSI":  # FILMMAKER
                pass

            # Lakukan hal sama untuk PROMOTER

if __name__ == "__main__":
    main()
