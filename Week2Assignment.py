import re

PATH = './regex_sum_178807.txt'
with open(PATH) as f:
    string = f.read()
    print(sum(map(int,re.findall('[0-9]+',string))))

