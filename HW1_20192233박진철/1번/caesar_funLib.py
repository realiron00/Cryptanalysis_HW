"""
암호분석 - Caesar 암호 함수 라이브러리: caesarLib
    -caesar_enc(key, PT)
    -caesar_dec(key, CT)
"""

UpAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LowAlphabet = 'abcdefghijklmnopqrstuvwxyz'

#암호화함수
def caesar_enc(key, PT):
    CT = ''
    for ch in PT:
        if ch in UpAlphabet:
            new_idx = (UpAlphabet.find(ch) + key) % 26
            CT = CT + UpAlphabet[new_idx]
        elif ch in LowAlphabet:
            new_idx = (LowAlphabet.find(ch) + key) % 26
            CT = CT + LowAlphabet[new_idx]
        else:
            CT = CT + ch #대문자, 소문자가 아니면, 그대로 추가한다.
    return CT

#복호화함수
def caesar_dec(key, CT):
    #주어진 암호문 CT를 복호화하여 DT 만들기
    DT = ''
    for ch in CT:
        if ch in UpAlphabet:
            new_idx = (UpAlphabet.find(ch) - key) % 26
            DT = DT + UpAlphabet[new_idx]
        elif ch in LowAlphabet:
            new_idx=(LowAlphabet.find(ch) - key) % 26
            DT = DT + LowAlphabet[new_idx]
        else:
            DT = DT + ch
    return DT

def main():    
    #함수를 이용한 메시지 암복호화
    msg = 'This is a plaintext to be encrypted'
    caesar_key = 3 #암호키
    msgCT = caesar_enc(caesar_key, msg)
    print('msg=',msg)
    print('msgCT=',msgCT)
    
    msgDT=caesar_dec(caesar_key, msgCT)
    print('msgDT=',msgDT)
    

#라이브러리를 실행하면 main함수가 호출되고
# import 하여 사용할 때는 main함수가 실행되지 않게 하자
if __name__ =="__main__": #__는 밑줄 2개임!!!
    main()