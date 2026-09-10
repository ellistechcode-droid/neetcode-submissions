from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    county = {}
    for i in word:
        if i in county:
            county[i] += 1
        else:
            county[i] = 1
    return county





# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
