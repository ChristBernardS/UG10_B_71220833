print("~"*10, "/('v')", "~"*10)
print("PROGRAM PENGHITUNG VOLUME BANGUN RUANG")
print("~"*10, "\('v')/", "~"*10)
print('')
print('Pilihlah salah satu bangun ruang yang ingin dihitung volumenya:')
print('1. Limas\n2. Bola\n3. Prisma\n4. Kerucut\n')
pilihan = int(input('Masukkan pilihan anda: '))
if pilihan == 1:
    panjang = int(input('Masukkan panjang sisi alas limas: '))
    tinggi = int(input('Masukkan tinggi limas: '))
    volumelimas = (1/3)*tinggi*(panjang**2)
    print('Volume limas tersebut adalah ', volumelimas)
elif pilihan == 2:
    jari_jari = int(input('Masukkan panjang jari-jari bola: '))
    volumebola = (4/3)*3.14*(jari_jari**3)
    print('Volume bola tersebut adalah ', volumebola)
elif pilihan == 3:
    print('Pilihlah salah satu dari pilihan di bawah')
    print('1. Prisma Segitiga\n2. Prisma Segiempat\n3. Prisma Segilima')
    pilihan2 = int(input('Tentukan pilihan Anda: '))
    if pilihan2 == 1:
        sisialasprisma = int(input('Masukkan panjang sisi alas prisma: '))
        tinggialasprisma = int(input('Masukkan tinggi alas prisma: '))
        tinggiprismasegitiga = int(input('Masukkan tinggi prisma segitiga: '))
        volumeprisma = (1/2)*sisialasprisma * \
            tinggialasprisma*tinggiprismasegitiga
        print('Volume prisma segitiga tersebut adalah ', volumeprisma)
    elif pilihan2 == 2:
        sisialasprisma = int(input('Masukkan panjang sisi alas prisma: '))
        tinggialasprisma = int(input('Masukkan tinggi alas prisma: '))
        tinggiprismasegitiga = int(input('Masukkan tinggi prisma segitiga: '))
        volumeprisma = sisialasprisma*tinggialasprisma * tinggiprismasegitiga
        print('Volume prisma segitiga tersebut adalah ', volumeprisma)
    elif pilihan2 == 3:
        sisialasprisma = int(input('Masukkan panjang sisi alas prisma: '))
        tinggialasprisma = int(input('Masukkan tinggi alas prisma: '))
        tinggiprismasegitiga = int(input('Masukkan tinggi prisma segitiga: '))
        volumeprisma = 2.5*sisialasprisma * tinggialasprisma*tinggiprismasegitiga
        print('Volume prisma segitiga tersebut adalah ', volumeprisma)
    else:
        print('Prisma yang Anda cari belum tersedia di Kalkulator ini')
elif pilihan == 4:
    jarikerucut = int(input('Masukkan jari-jari kerucut: '))
    tinggikerucut = int(input('Masukkan tinggi kerucut: '))
    volumekerucut = round((1/3)*3.14*(jarikerucut**2)*tinggikerucut, ndigits=1)
    print('Volume kerucut tersebut adalah ', volumekerucut)
else:
    print('nomor tidak terdaftar dalam menu pilihan\nUlangi program dan pilih nomor 1 sampai 4')
