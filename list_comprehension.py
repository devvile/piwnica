# list comprehension - czyli zrozumienie listy to sposob budowania list w oparciu o juz istniejace,
# byl obecny przed pythonem w innych jezykach programowania

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print([i for i in arr])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
arr2 = [i*2 for i in arr]

print(arr2)
#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

'''
podobny efekt daje:
arr2 = []
for i in arr:
    arr2.append(i*2)
print(arr2)
'''

# mozna dodac bramke warunkowa if na koncu

arr2 = [i for i in arr if i % 2 == 0]  # obliczenie liczb parzystych
print(arr2)

# mozna tez wykorzystac else, wtedy zmienia sie kompozycja
arr2 = ['parzysta' if i % 2 == 0 else i for i in arr]
print(arr2)  # [1, 'parzysta', 3, 'parzysta', 5, 'parzysta', 7, 'parzysta', 9, 'parzysta', 11, 'parzysta', 13, 'parzysta', 15, 'parzysta', 17, 'parzysta', 19, 'parzysta']
