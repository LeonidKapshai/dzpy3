# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

n = int(input("Введите количество элементов массива:")) 
a = []
for i in range (n):
    a.append(int(input("Введите элемент массива ")))
   
x = int(input("Введите число близкому к которому необходимое найти значение: "))
min = abs(a[0]-x)
num = a[0]
for i in a:
    if abs(i-x)<min:
        min=abs(i-x)
        num=i 
print ("Близкое по значению число в массиве ", end='- ' )
print(num)