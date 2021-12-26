# lista sklada sie ze zbioru elementow, elementy maja index i wartosc, numeracja indeksow zaczyna sie od 0.
# liste mozna zdefiniowac na pare sposobow


# w nawiasnie kwadratowyn wpisujemy wartosci
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(type(arr))  # <type 'list'>
print(arr)  # [1, 2, 3, 4, 5, 6, 7, 8]

# rozbija wyraz na liste z pojedynczych liter
arr = list('kwadrat')
print(arr)  # ['k', 'w', 'a', 'd', 'r', 'a', 't']

# przez list comprehension

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4]
arr2 = [i*2 for i in arr]
print(arr2)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 8]

# wartosc mozna latwo odczytac przez nazwa_listy[indeks], mozna tak tez nadawac wartosc
arr = ['motyl', 'pies', 'kangur', 'stonoga']
print(arr[3])  # 'stonoga'
arr[3] = 'dinozuar'
print(arr)  # ['motyl', 'pies', 'kangur', 'dinozuar']

# nazwa_listy.append(element) - dodaje element na koncu listy

arr = ['raz', 'dwa', 'trzy']
arr.append('maupa')
print(arr)  # ['raz', 'dwa', 'trzy', 'maupa']
arr.append('pies')
print(arr)  # ['raz', 'dwa', 'trzy', 'maupa', 'pies']

# nazwa_listy.pop(index) - usuwa element na koncu listy (domyslnie), mozna podac numer indeksu wtedy usuwa pod podanym indeksem

arr = ['raz', 'dwa', 'trzy', 'cztery', 'piec']
arr.pop()
print(arr)  # ['raz', 'dwa', 'trzy', 'cztery']
arr.pop(1)
print(arr)  # ['raz', 'trzy', 'cztery']

# nazwa_listy.remove(wartosc) - usuwa element o danej w argumencie wartosci

arr = ['Aneta', 'Marian', 'Janusz', 'Michal', 'Pawel', 'Kamil', 'Janusz']
arr.remove('Marian')
print(arr)  # ['Aneta', 'Janusz', 'Michal', 'Pawel', 'Kamil', 'Janusz']
arr.remove('Janusz')
# ['Aneta', 'Michal', 'Pawel', 'Kamil', 'Janusz'] -usuwa pierwsza jaka znajdzie
print(arr)

# nazwa_listy.index(wartosc) - wyszukuje indeks elementu o wskazanej wartosci - pierwszy jaki znajdzie
arr = ['kwadrat', 'trojkat', 'romb', 'graniastoslup']  # 2
print(arr.index('romb'))

# len(lista) - podaje dlugosc listy
arr = [1, 123, 434, 546, 7, 643, 32, 123123, 55, 2, 3]
print(len(arr))  # 11

# nazwa_listy.count(wartosc) - liczy elementy o danej wartosci w liscie
arr = ['raz', 'dwa', 'trzy', 'cztery', 'piec', 'dwa', 'raz']
print(arr.count('dwa'))  # 2

# nazwa_listy.insert(numer_indeksu,element) - wstawia element podany jako argument przed elementetem o numerze_indeksu istniejacym w liscie

arr = ['Aneta', 'Marian', 'Janusz', 'Michal', 'Pawel', 'Kamil', 'Janusz']
arr.insert(1, 'Antoni')
# ['Aneta', 'Antoni', 'Marian', 'Janusz', 'Michal', 'Pawel', 'Kamil', 'Janusz']
print(arr)
