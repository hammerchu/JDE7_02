import random

text=""
with open('./news.txt', "r", encoding="utf-8") as f:
    text=f.read()
  
def memberOne(shift_value, all=False):
    #convert to ascii
    print_text = ""
    for char in text:
        ascii_value = ord(char) + shift_value
        if all == True:
            print_text += chr(ascii_value%128)
        else:
            def ascii_range(ascii):
                if 65 <= ascii <= 90:
                    return 1
                elif 97 <= ascii <= 122:
                    return 2
                return 0
            asc=ord(char)
            if ascii_range(asc) != 0:
                if ascii_range(asc + shift_value) == ascii_range(asc):
                    print_text += chr(asc + shift_value)
                else:
                    asc = [0,65,97][ascii_range(asc)]
                    print_text += chr(asc)
            else:
                print_text += char
       
    return print_text


if __name__ == "__main__":
    print(memberOne(1, ))
