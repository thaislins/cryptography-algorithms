# -*- coding: utf-8 -*-

def read_file(f_name):
    f = open(f_name, 'r')
    text = f.read().rstrip().upper()

    return text

def rot(letter, letter_key):
    if ord('A') <= ord(letter) <= ord('Z'):    
        return chr(ord('A') + ((ord(letter) - ord(letter_key))%26))
    else:
        return letter

def decrypt_text(text, key):
    new_text = '' 
    j = 0

    for i,c in enumerate(text):
        j = j if c.isalpha() else j - 1
        index = j%len(key) 
        new_letter = rot(text[i],key[index])
        new_text += new_letter  
        j += 1

    print(new_text)

def run():
    text = read_file('msg.sec')
    decrypt_text(text, 'DESPACITO')

if __name__ == '__main__':
    run()



