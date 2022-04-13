# def decompose(n):
#     goal = 0
#     print ("Adding n, %s, to sequence.\n" % (n))
#     result = [n]
#     while result:
#         current = result.pop()
#         print ("The last number, %s, wasn't helpful. "
#                "Removing it from sequence and adding it back to `goal`" % (current))
#         print ("Trying lower numbers now.\n" if current - 1 > 0 else "\n")
#
#         goal += current ** 2
#         for i in range(current - 1, 0, -1):
#             print ("Trying %s" % (i))
#             if goal - (i ** 2) >= 0:
#                 goal -= i ** 2
#                 result.append(i)
#                 print("This number, %s, might work. Goal is not below zero. "
#                       "Adding it to sequence and subtracting from `goal`." % (i))
#                 if goal == 0:
#                     result.sort()
#                     print ("\nFound result, %s." % (result))
#                     return result
#             else:
#               print ("This number, %s, is too big here. Continuing." % (i))
#     return None

def decompose(n):
    def _recurse(s, i):
        if s < 0:
            return None
        if s == 0:
            return []
        for j in range(i-1, 0, -1):
            sub = _recurse(s - j**2, j)
            if sub != None:
                return sub + [j]
    return _recurse(n**2, n)


if __name__ == '__main__':
    print(decompose(5))