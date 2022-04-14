"""def listCheck(nums):
    for i in range(len(nums)-2): #ЦИКЛ ЗАКОНЧИТСЯ КОГДА ПРОИЗОЙДЕТ ВЗАИМОДЕЙСТВИЕ С ПОСЛЕДНИМ ЭЛЕМЕНТОМ СПИСКА
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
        return False
print(listCheck([1,2,3,1,2]))"""

'''def stingbits(str):
    return str[::2]
print(stingbits('Hello'))'''

'''def end_other(a, b):
    a = a.lower()
    b = b.lower()

    # return (b.endswitch(a) or a.endswitch(b))
    return a[-(len(b)):] == b or a == b[-len(a):]'''
'''def doublewords(str):
    j = ''
    for i in str:
        j += i*2
    return j'''
'''def poiskchisel(num):
    count = 0
    for i in num:
        if i % 2 == 0:
            count += 1
    return '{} Четных '.format(count)'''
