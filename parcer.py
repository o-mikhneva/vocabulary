# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import os


def cyrillic_match(string) -> bool:
    # re.search returns None if no position in the string matches the pattern
    # pattern to search for any character other then "\-а-яё"
    return not bool(re.search(r'[^-а-яё]', string))


vocabulary: dict[str | int] = {}

for filename in os.listdir("ChatExport"):
    with open(os.path.join("ChatExport", filename), 'r', encoding='utf-8') as f:
        text = f.read()
        soup = BeautifulSoup(text, "html.parser")
        message_list = soup.find_all('div', {'class': 'text'})
        for msg in message_list:
            text = msg.text.lower()
            text = re.split(r'[ ,.—:;?!\n()*]', text)
            for word in text:
                if cyrillic_match(word):
                    if word not in vocabulary:
                        vocabulary[word] = 1
                    else:
                        vocabulary[word] += 1

vocabulary = dict(sorted(vocabulary.items()))
with open('vocabulary.txt', 'a', encoding='utf-16') as f:
    for key in vocabulary:
        if vocabulary[key] > 3:
            f.write(f'{key}\n')

print(vocabulary)