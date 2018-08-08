import sys 
import math
import string

def read_file(f_name):
    f = open(f_name, 'r')
    text = f.read().rstrip()

    return text

def format_date(date):
    new_date = date.replace('/', '')
    return new_date

def rot(letter, shift_value):
    return chr(ord('a') + ((ord(letter) - ord('a')) - shift_value)%26)

def decipher_text(text,date):
    date_str = date * math.floor((len(text)/len(date))) + date[:len(text)%len(date)]
    new_text = ''
    
    for i, c in enumerate(date_str):
        new_letter = rot(text[i], int(c))
        new_text += new_letter

    print(new_text)

def run():
    if len(sys.argv) == 3:
        date = format_date(sys.argv[1]) 
        text = read_file(sys.argv[2])
        decipher_text(text,date)
    else :
        print('Missing Arguments!')

run()