from urllib.request import urlopen
from bs4 import BeautifulSoup

res = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(res.read(),'lxml')
# print(bs)
# print(res.read())
try:
    badContent = bs.ExistingTag.anotherTag
except AttributeError as e:
    print('Tag was not')
else:
    if badContent == None:
        print ('Tag was not found')
    else:
        print(badContent)