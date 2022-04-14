s='asd'

output = []
for count, letter in enumerate(s):
    output.append(letter.upper() + letter.lower() * (count))

print('-'.join(output))