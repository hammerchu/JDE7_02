import random

text = r"C:\Users\user\Desktop\git\JDE7_02\news.txt"
# f = open(text, "r")
# print(f.read())


def hammer_task_0():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result
  
def JasonTSOI():
    with open(text, "r") as f:
        news = f.read()

        lines = news.split('\n')
        reversed_lines = [' '.join(word[::-1] for word in line.split()) for line in lines]
        return '\n'.join(reversed_lines)
  
def memberTwo():
    pass
  
def memberThree():
    pass
  
def memberFour():
    pass


if __name__ == "__main__":
    print(hammer_task_0())
    print(JasonTSOI())
    print('call memberTwo() ')
    print('call memberThree() ')
    print('call memberFour() ')
   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
