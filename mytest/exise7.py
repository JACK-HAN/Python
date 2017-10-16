
def sumOfWord(word):
    sum = 0
    for char in word:
        sum += (ord(char) - 96)
    return sum


s = sumOfWord('attitude')
print(s)

with open('targetWords.txt', 'w', encoding='utf-8') as tf:
    with open('words_alpha.txt', 'r', encoding='utf-8') as f:
        for word in f.readlines():
            if sumOfWord(word.strip()) == 100:
                tf.write(word)
