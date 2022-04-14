brckt=[0,1,None,2,False,1,0]
brckt1=[]
sch=brckt.count(0)
for i in brckt:
    if i is False:
        sch -=1
    if i  != 0 or i is False :
        brckt1.append(i)
while sch > 0:
    brckt1.append(0)
    sch -=1
print(brckt1)

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
print(move_zeros([0,1,None,2,False,1,0]))
