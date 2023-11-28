def wrd_len (str) :
    length = []
    for word in str.split() : 
        word_length = len(word)
        length.append(word_length)
    return length

def calculate_average (lengths) :
    total =sum(lengths)
    av = total /len(lengths) 
    return av

def longest_word(str): 
    words = str.split() 
    longest = ""
    longest_len = 0
    for word in words:
        if len(word) > len (longest):
            longest = word
            longest_len = len(word)
    print("longest word : ",longest ," with length :", longest_len) 

def shortest_word(str):
    words = str.split() 
    shortest = words[0]
    shortest_len = len(words[0])
    for word in words:
        if len(word) < shortest_len:
            shortest = word
            shortest_len = len(word)
    print("shortest word : ",shortest ," with length :", shortest_len)
def word_frequency(str):
    words = str.split()
    word_freq = {}
    for word in words :
        length = len(word)
        if length in word_freq :
            word_freq[length] +=1
        else : 
            word_freq[length] = 1
    return word_freq

def display(word_freq):
    print ("Word length distribution : " )
    sorted_length = sorted(word_freq.items())
    for length , n in sorted_length : 
        print("number of words with length" , length ," = " , n)

words = input("Enter words separated by space : ")
length = wrd_len(words)
print ("Average length of words : ", calculate_average (length))
longest_word(words)
shortest_word(words)
frequency = word_frequency(words)
display (frequency)

