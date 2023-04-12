import VigenereLib
import os, sys
import EngDicLib
import caesar_funLib

"""
#1-(a)
in_file = "TEXT-1.txt"

InFileObj=open(in_file, 'rt', encoding='UTF8')
PT = InFileObj.read() #TEXT-1.txt 데이터를 PT에 저장
InFileObj.close()

key = 'KOOKMIN' #암호키: KOOKMIN
CT = VigenereLib.vigenere_encrypt(key, PT)
out_file = 'CIPHER-1.txt'
OutFileObj = open(out_file, 'w')
OutFileObj.write(CT) #암호문 CT를 CIPHER-1.txt에 저장
OutFileObj.close()
#=============================================
"""

#1-(b)
in_file = 'CIPHER-1.txt'
InFileObj = open(in_file)
CT = InFileObj.read() #CIPHER-1.txt 데이터를 CT에 저장
InFileObj.close()

MAX_KEY_LENGTH = 8 # 암호키의 최대길이
keylen_candidate = 0 #후보키의 길이
max_ic = 0.0 #영문일수록 높아짐
for key_len in range(1,MAX_KEY_LENGTH+1):
    sub_msg = ''
    idx = 0
    while idx < len(CT):
        sub_msg += CT[idx] #키 길이만큼의 간격으로 암호문을 sub_msg에 저장
        idx += key_len
    sub_ic = EngDicLib.IC(sub_msg) #키 길이만큼의 간격으로 저장된 암호문의 IC값 계산
    if max_ic < sub_ic:
        max_ic = sub_ic
        keylen_candidate = key_len #IC값이 가장 높을때의 키길이를 후보키의 길이로 설정
    print('key_len =', key_len, ':', end='')
    print('sub_msg', sub_msg[:10],"...", '( length =', len(sub_msg), ')\t', end='')
    print('IC(sub_msg)= %6.4f' %(sub_ic))
    
print('-------------------------------------')
    
key_list = [0]*keylen_candidate
for key_pos in range(1,keylen_candidate):
    key_ch_candidate = 0
    max_ic = 0.0
    for key_ch in range(0,26):
        sub_msg = ''
        idx = 0
        while idx < len(CT):
            sub_msg += CT[idx] #키의 첫번째 글자와의 차이값만큼의 간격으로 암호문을 sub_msg에 저장
            if (idx+key_pos) < len(CT):
                sub_msg += caesar_funLib.caesar_dec(key_ch, CT[idx+key_pos])
            idx += keylen_candidate
        sub_ic = EngDicLib.IC(sub_msg)
        if max_ic < sub_ic:
            max_ic = sub_ic
            key_ch_candidate = key_ch #IC값이 가장 높을때의 값을 키 첫 글자와의 상대적 거리로 설정
    key_list[key_pos] = key_ch_candidate
    print('key[%d] : key_ch_candidate = %d' %(key_pos, key_ch_candidate))

print('-------------------------------------')
    
for key_ch in range(0,26):
    dec_msg = ''
    key_pos= 0
    for ch in CT: #키의 첫번째 값을 A~Z로 설정
        key_now = (key_ch + key_list[key_pos]) % 26
        dec_msg += caesar_funLib.caesar_dec(key_now, ch)
        key_pos = (key_pos + 1) % keylen_candidate
    eng_percent = EngDicLib.percentEngWords(dec_msg) 
    #후보키로 복호화한 문장에 영단어가 얼마나 있는지 계산

    print('key_ch =', key_ch, ':', end='')
    print('dec_msg', dec_msg[:10],"...", '( length =', len(dec_msg), ')\t', end='')
    print('Eng(dec_msg)= %5.2f %%' %(eng_percent*100))
    
    if EngDicLib.isEnglish(dec_msg):
        key_0_candidate, rightPT = key_ch, dec_msg

if key_0_candidate >= 0:
    rightkey = ''
    for idx in key_list:
        rightkey += VigenereLib.Alphabet[(key_0_candidate + idx) % 26]
    
    print('right key =', rightkey)
    print('PT = ', rightPT[:20], '...', rightPT[-10:])
#=============================================