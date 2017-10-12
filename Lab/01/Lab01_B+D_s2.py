# Program prediksi waktu pemenuhan biaya pernikahan

# Input berupa biaya pernikahan (dalam rupiah)

# Keluaran berupa hasil prediksi waktu pemenuhan
# biaya pernikahan dalam format:
#   Anda harus bekerja selama x tahun, y bulan, z minggu,
#   a hari untuk memenuhi biaya pernikahan.

# Asumsi:
# 1 tahun  = 12 bulan
# 1 bulan  =  4 minggu
# 1 minggu =  7 hari


# Menerima masukan berupa biaya pernikahan
biaya = int(input("Masukkan biaya pernikahan: Rp "))
gaji  = 500000

# Mendapatkan waktu pemenuhan biaya dalam hari
hari  = biaya // 500000

# Menghitung jumlah hari dalam tahun
tahun  = hari // (12 * 4 * 7)

# Menghitung jumlah hari dalam bulan
# dengan sisa hari apabila waktu >= 1 tahun
# hari  -= (tahun * 12 * 4 * 7) # tanpa modulo
hari   = hari % (12 * 4 * 7)
bulan  = hari // (4 * 7)

# Menghitung jumlah hari dalam minggu
# dengan sisa hari apabila waktu >= 1 bulan
# hari  -= (bulan * 4 * 7)      # tanpa modulo
hari   = hari % (4 * 7)
minggu = hari // 7

# Menghitung sisa hari bila waktu >= 1 minggu
# hari  -= (minggu * 7)         # tanpa modulo
hari   = hari % 7

# Mencetak keluaran
print("Anda harus bekerja selama", tahun, "tahun", bulan, "bulan",
      minggu, "minggu", hari, "hari untuk memenuhi biaya pernikahan.")
