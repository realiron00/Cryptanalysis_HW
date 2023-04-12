Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#-- Vigenere 암호화
def vigenere_encrypt(key, msg):
    result = ''
    key_list = list(key.upper())
    key_pos= 0
    for ch in msg:
        if ch.upper() in Alphabet:
            key_ch = Alphabet.find(key_list[key_pos])
            idx = Alphabet.find(ch.upper())
            if ch.isupper():
                result += Alphabet[(idx+key_ch)%26].upper()
            else:
                result += Alphabet[(idx+key_ch)%26].lower()
        else:
            result += ch
        key_pos = (key_pos + 1) % len(key)
    return result

#-- Vigenere 복호화
def vigenere_decrypt(key, msg):
    result = ''
    key_list = list(key.upper())
    key_pos= 0
    for ch in msg:
        if ch.upper() in Alphabet:
            key_ch = Alphabet.find(key_list[key_pos])
            idx = Alphabet.find(ch.upper())
            if ch.isupper():
                result += Alphabet[(idx-key_ch)%26].upper()
            else:
                result += Alphabet[(idx-key_ch)%26].lower()
        else:
            result += ch
        key_pos = (key_pos + 1) % len(key)
    return result