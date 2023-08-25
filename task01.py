import random

text=""
with open('./news.txt', "r", encoding="utf-8") as f:
    text=f.read()


def hammer_task_0():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result
  
def memberOne():
    total_voice=0
    print_text=""
    for v in ['a','e','i','o','u']:
        num = text.count(v)
        print_text += 'The paragraph contains %i of %s.\n' %(num, v)
        total_voice += num
    print_text += 'The paragraph contains %i of voices letters.'%(total_voice)
    return print_text
  
def memberTwo():
    pass
  
def memberThree():
    pass
  
def memberFour():
    pass


if __name__ == "__main__":
    print(hammer_task_0())
    print(memberOne())
    print('call memberTwo() ')
    print('call memberThree() ')
    print('call memberFour() ')
   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
