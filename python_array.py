arr = [1, 2, 3, 4, 5, 6, 7, 8]

arr.insert(4, 'dupa')
print(arr)  # [1, 2, 3, 4, 'dupa', 5, 6, 7, 8]
arr.append(910)
print(arr)  # [1, 2, 3, 4, 'dupa', 5, 6, 7, 8, 910]
arr.pop()
print(arr)  # [1, 2, 3, 4, 'dupa', 5, 6, 7, 8]
arr.append('dupa')
arr.append('dupa')
print(arr)  # [1, 2, 3, 4, 'dupa', 5, 6, 7, 8, 'dupa', 'dupa']
print(arr.count('dupa'))  # 3
print(arr.index('dupa'))  # 4

# [2, 4, 6, 8, 'dupadupa', 10, 12, 14, 16, 'dupadupa', 'dupadupa']
arr2 = [i*2 for i in arr]
print(arr2)
