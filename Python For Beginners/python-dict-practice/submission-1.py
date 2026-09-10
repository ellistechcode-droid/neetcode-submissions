from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    dicto = {}
    for i in word:
        if i in dicto:
            dicto[i] += 1
        elif i not in dicto:
            dicto[i] = 1
    return dicto




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
