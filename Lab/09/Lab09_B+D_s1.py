'''
Kompresi Benny

Menyederhanakan sebuah kata dengan membuat beberapa
karakter yang sama dan berurutan hanya akan menjadi
satu karakter saja.
'''


def kompresi(a_str):
    '''
    Mengompres a_str sehingga tidak ada
    karakter yang sama yang bersebelahan.

    Contoh: kompresi('aabbbbaaacddeae')
            akan mengembalikan 'abacdeae'
    '''

    if len(a_str) <= 1:
        return a_str

    '''
    Apabila karakter pertama dan kedua adalah sama,
    maka langsung panggil kompresi tanpa karakter
    pertama.
    '''
    if a_str[0] == a_str[1]:
        return kompresi(a_str[1:])

    return a_str[0] + kompresi(a_str[1:])


if __name__ == '__main__':
    while True:
        the_str = input(">>> ")
        print("Hasil kompresinya adalah {}".format(kompresi(the_str)))
