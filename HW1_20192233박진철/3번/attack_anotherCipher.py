import os, sys

in_file = "AnotherCipher.txt"
InFileObj=open(in_file, 'rt', encoding='UTF8')
CT = InFileObj.read()
InFileObj.close()

my_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #임의의 키

UpAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 

#==============================================
#빈도 수 조사 함수
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

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

#빈도순서를 문자열로 정렬해주는 함수
def findfreq(message):
    letter2freq = getLetterCount(message)
    freq2letter = {}
    for char in UpAlphabet:
        if letter2freq[char] not in freq2letter:
            freq2letter[letter2freq[char]] = [char]
        else:
            freq2letter[letter2freq[char]].append(char)
            
    for freq in freq2letter:
        freq2letter[freq].sort(key=ETAOIN.find, reverse=False)
        freq2letter[freq] = ''.join(freq2letter[freq])
    freqPairs = list(freq2letter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)
    freqOrder = []
    for freq_pair in freqPairs:
        freqOrder.append(freq_pair[1])
        freq_order_str = ''.join(freqOrder)
    return freq_order_str

#남은 단어들 확인하는 함수
def checkremainword(msg):
    msgslice=msg.split()
    lea_word=[]
    for char in msgslice:
        if char.islower() == False:
            lea_word.append(char)
            
    count_lword={}
    for i in lea_word:
        try: count_lword[i] += 1
        except: count_lword[i]=1
    #찾은 단어들의 등장횟수를 사전 형태로 저장
    print('remain word=',count_lword)
#==============================================

CTfreq = findfreq(CT) #CT의 빈도순서
print('CT frequency=', CTfreq)

CTL=CT.upper()

#21-3. e 찾기
my_key = my_key.replace('E', CTfreq[1].lower())

CTL = CTL.replace(CTfreq[1], 'e')
#==============================================

#21-4. the 찾기
CTLslice=CTL.split()

findxxe=[]
for char in CTLslice:
    if 'e' in char:
        if len(char) == 3: #e가 들어있고, 글자가 3개인 단어들을 선택
            findxxe.append(char)

countxxe={}
for i in findxxe:
    try: countxxe[i] += 1
    except: countxxe[i]=1
print('find the=', countxxe) #선택된 단어들의 등장 횟수를 사전형태로 저장

max_xxe=max(countxxe, key=countxxe.get) #가장 많이 나온 단어 찾기

my_key = my_key.replace('T', max_xxe[0].lower())
my_key = my_key.replace('H', max_xxe[1].lower())

CTL = CTL.replace(max_xxe[0], 't')
CTL = CTL.replace(max_xxe[1], 'h')
#print(CTL)
#==============================================

#21-5. to 찾기
CTLslice=CTL.split()
findtx=[]
for char in CTLslice:
    if 't' in char:
        if len(char) == 2:
            findtx.append(char)
            
counttx={}
for i in findtx:
    try: counttx[i] += 1
    except: counttx[i]=1
print('find to=', counttx)

max_tx=max(counttx, key=counttx.get)
my_key = my_key.replace('O', max_tx[1].lower())

CTL = CTL.replace(max_tx[1], 'o')
#print(CTL)
#=============================================

#21-6. of 찾기
CTLslice=CTL.split()
findox=[]
for char in CTLslice:
    if 'o' in char:
        if len(char) == 2 and 't' not in char :
            findox.append(char)
            
countox={}
for i in findox:
    try: countox[i] += 1
    except: countox[i]=1
print('find of=',countox)

max_ox=max(countox, key=countox.get)
my_key = my_key.replace('F', max_ox[1].lower())

CTL = CTL.replace(max_ox[1], 'f')
#print(CTL)
#=============================================

#21-7. theWe YWe라는 문장 발견
#W->r, Y->a로 바꾸면 there are라는 자연스러운 문장이 됨
my_key = my_key.replace('R', 'w')
my_key = my_key.replace('A', 'y')

CTL = CTL.replace('W', 'r')
CTL = CTL.replace('Y', 'a')
#print(CTL)
#=============================================

#21-8. and 찾기
CTLslice=CTL.split()
findaxx=[]
for char in CTLslice:
    if 'a' in char:
        if len(char) == 3:
            findaxx.append(char)
            
countaxx={}
for i in findaxx:
    try: countaxx[i] += 1
    except: countaxx[i]=1
print('find and=', countaxx)

max_axx=max(countaxx, key=countaxx.get)
my_key = my_key.replace('N', max_axx[1].lower())
my_key = my_key.replace('D', max_axx[2].lower())

CTL = CTL.replace(max_axx[1], 'n')
CTL = CTL.replace(max_axx[2], 'd')
#print(CTL)
#=============================================

#21-9. 자연스러운 단어/문장 만들기
#doDnIoadaAIe라는 단어 발견
#D->w, I->l, A->b로 바꾸면 downloadable라는 자연스러운 단어가 됨
my_key = my_key.replace('W', 'd')
my_key = my_key.replace('L', 'i')
my_key = my_key.replace('B', 'a')

CTL = CTL.replace('D', 'w')
CTL = CTL.replace('I', 'l')
CTL = CTL.replace('A', 'b')

#thLO LO라는 문장 발견
#L->i, O->s로 바꾸면 this is라는 자연스러운 문장이 됨
my_key = my_key.replace('I', 'l')
my_key = my_key.replace('S', 'o')

CTL = CTL.replace('L', 'i')
CTL = CTL.replace('O', 's')

#Han be Vsed라는 문장 발견
#H->c, V->u로 바꾸면 can be used라는 자연스러운 문장이 됨
my_key = my_key.replace('C', 'h')
my_key = my_key.replace('U', 'v')

CTL = CTL.replace('H', 'c')
CTL = CTL.replace('V', 'u')
print(CTL)
#=============================================

#21-10. 남은 단어로 유추하기
checkremainword(CTL)

#ciThers, includinU, decrZTtion, attacXs라는 단어 발견
#T->p, U->g, Z->y, X->k로 바꾸면 
#ciphers, including, decryption, attacks라는 자연스러운 단어가 됨
my_key = my_key.replace('P', 't')
my_key = my_key.replace('G', 'u')
my_key = my_key.replace('Y', 'z')
my_key = my_key.replace('K', 'x')

CTL = CTL.replace('T', 'p')
CTL = CTL.replace('U', 'g')
CTL = CTL.replace('Z', 'y')
CTL = CTL.replace('X', 'k')

checkremainword(CTL)

#Eessage, freSuency, seBeral, boCentriS라는 단어 발견
#E->m, S->q, B->v, C->x로 바꾸면 
#message, frequency, several, boxentriq라는 자연스러운 단어가 됨
my_key = my_key.replace('M', 'e')
my_key = my_key.replace('Q', 's')
my_key = my_key.replace('V', 'b')
my_key = my_key.replace('X', 'C')

CTL = CTL.replace('E', 'm')
CTL = CTL.replace('S', 'q')
CTL = CTL.replace('B', 'v')
CTL = CTL.replace('C', 'x')

checkremainword(CTL)

out_file = 'anotherPT.txt'
if os.path.exists(out_file):
    print("Overwrite ? (Y/N) > ")
    response = input()
    if not (response == 'Y'):
        sys.exit()
        
outfile_object = open(out_file, 'w')
outfile_object.write(CTL)
outfile_object.close()

"""
#1. 빈도를 통해 E 찾기
my_key = my_key.replace('E', CTfreq[0].lower())
#가장 빈도수가 높은 알파벳을 e로 변경

CTL = CTL.replace(CTfreq[0], 'e')
#암호문에서 빈도수가 높은 알파벳을 e로 변경

#print(CTL)
#=============================================

#2. the 찾기
CTLslice=CTL.split()

findxxe=[]
for char in CTLslice:
    if 'e' in char:
        if len(char) == 3: #e가 들어있고, 글자가 3개인 단어들을 선택
            findxxe.append(char)

countxxe={}
for i in findxxe:
    try: countxxe[i] += 1
    except: countxxe[i]=1
print('find the=', countxxe) #선택된 단어들의 등장 횟수를 사전형태로 저장

max_xxe=max(countxxe, key=countxxe.get) #가장 많이 나온 단어 찾기

my_key = my_key.replace('T', max_xxe[0].lower())
my_key = my_key.replace('H', max_xxe[1].lower())

CTL = CTL.replace(max_xxe[0], 't')
CTL = CTL.replace(max_xxe[1], 'h')
print(CTL)
print(my_key)
#=============================================
"""