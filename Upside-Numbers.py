def strobogrammatic_num(n):
    result = numdef(n)
    return result

# definition function
def numdef(n):
    if n == 0: return [""]
    if n == 1: return ["1", "0", "8"]

    middles = numdef(n - 2)
    result = set()

    for middle in middles:

        result.add("8" + middle + "8")
        result.add("1" + middle + "1")
        result.add("9" + middle + "6")
        result.add("6" + middle + "9")

    print(result,len(result))
    return result


def upsidedown(x,y):
    counter = 0
    if int(x) > int(y):
        zi = strobogrammatic_num(len(x))
    else:
        zi = strobogrammatic_num(len(y))
    for i in zi:
        if int(i) <= int(x) and int(i) >= int(y):
            counter += 1

    return counter

print(upsidedown('10','100'))