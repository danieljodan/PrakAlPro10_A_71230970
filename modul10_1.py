# Program untuk mendapatkan nilai key, value, dan item dari sebuah dictionary
def tampilkan(d):
    print("key\t" "value\t" "item")
    counter = 0
    for i in d:
        counter += 1
        print(i, end = "\t")
        print(d[i], end = "\t")
        print(counter, end = "\n")    
    
dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
tampilkan(dictionary)

