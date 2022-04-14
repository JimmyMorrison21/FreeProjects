class VigenereCipher:
    def __init__(self, key, abc):
        self.key = key
        self.abc = abc

    def encode(self, text):
        result = []
        key=self.key
        key *= len(text)//len(key)+1
        index = 0
        for c in text:
            if c in self.abc:
                offset = self.abc.index(key[index])
                result.append(self.abc[(self.abc.index(c) + offset) % len(self.abc)])
                index += 1
            else:
                result.append(c)
        return ''.join(result)

    def decode(self, text):
        result = []
        key=self.key
        key *= len(text)//len(key)+1
        index = 0
        for c in text:
            if c in self.abc:
                offset = self.abc.index(key[index])
                decoded = self.abc[(self.abc.index(c) - offset) % len(self.abc)]
                result.append(decoded)
                key += decoded
                index += 1
            else:
                result.append(c)
        return ''.join(result)

abc = 'abcdefghijklmnopqrstuvwxyz'
key = 'カタカナ'
c = VigenereCipher(key, abc)
print((c.decode("ドレタウガロゴザキアニ")))