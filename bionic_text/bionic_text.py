import string
import requests
from bs4 import BeautifulSoup


punct = []
pun = string.punctuation
for ob in pun:
    punct.append(ob)
punct.remove("'")


def punctuated(word):
    result = []
    for char in punct:
        if word.__contains__(char):
            result.append(1)
    return len(result) > 0, len(result)


def bionic(word):
    res, amount = punctuated(word)
    if res:
        num = len(word) - amount
    else:
        num = len(word)
    char = []
    for ob in word:
        char.append(ob)
    if num < 4:
        bio = char[0]
        reg = char[1:]
        print('\033[1m' + bio, end='')
        print('\033[0m' + ''.join(reg), end=' ')
    elif num == 4:
        bio = ''.join(char[:2])
        reg = char[2:]
        print('\033[1m' + bio, end='')
        print('\033[0m' + ''.join(reg), end=' ')
    elif num < 7:
        bio = ''.join(char[:3])
        reg = char[3:]
        print('\033[1m' + bio, end='')
        print('\033[0m' + ''.join(reg), end=' ')
    elif num < 9:
        bio = ''.join(char[:4])
        reg = char[4:]
        print('\033[1m' + bio, end='')
        print('\033[0m' + ''.join(reg), end=' ')
    elif num < 11:
        bio = ''.join(char[:5])
        reg = char[5:]
        print('\033[1m' + bio, end='')
        print('\033[0m' + ''.join(reg), end=' ')
    elif num < 13:
        bio = ''.join(char[:6])
        reg = char[6:]
        print('\033[1m' + bio, end='')
        print('\033[0m' + ''.join(reg), end=' ')
    elif num < 15:
        bio = ''.join(char[:7])
        reg = char[7:]
        print('\033[1m' + bio, end='')
        print('\033[0m' + ''.join(reg), end=' ')
    elif num >= 15:
        if num % 2 == 0:
            i = int(num / 2)
        else:
            i = int((num + 1) / 2)
        bio = ''.join(char[:i])
        reg = char[i:]
        print('\033[1m' + bio, end='')
        print('\033[0m' + ''.join(reg), end=' ')


def convert_to_bionic(text, words_per_row=30):
    for i in range(30):
        text = text.replace('  ', ' ')
    splitt = text.split(' ')
    y = words_per_row
    if len(splitt) > y:
        for i in range((len(splitt) // y) + 1):
            n = y * i
            m = y * (i + 1)
            for b in splitt[n:m]:
                bionic(b)
            print('')
    else:
        for word in splitt:
            bionic(word)


def convert_bionic(text, url=False, words=30):
    if url:
        page = requests.get(text)
        soup = BeautifulSoup(page.content, 'html.parser')
        elements = soup.find_all('p')
        scrape = []
        for i in elements:
            scrape.append(i.text)
        final = ' '.join(scrape)
        text = final.replace('\n', ' ').lstrip(' ').rstrip(' ')
    convert_to_bionic(text, words_per_row=words)
    print('')


# sentence to transfrom
text_input = 'Hello, my name is Oliver'

# function to transfrom, when input is not url
convert_bionic(text_input, url=False)

# regular to compare
print('Hello, my name is Oliver')

# link to scrape and transfrom text
wikipedia_link = 'https://en.wikipedia.org/wiki/Data_science'

# function to transfrom, and using url arguement
convert_bionic(wikipedia_link, url=True, words=5)
