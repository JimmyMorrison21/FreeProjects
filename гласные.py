s="This website is for losers LOL!"
for i in s:
    if i.lower()=='a' or i.lower()=='e' or i.lower()=='i' or i.lower()=='o' or i.lower()=='u':
        s=s.replace(i,"")
print(s)