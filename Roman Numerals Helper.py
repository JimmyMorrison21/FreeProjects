class RomanNumerals:

    def to_roman(self):
        coding = zip(
            [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
            ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        )
        if self <= 0 or self >= 4000 or int(self) != self:
            raise ValueError('Input should be an integer between 1 and 3999')
        result=[]
        for d,r in coding:
            while self>=d:
                result.append(r)
                self -= d
        return ''.join(result)

    def from_roman(self):
        decoding = dict((zip(
            ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"],
            [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        )))
        resultb = []
        result = 0
        for i in range(len(self)):
            resultb.append(decoding.get(self[i]))
        for j in range(len(resultb) - 1):
            if resultb[j] >= resultb[j + 1]:
                result += resultb[j]
            if resultb[j] < resultb[j + 1]:
                result -= resultb[j]
        result += resultb[-1]
        return result