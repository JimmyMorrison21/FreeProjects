
def countItems(iter):
  from collections import Counter
  return sorted(Counter(iter).items())
def anagrams(word, words):
    brckt = []
    for i in words:
        if countItems(i) == countItems(word):
            brckt.append(i)
    return brckt

