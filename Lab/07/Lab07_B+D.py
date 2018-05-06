'''
BenJek Program
Mengelola pangkalan data akun driver BenJek.
'''

drivers = {}
BenJek_income = 0


class BenJekDriver(object):
    '''
    Kelas yang merupakan driver BenJek.
    '''
    def __init__(self, driver_name, service_type):
        '''
        Membuat sebuah instance dari BenJekDriver.
        '''
        self.name = driver_name
        self.service = service_type
        self.salary = 0
        self.fare = 0

    def go(self, distance):
        '''
        Melakukan perjalanan untuk seorang driver
        dengan jarak sejauh <distance> dan
        menambahkan pendapatan driver sesuai
        jenis layanannya.
        '''
        if distance <= 0:
            return "Jarak perjalanan tidak boleh <= 0"

        if self.name not in drivers.keys():
            return ("{} tidak ada di dalam sistem"
                    .format(self.name))

        if self.service == 'NORMAL':
            self.fare = distance*1000*(80/100)

        if self.service == 'SPORT':
            if distance < 10:
                return ("{} tidak bisa melakukan perjalanan"
                        .format(self.name))
            self.fare = distance*2500*(80/100)

        if self.service == 'CRUISER':
            if distance < 25:
                return ("{} tidak bisa melakukan perjalanan"
                        .format(self.name))
            self.fare = distance*7500*(80/100)

        self.salary += self.fare

        return ("{} melakukan perjalanan sejauh {:.2f} "
                "dan mendapatkan pendapatan sebesar {:.2f}"
                .format(self.name, distance, self.fare))

    def check(self):
        '''
        Mengembalikan pendapatan dari seorang driver
        sejauh ini.
        '''
        if self.name in drivers.keys():
            return ("{} memiliki pendapatan sebesar Rp.{:.2f}"
                    .format(self.name, self.salary))

        return ("{} tidak ada di dalam sistem"
                .format(self.name))


def register(driver_name, service_type):
    '''
    Mendaftarkan driver baru pada dict drivers.
    '''
    service_type = service.upper()
    if driver_name in drivers.keys():
        return ("{} gagal mendaftar sebagai driver BenJek"
                .format(driver_name))
    if service_type not in ['NORMAL', 'SPORT', 'CRUISER']:
        return ("Tipe driver {} tidak tersedia"
                .format(service_type))
    drivers[driver_name] = BenJekDriver(driver_name, service_type)
    return ("{} berhasil mendaftar sebagai driver BenJek {}"
            .format(driver_name, service_type))


def endmonth():
    '''
    Mengakhiri bulan dan mencetak pendapatan secara keseluruhan.
    '''
    if not drivers:
        summary = "Belum ada driver yang terdaftar!"
        return summary

    summary = ("Sudah akhir bulan! "
               "Pendapatan BenJek bulan ini adalah Rp.{:.2f}\n"
               "Daftar pendapatan pengemudi:\n"
               .format(BenJek_income))
    for each_driver in drivers:
        summary += ("{}: Rp.{:.2f}\n"
                    .format(each_driver, drivers[each_driver].salary))
    return summary


print(("Selamat datang di program pengelola pangkalan data BenJek.\n"
       "Berikut adalah perintah yang bisa Anda jalankan:\n"
       "DAFTAR <nama_driver> <NORMAL/SPORT>\n"
       "MULAI PERJALANAN <nama_driver> <jarak_ditempuh_km>\n"
       "CEK PENDAPATAN <nama_driver>"
       "AKHIR BULAN\n"
       "Masukkan perintah yang ingin Anda jalankan:"))

while True:
    command = input("\n")
    coms = command.split()
    try:
        if coms[0].upper() == "DAFTAR":
            name = coms[1]
            service = coms[2].upper()
            print(register(name, service))

        if coms[0].upper() + ' ' + coms[1].upper() == "MULAI PERJALANAN":
            name = coms[2]
            print(drivers[name].go(float(coms[3])))
            BenJek_income += drivers[name].fare / 4

        if coms[0].upper() + ' ' + coms[1].upper() == "CEK PENDAPATAN":
            name = coms[2]
            print(drivers[name].check())

        if coms[0].upper() + ' ' + coms[1].upper() == "AKHIR BULAN":
            print(endmonth())
            break

    except IndexError:
        print("Perintah salah.")

input("Tekan <enter> untuk keluar dari program...")
