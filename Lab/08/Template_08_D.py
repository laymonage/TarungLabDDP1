'''
class Staff:
    def __init__(self, nama):
        self.nama = nama
        self.jam_kerja = 0
        self.progress = 0

    def kerja(self, jam):
        self.jam_kerja += jam

    def hitung_gaji(self):
        pass


class StaffAcara(Staff):
    # TODO : Implementasikan inheritance terhadap kelas ini
    def __init__(self,nama):
        super().__init__(nama)

class StaffPartnership(Staff):
    # TODO : Implementasikan inheritance terhadap kelas ini
    def __init__(self,nama):
        super().__init__(nama)

class StaffPublikasi(Staff):
    # TODO : Implementasikan inheritance terhadap kelas ini
    def __init__(self,nama):
        super().__init__(nama)

class Manager:
    def __init__(self):
        self.staffs = {}

    def recruit_staff(self, staf):
        self.staffs[staf.nama] = staf

    def get_staff(self,nama):
        return self.staffs[nama]

    def is_staff_recruited(self, nama):
        return nama in self.staffs

# Tuliskan kode anda untuk alur program dibawah
# Selamat mengerjakan. Semangat!
'''
