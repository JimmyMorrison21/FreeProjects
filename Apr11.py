
def arithmetic(a,b,opr):
    if opr == '+':
        return a+b
    elif opr == '-':
        return a-b
    elif opr == '*':
        return a * b
    elif opr == '/':
        return a / b
    else:
        return 'Unknow operation'

print(arithmetic(12,44,'-'))

def is_year_leap(year):
    if year % 4 == 0 :
        return 'Високосный'
    else:
        return 'Не високосный'

print(is_year_leap(2020))

def square(side):
    s = side**2
    P = side*4
    dig = (2 ** (1/2)) * side
    return (s,P,round(dig,3))

print(square(5))

def season(month):
    if month < 3 or month == 12 :
        return 'winter'
    elif month >= 3 and month < 6:
        return 'spring'
    elif month >= 6 and month < 9:
        return 'summer'
    elif month >= 9 and month < 12:
        return 'autmn'
    else:
        return 'Incorrect input'

print(season(12))

def bank(a,years):
    for _ in range(years):
        a = a * 1.1
    return a
print(bank(100,3))

def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return n in prime_numbers

print(get_prime_numbers(12))

def XOR_code(string,key):
    result = ''
    for i in range(len(string)):
        temp = ord(string[i])
        for j in range(len(key)):
            temp ^= ord(key[j])
        result += chr(temp)
    return result

def XOR_encode(string,key):
    result = ''
    temp = []
    for i in range(len(string)):
        temp.append(string[i])
        for j in range(len(key)):
            temp[i] = chr(ord(key[j]) ^ ord(temp[i]))
        result += temp[i]
    return result
print(XOR_code('Hello','Word'))
print(XOR_encode('fKBBA','Word'))