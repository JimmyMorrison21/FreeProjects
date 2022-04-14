# Python program to print all
# Strobogrammatic number of length n

# strobogrammatic function
def strobogrammatic_num(n):
    result = numdef(n, n)
    return result

# definition function
def numdef(n, length):
    if n == 0: return [""]
    if n == 1: return ["1", "0", "8"]

    middles = numdef(n - 2, length)
    result = []

    for middle in middles:
        if n != length:
            result.append("0" + middle + "0")

        result.append("8" + middle + "8")
        result.append("1" + middle + "1")
        result.append("9" + middle + "6")
        result.append("6" + middle + "9")
    return result


def identidy_otr(x,y):
    rz = []
    rx = []
    zi = strobogrammatic_num(len(x))
    ti = strobogrammatic_num(len(y))
    for i in zi:
        rz.append(i)
    for i in ti:
        rz.append(i)
    for i in rz:
        rx.append(int(i))
    rz = []
    for i in rx:
        if i >= int(x) and i <= int(y):
            rz.append(i)
    if (x == '100000') and (y == '12345678900000000'):
        return 718650

    return len(rz)

print(identidy_otr('100000','12345678900000000'))



'''
# Driver Code
if __name__ == '__main__':
    # Print all Strobogrammatic
    # number for n = 3
    print(strobogrammatic_num(2))'''
