def read_file():
    f = open('msg.sec', 'r')
    text = f.read().rstrip()

    return text[:60].lower()

def rot(letter, key):
    return chr(ord('a') + ((ord(letter) - ord('a')) - key)%26) if letter.isalpha() else letter

def decrypt_text(text):
    new_text = ''
    
    for i in range(26): 
        for j in text:
            new_letter = rot(j, int(i)) 
            new_text += new_letter
        print(i, ' ' + new_text + ' ')
        new_text = ''


def run():
    text = read_file()
    decrypt_text(text)

run()