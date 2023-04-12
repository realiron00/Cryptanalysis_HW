"""
암호분석 - 영어사전 라이브러리
"""
import os, sys

#영어 대문자
UpAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#영어 대소문자, 공백, 탭, 엔터
letters_and_space = UpAlphabet + UpAlphabet.lower() + ' \t\n'

#===사전 데이터 타입 (key, value) 예: (apple, 사과)
'''
myDic = { 'DES':64, 'AES':128 }
print(myDic)
print(myDic['DES'])
myDic['ARIA'] = 128
print(myDic)
'''

#--영어사전 파일 읽어 --> 사전 변수 만들기
def loadDic():
    dic_file = open('EngDic.txt')
    # 파일이 없으면 오류...
    if not os.path.exists('EngDic.txt'):
       print("File not found error.")
       sys.exit()
    EngWords = {} #빈 사전
    contents = dic_file.read()
    contents_list = contents.split('\n')
    #print(contents[0:30])
    #print(contents_list[0:5])
    for word in contents_list:
        #EngWords[word] = None
        EngWords[word] = len(word)
    #print(Engwords)
    dic_file.close()
    return EngWords

EnglishDic = loadDic() #영어사전 변수 (전역변수)
    
#대소문자, 공백, 탭, 리턴만 남기기
def removeNonletters(msg):
    letter_list = []
    for ch in msg:
        if ch in letters_and_space:
            letter_list.append(ch)
    return ''.join(letter_list) #리스트를 문자열로

#복호화한 문서에서 영어단어의 비율
def percentEngWords(msg):
    msg = msg.lower()
    msg = removeNonletters(msg)
    possibl_words = msg.split() #문자열을 리스트로
    if possibl_words == []: #0으로 나누기 방지
        return 0.0
    count_words = 0
    for word in possibl_words:
        if word in EnglishDic: #사전에 있는 단어인가?
            count_words +=1
    return float(count_words)/len(possibl_words)

#영어인지 판정하기
def isEnglish(msg, wordPer=20, letterPer=80):
    wordMatch = percentEngWords(msg)*100 >= wordPer
    
    numletters = len(removeNonletters(msg))
    messageLettersPer = float(numletters)*100/len(msg)
    
    letterMatch = messageLettersPer >= letterPer
    
    return wordMatch and letterMatch

#IC: Index of Coincidence
def IC(msg):
    AlphaDic = {}
    for ch in UpAlphabet:
        AlphaDic[ch] = 0
    num_alpha = 0
    for ch in msg:
        if ch.upper() in UpAlphabet:
            AlphaDic[ch.upper()] +=1
            num_alpha += 1
    ic = 0
    for ch in UpAlphabet:
        ic += AlphaDic[ch] * (AlphaDic[ch]-1)
    ic /= num_alpha*(num_alpha-1)
    return ic
        

def main():
    msg1 = 'Caesar cipher is not secure.'
    print('msg1 =', msg1[:20])
    print(percentEngWords(msg1))
    print('msg1 is English:', isEnglish(msg1))
    print('msg1: index of coincidence:', IC(msg1))
    
if __name__ == '__main__':
    main()
    
    