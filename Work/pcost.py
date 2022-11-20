# pcost.py
#
# Exercise 1.27

file_name = input('Enter file name with path: ')
header = input('First line is header: y/n ')

content = []

with open(file_name, 'rt') as f:
    for line in f:
        content.append(line.replace('\n', '').split(','))

SHARES = 1
PRICE = 2

result = sum(map(lambda x: int(x[SHARES]) * float(x[PRICE]), content[1:]))
    
print(f'Total result: {result}')
