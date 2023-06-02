from borders_optimize import calculate_borders
from answers import return_answer

table = 'table.csv'
borders = calculate_borders(table)


while True:
    score = float(input('Введите значение score: '))
    print(f'Ответ - {return_answer(score, borders)}')


