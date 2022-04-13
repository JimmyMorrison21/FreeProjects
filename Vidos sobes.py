'''Дан массив целых чисел. Функция возвращает True, если он содержит дубликаты, в обратном случае возвращает False'''

def check_double(x):
    return len(x) != len(set(x))

'''Дано положительное число, найти сумму его цифр. Если передается не число, тогда вернуть строку "Неверный ввод"'''
def dig_sum(x2):
    if type(x2) == int:
        res = 0
        for i in str(x2):
            res += int(i)
        return res
    else:
        return "Неверный ввод"

'''Дано целое число x3. Вернуть наибольшее число, содержащее ровно x3 цифр'''

def max_dig(x3):
    res =''
    while len(res) != x3:
        res += '9'
    return int(res)

