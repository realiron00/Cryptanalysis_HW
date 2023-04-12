#2-(a)
Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#단순치환암호 암호화
def subst_encrypt(key, msg):
    result = ''
    InSet = Alphabet
    OutSet = key
    for ch in msg:
        if ch.upper() in InSet:
            idx = InSet.find(ch.upper())
            if ch.isupper():
                result += OutSet[idx].upper()
            else:
                result += OutSet[idx].lower()
        else:
            result += ch
        #메시지에서 알파벳 위치의 문자를 동일한 위치의 키값으로 변경
    return result


#단순치환암호 복호화
def subst_decrypt(key, msg):
    result = ''
    InSet = key
    OutSet = Alphabet
    for ch in msg:
        if ch.upper() in InSet:
            idx = InSet.find(ch.upper())
            if ch.isupper():
                result += OutSet[idx].upper()
            else:
                result += OutSet[idx].lower()
        else:
            result += ch
        #메시지에서 키값 위치의 문자를 동일한 위치의 알파벳으로 변경
    return result
#=============================================