# Элемент_списка _и_его_индекс.Функция_enumerate()
i = 0
list_ = ["Первое слово", "Второе", "Третье слово"]
for el in list_:
    print(i, e)
    i += 1

# Лучше воспользоваться функцией enumerate(). Эта функция преобразует каждый элемент
# последовательности в кортеж. Первым в кортеже будет идти индекс элемента
# последовательности. Вторым — сам элемент последовательности
list_ = ["Первое слово", "Второе", "Третье слово"]
for el in enumerate(list_):
    # в каждой итерации enumerate будет
    # создавать кортеж из двух элементов
    print(el[0], el[1])

# Этот кортеж можно распаковать в две переменные и тогда код станет чуточку лучше
list_ = ["Первое слово", "Второе", "Третье слово"]
for el in enumerate(list_):
    i, e = el
    print(i, e)

# А благодаря удобству Python, кортеж можно распаковать прямо в строке с объявлением
# цикла. Это даст нам самый простой и красивый код
list_ = ["Первое слово", "Второе", "Третье слово"]
for i, el in enumerate(list_):
    # в каждой итерации enumerate будет
    # создавать кортеж из двух элементов.
    # Этот кортеж, в свою очередь,
    # будет распакован в переменные
    print(i, el)

# Если указать индекс, например 1, то программа будет начинать нумерацию с 1
list_ = ["Первое слово", "Второе", "Третье слово"]
for i, e in enumerate(list_, 1):
    # в каждой итерации enumerate будет
    # создавать кортеж из двух элементов.
    # Этот кортеж, в свою очередь,
    # будет распакован в переменные
    print(i, e)
