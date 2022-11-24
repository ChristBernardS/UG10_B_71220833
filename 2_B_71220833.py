print('='*10, 'PROGRAM PENGHITUNG PYTHAGORAS', '='*10)
angka1 = int(input('Masukkan bilangan bulat pertama: '))
angka2 = int(input('Masukkan bilangan bulat kedua: '))
angka3 = int(input('Masukkan bilangan bulat ketiga: '))
if (angka1**2)+(angka2**2) == (angka3**2):
    print('Merupakan Pythagoras')
elif (angka2**2)+(angka3**2) == (angka1**2):
    print('Merupakan Pythagoras')
elif (angka1**2)+(angka3**2) == (angka2**2):
    print('Merupakan Pythagoras')
else:
    print('Bukan Merupakan Pythagoras')
