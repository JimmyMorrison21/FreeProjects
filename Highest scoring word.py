x='man i need a taxi up to ubud'
arr,numArr= x.split(' '),[]
for val in arr:
    intNum = 0
    letters = list(val)
    for word in letters:
        intNum += ord(word) - 96
    numArr.append(intNum)
print (arr[numArr.index(max(numArr))])
