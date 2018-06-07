
class Bangunan:
    def __init__(self, nama, lama_sewa, harga_sewa):
        self.nama = nama
        self.lama_sewa = lama_sewa
        self.harga_sewa = harga_sewa

    def getHargaSewa(self):
        return self.harga_sewa

class Restoran(Object):
    def __init__(self, nama, lama_sewa):
        Bangunan.__init__(self, nama, lama_sewa, 30000000)

# Silahkan ditambahkan class-class lainnya atau jika ingin memodifikasi


daftar_bangunan = None

while True:
    masukan = input().split()

    if(masukan[0] == "BANGUN"):
		# dapatkan nilai ini dari masukan_split sesuai indexnya (lihat format input)
		nama = None
		jenis_bangunan = None

		# lakukan selection untuk menentukan tipe Pegawai
		if(jenis_bangunan == "HOTEL"):
			bangunan = Hotel(nama) #instansiasi objek
		elif(jenis_bangunan == "RESTORAN"):
			bangunan = None
		elif(jenis_bangunan == "RUMAHSAKIT"):
			bangunan = None

		# masukan bangunan yang sudah dibuat ke dalam dictionary
		# cetak pesan sesuai format

	elif(masukan[0] == "INFO"):

	elif(masukan[0] == "JUALMAKANAN"):

	elif(masukan[0] == "TERIMATAMU")

	elif(masukan[0] == "OBATIPASIEN"):

	elif(masukan[0] == "HITUNGUANG"):
