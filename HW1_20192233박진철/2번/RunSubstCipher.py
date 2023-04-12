import random
import SubstLib

UpAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#2-(b)
def randomkey(msg):
    alpha_list = list(msg)
    random.shuffle(alpha_list) #26개의 대문자를 랜덤하게 섞음
    shuffled = ''.join(alpha_list)
    return shuffled

def findright(msg):
    for i in range(0, len(msg)):
        for j in range(i+1, len(msg)):
            if msg[i] == msg[j]:
                return False
            else:
                return True
#=============================================

#2-(c)
in_file = "TEXT-1.txt"

InFileObj=open(in_file, 'rt', encoding='UTF8')
PT = InFileObj.read()
InFileObj.close()

key = randomkey(UpAlphabet) #랜덤하게 섞인 값을 키로 설정

if findright(key) == True: #유효한 키 값이라면, 암호화
    CT = SubstLib.subst_encrypt(key, PT)
    out_file = 'CIPHER-3.txt'
    OutFileObj = open(out_file, 'w')
    OutFileObj.write(CT)
    OutFileObj.close()
else: #유효하지 않은 키값이라면, 오류메시지 출력
    print('InValued key')
#=============================================

#2-(d)
def getLetterCount(message):
    letterCount = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0,
                   'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0,
                   'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0,
                   'Y':0, 'Z':0}
    for char in message.upper():
        if char in UpAlphabet:
            letterCount[char] += 1
    return letterCount

#배열의 첫번째 원소를 주는 함수
def getItemAtIndexZero(items):
    return items[0]

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ' #영문자 빈도 순서

def findfreq(message):
    letter2freq = getLetterCount(message) #메시지의 빈도 사전 만들기
    
    #사전 반대로 바꾸기
    freq2letter = {}
    for char in UpAlphabet:
        if letter2freq[char] not in freq2letter:
            freq2letter[letter2freq[char]] = [char]
        else:
            freq2letter[letter2freq[char]].append(char)
    
    #동일한 출현빈도인 문자들을 정렬        
    for freq in freq2letter:
        freq2letter[freq].sort(key=ETAOIN.find, reverse=False)
        #작은 값을 앞쪽에 정렬
        freq2letter[freq] = ''.join(freq2letter[freq])
    
    
    freqPairs = list(freq2letter.items()) #사전을 리스트로 전환
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)
    #배열의 첫번째 값을 기준으로 정렬
    
    #빈도순서를 문자열로 바꾸기
    freqOrder = []
    for freq_pair in freqPairs:
        freqOrder.append(freq_pair[1])
        freq_order_str = ''.join(freqOrder)
        
    return freq_order_str #빈도순서를 반환

print('Key=', key)

CTfreq=findfreq(CT)
print('CT frequency=', CTfreq)

PTfreq=findfreq(PT)
print('PT frequency=', PTfreq)
