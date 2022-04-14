def spin_words(sentence):
    L = sentence.split()
    new = []
    for word in L:
        if len(word) >= 5:
            new.append(word[::-1])
        else:
            new.append(word)
    string = " ".join(new)
    print (string)
spin_words('Hello darkness my old friend')