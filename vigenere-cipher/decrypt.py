# -*- coding: utf-8 -*-
def read_file(f_name):
    f = open(f_name, 'r')
    text = f.readlines()

    return ''.join(text)

def rot(letter, letter_key, my_dict):
    alphabet = {}
    alphabet_ = {}
    for a, b in enumerate(my_dict):
        alphabet[b] = a
        alphabet_[a] = b

    if letter in my_dict:
        return alphabet_[(alphabet[letter] - alphabet[letter_key])%len(alphabet)]
    else:
        return letter

def encrypt_text(text,key):
    my_dict = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    new_text = '' 
    j = 0

    for i,c in enumerate(text):
        j = j if c in my_dict else j - 1
        index = j%len(key) 
        new_letter = rot(c,key[index],my_dict)
        new_text += new_letter  
        j += 1

    return new_text

def run():
    text = read_file('musica.sec')
    result_str = encrypt_text(text,'Despacito') 

    print(result_str)

if __name__ == '__main__':
    run()



