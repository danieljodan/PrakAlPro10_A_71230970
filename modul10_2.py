# Program untuk memetakan dua list menjadi satu dictionary
def satudict(Lista, Listb):
    dictionary = {}
    for i in range(len(Lista)):
        dictionary[Lista[i]] = Listb[i]
    print(dictionary)

Lista = ['red', 'green', 'blue']
Listb = ['#FF0000','#008000', '#0000FF']
satudict(Lista, Listb)

