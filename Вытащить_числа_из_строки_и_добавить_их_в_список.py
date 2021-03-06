'''
1) Напишите программу, которая получает строку от пользователя с помощью input().
2) Из этой строки программа должна получить список, разбив ее по символу пробела с помощью
метода строки .split()
3) Потом программа должна создать переменную numbers с пустым списком. numbers = []
4) С помощью цикла for программа должна перебрать элементы списка, получившегося после
разбития строки и добавить в список numbers элементы, которые являются числами.
5) Проверить это можно с помощью метода строки .isdigit()
6) При добавлении нужно преобразовывать элементы к целому числу с помощью функции int()
7) После этого нужно отсортировать список numbers по возрастанию.
8) Вывести отсортированный список на экран с помощью функции print()
'''

from rich import print


print("[bold magenta]Program start[/]")

# 1) получаем строку от пользователя с помощью input
# string = input("Строка: ") # раскоментировать для ручного ввода
string = "Мороженое стоит 60 рублей и 50 копеек"

# 2) преобразуем стоку в список
list_ = string.split()

# 3) создаем переменную с пустым списком
numbers = []

# 4) перебираем элементы списка, если они проходят условие, добавляем их к пустому списку
for i in list_:
    # 5) проверяем является ли элемент числом
    if i.isdigit():
        print("Элемент " + i + " является числом.")
        # 6) преобразуем элемент в целое число и добавляем к пустому списку
    	numbers.append(int(i))   	
    else:
        print("Элемент " + i + " НЕ число")
#7)отсортируем список numbers по возрастанию        
numbers.sort()
#8)выводим его на экран
print(numbers)

print("[bold magenta]Program finish[/]")
