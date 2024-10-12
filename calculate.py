"""
Импортируем circle и square.
Они содержат функции для вычисления периметра и площади круга и квадрата.
"""
import circle
import square

"""
Определяем список доступных фигур, а затем функций. После чего создаём sizes.
"""
figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}
"""
Создаем функцию calc, которая принимает три аргумента: fig, func и size. Эта функция выполняет вычисления в зависимости от типа фигуры, выбранной функции и её размеров. 

Сначала удостоверяемся, что указанные фигура и функция находятся в списках figs и funcs. 

Затем применяем eval для вызова соответствующей функции из модуля фигур. 

В конце выводим на экран результат вычислений, показывая, какая функция была применена к какой фигуре и каков итог.
	"""
def calc(fig, func, size):
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')
  """
    Разрабатываем функцию под названием calc, которая принимает три параметра: fig, func и size. Эта функция осуществляет вычисления в зависимости от типа фигуры, выбранной операции и её размеров.

Сначала проверяем, присутствуют ли указанные фигура и функция в списках figs и funcs.

Далее используем eval для вызова соответствующей функции из модуля фигур.

В завершение отображаем результат вычислений, указывая, какая операция была применена к какой фигуре и каков итоговый результат.
    """

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



