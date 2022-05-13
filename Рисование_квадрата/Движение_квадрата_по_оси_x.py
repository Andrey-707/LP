# Задача. Движущийся квадрат по оси x.
'''Условие задачи:
Напишите программу, которая рисует движущийся квадрат. Квадрат должен «лететь» от левого
края холста к правому. Программа должна закончиться, как только квадрат «вылетит» за
правый край холста.
Объявите переменную x и присвойте ей значение 0. После напишите цикл while, который
будет выполняться до тех пор, пока переменная x будет меньше 350. В каждой итерации
этого цикла вы должны:
Увеличить значение x на 2
Переменная x будет увеличиваться до тех пор, пока не станет больше 350, то есть больше
ширины холста.
Очистить холст
Перед тем, как нарисовать квадрат, нужно очистить холст от предыдущего кадра. Для этого
надо использовать функцию canvas.clear(). Не забудьте импортировать модуль canvas в
самом начале программы.
Нарисовать квадрат
Используйте fill_rect или stroke_rect на свой выбор. Переменная x должна быть
координатой левого края квадрата. Координата y может быть любой — главное, чтобы
квадрат был виден. Сторона квадрата — 50 пикселей. Не забудьте вызвать canvas.draw()
для прорисовки кадра.
Сделать паузу
Если квадрат «летит» по холсту слишком быстро, после каждой прорисовки кадра можно
делать небольшую паузу в одну сотую секунды. Для того, чтобы сделать паузу, импортируйте
модуль time в начале программы, а после canvas.draw() вызовите time.sleep(0.01)
'''
import canvas # модуль canvas работает на платформе https://letpy.com
import time


# Координаты квадрата
x, y = 0, 0

# Размеры квадрата
width, height = 50, 50

# Предварительно отрисуем кадрат на холсте
canvas.stroke_rect(x, y, width, height)
canvas.draw()

xn = 350 # крайняя точка, по оси Х, после пересечения которой цикл остановится
while x < xn:
    # очистка холста перед выполнением цикла отрисовки новой фигуры
    # если не очищать холст, он будет закрашен движущейся фигурой, словно мелом
    canvas.clear()
    # фигура получает координаты в начале каждой итерации
    canvas.fill_rect(x, y, width, height)
    # отрисовка фигуры
    canvas.draw()
    # пауза между итерациями 0.01 секунды
    time.sleep(0.01)
    # движение фигуры относительно оси x на 2
    x += 2
