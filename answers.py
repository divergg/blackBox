CORRECT = 'CORRECT'
REASK = 'REASK'
OPERATOR = 'OPERATOR'

def return_answer(score: float, borders: tuple):
    score = score * 100
    if score > 100 or score < 0:
        raise ValueError('Ошибка! Введено неверное значение')
    if score < borders[0]:
        return OPERATOR
    if score > borders[1]:
        return CORRECT
    return REASK
