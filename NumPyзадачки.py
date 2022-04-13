import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
'''
Как найти количество уникальных значений в массиве NumPy? Найдите уникальные значения и их количество в столбце species таблицы iris.
# Решение
# Извлекаем столбец species как массив
species = np.array([row.tolist()[4] for row in iris])
print(species)
# Получаем уникальные значения и их количество
np.unique(species, return_counts=True)
print(np.unique(species, return_counts=True))'''
'''

Как найти второе максимальное значение в массиве, который сгруппирован по другому массиву? Найдите значение второго самого длинного petallength вида setosa в таблице iris.
# Ввод
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

# Решение
# Извлекаем столбцы вида и длины лепестков
setosa_petal_len = iris[iris[:, 4] == b'Iris-setosa', [2]].astype('float')

# Получаем второе значение с конца
np.unique(np.sort(setosa_petal_len))[-2]'''