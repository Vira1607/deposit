print('Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Программа по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

deposit_begin = int(input('Первый вклад: '))
deposit_end = int(input('Последний вклад: '))
percent = int(input('Проценты: '))

counter = 0

while deposit_begin < deposit_end:
    deposit_begin += (deposit_begin * percent) // 100
    counter += 1

print(counter, 'лет')
