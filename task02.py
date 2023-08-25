import random

text = './news.txt'
f = open(text, "r")
print(f.read())


# def organge_task_2():
#     '''example function'''

#     teamJDE = ['Feddy', 'Jason C', 'Kelly', 'Gary']
#     result = random.sample(teamJDE, 1)
#     return result
  
# def memberOne():
#     pass
  
# def memberTwo():
#     pass
  
# def memberThree():
#     pass
  
# def memberFour():
#     pass


# if __name__ == "__main__":
#     print(organge_task_2)
#     print('call memberOne() ')
#     print('call memberTwo() ')
#     print('call memberThree() ')
#     print('call memberFour() ')
   
# Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
def count_vowel_words(para):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    words = para.split()
    for word in words:
        if any(vowel in word for vowel in vowels):
            count += 1
    return count


with open(text, 'r') as file:
    para = file.read()

total_num_of_words_with_vowel = count_vowel_words(para)
print(total_num_of_words_with_vowel)

# Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz
def encode_para(para, shift):
    encoded_para = ""
    for char in para:
        if char.isalpha():
            if char.islower():
                encoded_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encoded_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encoded_char = char
        encoded_para += encoded_char
    return encoded_para

with open(text, 'r') as file:
    para = file.read()

shift = 1
encoded_para = encode_para(para, shift)
print(encoded_para)

# Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

# Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
