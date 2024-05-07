# Program Menghitung Banyak Pesan Yang Masuk Dari Email dan Disajikan Dalam Dictionary
def tampilkan(namaFile):
    with open(namaFile, 'r') as f:
        pesan = f.readlines()
        d = {}
        for line in pesan:
            line = line.strip()
            words = line.split()
            if 'Author:' in words:
                for word in words:
                    if '@' in word:
                        if word not in d:
                            d[word] = 1
                        else:
                            d[word] += 1
        print(d)
    
namaFile = input("Masukkan nama file: ")
tampilkan(namaFile)


