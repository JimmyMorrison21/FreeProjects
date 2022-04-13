def simplify(poly):
    # I'm feeling verbose today

    # get 3 parts (even if non-existent) of each term: (+/-, coefficient, variables)
    import re
    matches = re.findall(r'([+\-]?)(\d*)([a-z]+)', poly)

    # get the int equivalent of coefficient (including sign) and the sorted variables (for later comparison)
    expanded = [[int(i[0] + (i[1] if i[1] != "" else "1")), ''.join(sorted(i[2]))] for i in matches]

    # get the unique variables from above list. Sort them first by length, then alphabetically
    variables = sorted(list(set(i[1] for i in expanded)), key=lambda x: (len(x), x))

    # get the sum of coefficients (located in expanded) for each variable
    coefficients = {v:sum(i[0] for i in expanded if i[1] == v) for v in variables}

    # clean-up: join them with + signs, remove '1' coefficients, and change '+-' to '-'
    return '+'.join(str(coefficients[v]) + v for v in variables if coefficients[v] != 0).replace('1','').replace('+-','-')

print(simplify("2xy-yx"))

'''import re
from collections import Counter
def simplify(poly):
    poly = re.sub('((?<=[-+])|^)(?=[a-z]+)', r'1', poly)
    terms = re.findall(r'(-?[0-9]+)([a-z]*)', poly)
    c = Counter()
    for n, term in terms:
        c[''.join(sorted(term))] += int(n)
    result = '+'.join('%d%s'%(n,x) for x, n in sorted(c.items(), key=lambda (x,_): (len(x), x)) if n)
    return re.sub(r'\+(?=-)|((?<=-|\+)|^)1(?=[a-z])', '', result)'''