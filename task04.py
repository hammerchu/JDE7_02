import random

text=""
with open('./news.txt', "r", encoding="utf-8") as f:
    text=f.read()

def memberOne():
    print_text=""
    word=""
    for char in text:
        if char.isalpha():
            word+=char
        else:
            if len(word) > 0:
                print_text +=  word[::-1]
            word=""
            print_text += char
    return print_text

if __name__ == "__main__":
    print(memberOne())
   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
