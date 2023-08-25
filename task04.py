import random

text = r"C:\Users\fan00\Desktop\JDE7\JDE7_02\news.txt"
with open(text, "r", encoding="utf-8") as f:
    words = f.read()


def hammer_task_0():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result
  
def memberOne():
    pass
  
def memberTwo():
    pass
  
def memberThree():
    pass
  
def memberFour():
    pass


if __name__ == "__main__":
    # print(hammer())
    print('call memberOne() ')
    print('call memberTwo() ')
    print('call memberThree() ')
    print('call memberFour() ')
   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)

parag_split = words.split('\n')
# print(len(parag_split)) # for checking

for i, para in enumerate(parag_split):
    word_splits = para.split(' ')
    # print(word_splits) # for checking
    # print(len(word_splits)) # for checking
    vowels = []
    for word_split in word_splits:
        if "a" in word_split:
            vowels.append(word_split)
        elif "e" in word_split:
            vowels.append(word_split)
        elif "i" in word_split:
            vowels.append(word_split)
        elif "o" in word_split:
            vowels.append(word_split)
        elif "u" in word_split:
            vowels.append(word_split)
        else:
            pass
    print(f'Paragrah {i+1} has {len(vowels)} words')

    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

parag_split = words.split('\n')
for i, para in enumerate(parag_split):
    words_split = para.split(" ")
    reversed_words = []
    for word_split in words_split:
        reversed_words.append(word_split[::-1])
    print(f"The {i+1} para: {reversed_words}")

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

parag_split = words.split('\n')
for i, para in enumerate(parag_split):
    words_split = para.split(" ")
    # print(words_split) # for checking
    # print(type(words_split)) # for checking
    # print(len(words_split)) # for checking
    vocab_reversed = words_split[::-1] # have no ideas of why can't use reverse
    print(f"The {i+1} para: {vocab_reversed}")

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
    
    # not done
