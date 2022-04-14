def schet(word) :
    s1,s2=0,0
    for r in word:
        if r == '(':
            s1 += 1
        else:
            s2 += 1
    if s1 == s2:
        return True
    else:
        return False

stroka = 'hi(hi)()'
arr=[]
for i in  stroka :
    if i == '(' or i == ')':
        arr.extend(i)
print(arr)
print(len(arr))
l=0
if (arr[0] == '(' and arr[-1] == ')') and len(arr)%2 == 0 and schet(arr) == True:
    print('True')
else:
    print('False')
'''def valid_parentheses(string):
    # your code here

    stack = []
    for s in string:
        if(s == '('):
            stack.append(s)
        elif(s == ')'):
            try:
                stack.pop()
            except:
                return False

    if(len(stack) == 0):
        return True
    else:
        return False'''