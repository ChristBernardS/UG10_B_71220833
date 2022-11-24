print(
    '~~ Selamat Datang di Program Pengurutan Bilangan ~~\nTentukan Pilihan Anda!!! [1/2]\n\n1. Ascending\n2. Descending\n')
Pilihan = int(input('Masukkan Pilihan yang Anda Inginkan: '))
if Pilihan == 1:
    angka1 = int(input('Masukkan bilangan pertama : '))
    angka2 = int(input('Masukkan bilangan kedua : '))
    angka3 = int(input('Masukkan bilangan ketiga : '))
    angka4 = int(input('Masukkan bilangan keempat : '))
    ascending = [angka1, angka2, angka3, angka4]
    print(sorted(ascending))
elif Pilihan == 2:
    angka1 = int(input('Masukkan bilangan pertama : '))
    angka2 = int(input('Masukkan bilangan kedua : '))
    angka3 = int(input('Masukkan bilangan ketiga : '))
    angka4 = int(input('Masukkan bilangan keempat : '))
    descending = [angka1, angka2, angka3, angka4]
    print(sorted(descending))
else:
    print('Menu tidak terdaftar dalam pilihan')
