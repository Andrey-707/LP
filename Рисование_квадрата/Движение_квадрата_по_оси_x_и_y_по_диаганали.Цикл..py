# Задача. Движение_квадрата_по_оси_x_и_y_по_диаганали.Цикл.
'''Условие задачи: (старое условие (только для оси х не в цикле))
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


x, y = 0, 0
width, height = 50, 50
xn = 300 # крайняя точка, по оси Х
delta = 2

while True:
    while x < xn:
        canvas.clear()
        canvas.fill_rect(x, y, width, height)
        canvas.draw()
        time.sleep(0.01)
        x += delta
        y += delta
    delta = -delta
    while x > 0:
        canvas.clear()
        canvas.fill_rect(x, y, width, height)
        canvas.draw()
        time.sleep(0.01)
        x += delta
        y += delta
    delta = -delta

# Бесконечный цикл по оси x и y можно написать проще.
import canvas # модуль canvas работает на платформе https://letpy.com
import time


x, y = 0, 0
delta = 2

while x < 350:
    if x < 0 or x > 300:
        delta = -delta
    canvas.clear()
    canvas.fill_rect(x, y, 50, 50)
    canvas.draw()
    x += delta 
    y += delta
    time.sleep(0.01)