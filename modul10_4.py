# Program Pencatat Nama Domain Pengirim Pesan
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
                        domain = word.split('@')[-1]
                        if domain not in d:
                            d[domain] = 1
                        else:
                            d[domain] += 1
        print(d)
    
namaFile = input("Masukkan nama file: ")
tampilkan(namaFile)