def _next_permutation(array):
    i = max(i for i in range(1, len(array)) if array[i - 1] < array[i])
    j = max(j for j in range(i, len(array)) if array[j] > array[i - 1])
    array[j], array[i - 1] = array[i - 1], array[j]
    array[i:] = reversed(array[i:])


def next_permutation(n):
    array = list(str(n))
    try :
        _next_permutation(array)
        return int(''.join(array))
    except (ValueError):
        return (-1)


print(next_permutation(2017))


'''import itertools
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1'''