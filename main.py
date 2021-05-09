from collections import Counter

import requests
import urllib.request
from lxml import etree

def get_numbers_as_list ():
    fp = urllib.request.urlopen("https://bet.szerencsejatek.hu/cmsfiles/otos.html")
    my_bytes = fp.read()

    html_content = my_bytes.decode("utf8")
    # print(html_content)
    table = etree.HTML(html_content).find("body/table")
    rows = iter(table)
    # print(rows)
    headers = [col.text for col in next(rows)]
    number_list = []
    for row in rows:
        column = [col.text for col in row]
        number_list = number_list + column[-5:]
    return number_list

#print (get_numbers_as_list())
dictionary_of_numbers ={}
for i in range(1,91):
    dictionary_of_numbers[i]=0

numbers = get_numbers_as_list()
numbers = list(map(int, numbers))
print (numbers)
for i in numbers:
    dictionary_of_numbers[i] = dictionary_of_numbers[i]+1

sorted_dict_of_numbers = sorted(dictionary_of_numbers.items(), key=lambda x: x[1])
print ("A leggyakrabban kíhúzott öt szám: (szám, előfordulás)")
print (sorted_dict_of_numbers[-5:])






