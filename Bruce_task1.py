import random

text = './news.txt'
f = open(text, "r")
print(f.read())


def Bruce_task_0():
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
    print(hammer())
    print('call memberOne() ')
    print('call memberTwo() ')
    print('call memberThree() ')
    print('call memberFour() ')


# Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
import random

def count_words_with_vowels(paragraph):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word_count = 0

    # Split the paragraph into words
    words = paragraph.split()

    # Iterate over each word
    for word in words:
        # Check if the word contains any vowel characters
        if any(vowel in word.lower() for vowel in vowels):
            word_count += 1

    return word_count


# Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz


def encode_paragraph(paragraph, shift):
    encoded_paragraph = ""

    for char in paragraph:
        if char.isalpha():
            if char.isupper():
                encoded_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encoded_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encoded_char = char

        encoded_paragraph += encoded_char

    return encoded_paragraph


# Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

# Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
