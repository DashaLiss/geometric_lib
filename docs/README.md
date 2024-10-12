# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Общее описание решения
## square.py
### def area(a) **Возвращает площадь квадрата**
- def area(a): *Параметры: принимает число a*
-	return a * a ~~Возвращаемое значение: а в квадрате~~
- премер area(5)
  >> 25
###def perimeter(a) **Возвращает периметр квадрата**
- def perimeter(a): ***Параметры: принимает число а***
-	return 4 * a <sub>Возвращаемое значение: произведение 4 и а</sub>
- пример perimeter(4)
  >> return 16
## circle.py import math <sup>Импортируем библиотеку math, чтобы подключить math.pi</sup>
### def area(r) *Возращает площадь круга*
- def area(r): *Принимаемое занчение: число r - радус круга*
-   return math.pi * r * r *Возращаемое значение : произведение пи на радиус в квадрате*
-   пример area(3)
  >> return 28,26
### def perimeter(r): *Возращает периметр круга*
- def perimeter(r): *Принимаемое занчение: число r - радус круга*
-   return 2 * math.pi * r *Возращаемое значение : произведение 2 на пи на радус круга*
-   пример perimeter(2)
  >> return 12,56
## triangle.py
### def area(a, b, c)
- def area(a, b, c): *Определяет функцию area, которая принимает три аргумента: a, b и c.*
- return (a + b + c) / 2 *Вычисляет сумму трех чисел a, b и c (a + b + c), а затем делит результат на 2. return возвращает результат вычисления функции area.*
### def perimeter(a, b, c)
- def perimeter(a, b, c): *Определяет функцию с именем perimeter, которая также принимает три аргумента: a, b и c*
- return a + b + c *Вычисляет сумму трех чисел a, b и c (a + b + c). return возвращает результат вычисления функции perimeter.*
## calculate.py

- import circle, import square *Эти строки импортируют модули circle и square, которые, предположительно, содержат функции для вычисления периметра и площади соответствующих фигур.*
- figs = ['circle', 'square'] *Создает список доступных фигур (circle и square).*
- funcs = ['perimeter', 'area'] *Создает список доступных функций (perimeter и area).*
- sizes = {} *Создает пустой словарь sizes, который в будущем, возможно, будет использоваться для хранения информации о размерах фигур.*
- fig *Название фигуры (например, circle).*
- func *Название функции (например, perimeter).*
- size *Список значений, необходимых для вычисления (например, радиус круга или сторона квадрата).*
- assert fig in figs *Проверяет, существует ли фигура fig в списке figs. Если нет, то программа завершится с ошибкой.*
- assert func in funcs *Проверяет, существует ли функция func в списке funcs. Если нет, то программа завершится с ошибкой.*
- result = eval(f'{fig}.{func}(*{size})') *Вычисляет результат функции func из fig.* 
- f'{fig}.{func}(*{size})'  *это строка, которая формируется в зависимости от значений fig, func и size.*
- eval() *выполняет строку в результате чего вызывается функция func из fig с передачей значений size.*

# History
- |Sat Oct 12 20:21:37 2024 +0300|8bbf1f1|Dasha Ivanova|add documentation for triangle.py|
- |Sat Oct 12 20:20:50 2024 +0300|f2f701a|Dasha Ivanova|Add documentation to square.py|
- |Sat Oct 12 20:20:00 2024 +0300|9704402|Dasha Ivanova|Add documentation to circle.py|
- |Sat Oct 12 20:18:53 2024 +0300|52f9ead|Dasha Ivanova|add documentation for calculate.py|
- |Thu Mar 4 14:55:29 2021 +0300|d078c8d|smartiqa|Docs added|
- |Thu Mar 4 14:54:08 2021 +0300|8ba9aeb|smartiqa|Circle and square added|

