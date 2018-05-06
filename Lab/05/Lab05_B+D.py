'''
Program Mini-Kuis DDP1
Program untuk mengerjakan kuis yang berisi 4 buah pertanyaan yang meminta
user untuk mengkonversi bilangan biner ke bilangan desimal.
'''


def cetak_pertanyaan(urutan, angka_biner):
    '''
    Mencetak pertanyaan
    '''
    print("Soal {}: Berapakah angka desimal dari bilangan biner {}?"
          .format(urutan, angka_biner))


def cek_jawaban(jawaban, angka_biner):
    '''
    Mengecek kebenaran jawaban
    '''
    return jawaban == int(angka_biner, 2)


def main():
    '''
    Program utama
    '''
    print("Selamat datang di Mini Kuis DDP-1: Sistem Bilangan!")
    # Menyimpan soal
    soal1 = "11111100001"
    soal2 = "11111001111"
    soal3 = "10001100"
    soal4 = "100011101"
    counter_soal = 1
    skor = 0
    while counter_soal <= 4:
        # Menyesuaikan counter_soal dengan soal yang digunakan
        if counter_soal == 1:
            angka_biner = soal1
        elif counter_soal == 2:
            angka_biner = soal2
        elif counter_soal == 3:
            angka_biner = soal3
        else:
            angka_biner = soal4

        # Mencetak pertanyaan sesuai dengan counter soal
        # dan angka biner untuk counter tersebut
        cetak_pertanyaan(counter_soal, angka_biner)

        # Meminta input jawaban, format output: “Jawab: <input_di_sini>”
        jawaban = int(input("Jawab: "))

        # Mengecek apakah jawabannya benar
        if cek_jawaban(jawaban, angka_biner):
            skor += 25

        # Menambahkan counter soal
        counter_soal += 1

    # Mencetak skor akhir, format output: “Skor akhir: <skor>""
    print("Skor akhir: {}".format(skor))


def main_bonus():
    '''
    Program bonus
    '''
    print("\nSelamat datang di Mini Kuis DDP-1: Sistem Bilangan!")
    # Meminta input soal
    list_soal = input("Masukkan 4 soal: ").split()
    skor = 0

    for i in range(len(list_soal)):
        cetak_pertanyaan(i + 1, list_soal[i])
        jawaban = int(input("Jawab: "))
        if cek_jawaban(jawaban, list_soal[i]):
            skor += 25

    print("Skor akhir: {}".format(skor))


if __name__ == '__main__':
    main()
    main_bonus()
