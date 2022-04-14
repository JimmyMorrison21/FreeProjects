'''s = 'python'
print(s[0])
print(s[-2])
print(s[:3])
print(s[1:3])
print(s[4:])
print(s[::-1])
print(s[::2])'''

'''age = 10
name = 'Lisa'
print('Hello, my name is {}  and I am {} years old'.format(name,age))'''

'''l = [1,2,[3,2,True],[10,13,'Hello',False]]
l[3][2] = 'Bye'
print(l)'''



'''d1 = {'key':'hello'}
d2 = {'k1': {'k2' : 'hello'}}
d3 = {'k1' : [{'nest_key': ['deep',['hello']]}]}
print(d1['key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])'''

'''mylist = [1,1,1,1,2,2,2,2,3,3,3,3,3]
print((set(mylist)))'''

st1 = 'qwe'
st2 = 'XZZqwe'
st1 = st1.lower()
st2 = st2.lower()
if st1.endswith(st2) or st2.endswith(st1):
    print('true')
else:
    print('false')
