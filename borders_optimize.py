import pandas as pd
import numpy as np

"""
Для бота предполагается следующая логика ответов:
Если score <= left_border: осуществляется перевод  на оператора
Если score > right_border: ответ положительный (correct)
В остальных случаях алгоритм должен просить переформулировать вопрос

Для определения точности алгоритма выбрана метрика Accuracy, т.к. 
алгоритм должен равновероятно определять тип ответа.
Проводится оптимизация границ диапазона для максимизации данной метрики
"""

def calculate_borders(table_path):

    # Загрузка данных
    df = pd.read_csv(table_path)
    scores = df['Score']
    real_values = df['Action']

    pd.set_option('display.max_rows', len(scores))

    # Словарь для записи величины метрики Accuracy в зависимости от величины границ
    accuracy = {}

    # Итерирование по границам (сдвигаем правую при постоянной левой и постепенно сдвигаем левую)
    for left_edge in range(0, 101):
        for right_edge in range(left_edge, 101):

            # Присваиваем результатам черного-ящика человекоподобные ответы
            black_box_actions = np.where(scores <= left_edge, 'operator',
                                         np.where((left_edge < scores) & (scores <= right_edge), 'reask', 'correct'))
            total_sum_of_correct_answers = np.sum(real_values == black_box_actions)

            # Выполняем подсчет суммарного количества правильных ответов
            accuracy[(left_edge, right_edge)] = total_sum_of_correct_answers

    # Определение оптимальных границ
    optimal_borders = max(accuracy, key=accuracy.get)

    return optimal_borders


