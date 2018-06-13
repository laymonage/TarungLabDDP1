'''
Program pengelola panitia Parfest X
'''


class Staff:
    '''
    Staf secara umum
    '''
    def __init__(self, nama):
        self.nama = nama
        self.jam_kerja = 0
        self.progress = 0

    def kerja(self, jam):
        '''
        Menambahkan jam kerja seorang staf.
        '''
        self.jam_kerja += jam

    def hitung_gaji(self):
        '''
        Menghitung gaji seorang staf.
        Penghitungan gaji didefinisikan lebih lanjut di class
        masing-masing divisi panitia.
        '''
        pass


class StaffAcara(Staff):
    '''
    Staf acara
    '''
    def __init__(self, nama):
        Staff.__init__(self, nama)

    def persentase(self):
        '''
        Mengembalikan persentase jam kerja dari seorang staf Acara.
        Persentase jam kerja staf acara = 4%/jam kerja
        '''
        return 4 * self.jam_kerja

    def hitung_gaji(self):
        '''
        Mengembalikan gaji sementara dari seorang staf Acara.
        Gaji staf Acara = persentase x 2000 BenCoin
        '''
        return self.persentase() * 2000


class StaffPartnership(Staff):
    '''
    Staf Partnership
    '''
    def __init__(self, nama):
        Staff.__init__(self, nama)

    def persentase(self):
        '''
        Mengembalikan persentase jam kerja dari seorang staf Partnership.
        Persentase jam kerja staf Partnership = 1%/jam kerja
        '''
        return self.jam_kerja

    def hitung_gaji(self):
        '''
        Mengembalikan gaji sementara dari seorang staf Partnership.
        Gaji staf Partnership = jam kerja x persentase x 4000 BenCoin
        '''
        return self.jam_kerja * self.persentase() * 4000


class StaffPublikasi(Staff):
    '''
    Staf publikasi
    '''
    def __init__(self, nama):
        Staff.__init__(self, nama)

    def persentase(self):
        '''
        Mengembalikan persentase jam kerja dari seorang staf Publikasi.
        Persentase jam kerja staf Publikasi = 20%/jam kerja
        '''
        return 20 * self.jam_kerja

    def hitung_gaji(self):
        '''
        Mengembalikan gaji sementara dari seorang staf Publikasi.
        Gaji staf publikasi = jam kerja * 1500 BenCoin
        '''
        return self.jam_kerja * 1500


class Manager:
    '''
    Manajer staf Parfest X
    '''
    def __init__(self):
        self.staffs = {}

    def recruit_staff(self, staf):
        '''
        Merekrut staf baru dan menyimpannya dalam dict staffs.
        '''
        self.staffs[staf.nama] = staf

    def get_staff(self, nama):
        '''
        Mengembalikan objek seorang staf
        '''
        return self.staffs[nama]

    def is_staff_recruited(self, nama):
        '''
        Mengecek apakah staf sudah direkrut sebelumnya.
        '''
        return nama in self.staffs


manajer = Manager()
while True:
    perintah = input("Masukkan perintah yang ingin dilakukan:\n").split(';')
    if perintah[0] == 'EXIT':
        break

    nama_staf = perintah[1]
    if perintah[0] == 'REKRUT':
        if manajer.is_staff_recruited(nama_staf):
            print("{} sudah direkrut sebelumnya\n".format(nama_staf))
        else:
            # Membuat instance sesuai dengan bidang staf
            if perintah[2] == 'ACARA':
                new_recruit = StaffAcara(nama_staf)
            elif perintah[2] == 'PARTNERSHIP':
                new_recruit = StaffPartnership(nama_staf)
            elif perintah[2] == 'PUBLIKASI':
                new_recruit = StaffPublikasi(nama_staf)
            else:
                print("Bidang staff tidak tersedia.\n")
                continue

            # Menyimpan instance dalam dictionary melalui method recruit_staff
            manajer.recruit_staff(new_recruit)
            print("{} direkrut\n".format(new_recruit.nama))

    if perintah[0] == 'KERJA':
        the_staff = manajer.staffs[nama_staf]
        lama = int(perintah[2])
        if the_staff.persentase() >= 100:
            print(("{} sudah mencapai {}% progress\n"
                   .format(the_staff.nama, int(the_staff.persentase()))))
        else:
            # Menambahkan jam kerja seorang staf
            the_staff.kerja(lama)
            print("{} bekerja selama {} jam\n".format(the_staff.nama, lama))

    if perintah[0] == 'LOG':
        # Mencetak log seorang staf
        the_staff = manajer.staffs[nama_staf]
        log = (">> {}\n"
               "Telah bekerja selama: {} jam\n"
               "Progress: {} persen\n"
               "Gaji sementara: {} BenCoin\n"
               .format(the_staff.nama,
                       the_staff.jam_kerja,
                       int(the_staff.persentase()),
                       the_staff.hitung_gaji()))
        print(log)
