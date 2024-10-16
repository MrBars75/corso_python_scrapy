# creazione di una lista e popolamento

list1 = []
for i in range(10):
    list1.append(i*2)
print(list1)

# la stessa lista con list comprehension

list2 = [i*2 for i in range(10)]
print(list2)


# in generale: nuova_lista = [espressione for membro in iterabile]

# espressione: può essere anche una funzione. Esempio:

def fatt(n):
    if(n == 0) or (n == 1):
        return 1
    else:
        return n*fatt(n-1)

list2 = [fatt(i) for i in range(10)]
print(list2)

# possiamo aggiungere anche dei filtri if al risultato. Esempio:

list3 = [i for i in range(10) if i%2==0]
print(list3)

# altra tecnica di filtraggio, questa volta con un if else. Esempio:

l1 = [1,2,3,4,5,6,7,8,9]
l2 = [0 if i < 5 else i for i in l1]
print(l2)
