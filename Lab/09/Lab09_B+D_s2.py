'''
Angka Cantik Versi Benny

Mengembalikan angka cantik versi Benny
dari sebuah bilangan bulat positif.

Definisi angka cantik versi Benny adalah:
    - Apabila x hanya terdiri dari satu digit,
      bilangan cantiknya adalah x.
    - Apabila tidak, bilangan cantik dari x adalah
      bilangan cantik dari penjumlahan digit-digitnya.
'''


def cantik(a_int):
    '''
    Mengambil angka cantik versi Benny dari a_int.
    Contoh:
    cantik(12345) = cantik(1+2+3+4+5)
                  = cantik(15)
                  = cantik(1+5)
                  = cantik(6)
                  = 6
    '''

    if a_int // 10 == 0:
        return a_int

    x = 0
    for num in str(a_int):
        x += int(num)

    return cantik(x)


if __name__ == '__main__':
    while True:
        the_int = int(input(">>> "))
        print(cantik(the_int))
