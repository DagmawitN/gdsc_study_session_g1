def get_paragraph():
    lines = []
    print("Enter your paragraph. Press Enter twice to finish:")
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
           break
    paragraph = '\n'.join(lines)
    return paragraph

def get_words(paragraph):
    words = paragraph.split()
    return words

def calculate_word_frequency(words_list):
    word_frequency = {}
    for word in words_list:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

def search_word_frequency(word_frequency, search_word):
    if search_word in word_frequency:
        frequency = word_frequency[search_word]
        print(f"The word " , search_word , " appears ",frequency," times.")
    else:
        print(f"The word ", search_word, " does not appear in the text.")

from collections import Counter

def display_top_words(word_frequency, N):
    counter = Counter(word_frequency)
    top_words = counter.most_common(N)
    print(f"Top {N} words:")
    for word, frequency in top_words:
        print(word, " = ", frequency)

paragraph = get_paragraph()
word_list = get_words(paragraph)
word_freq = calculate_word_frequency(word_list)
print ("Word frequency : ")
for word , n in word_freq.items() :
    print (word , " = " , n)
num = int(input ("enter top number of word to display : "))
display_top_words(word_freq , num)
search = input("Enter word to search : ")
search_word_frequency(word_freq , search)

