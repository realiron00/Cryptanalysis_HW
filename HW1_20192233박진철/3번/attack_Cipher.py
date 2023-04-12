#1. 파일에서 암호문 받아오기
in_file = "CIPHER-2.txt"
InFileObj=open(in_file, 'rt', encoding='UTF8')
CT = InFileObj.read()
InFileObj.close()
#=============================================

#2. 임의의 키 설정
my_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#=============================================

#3. 빈도수 조사
UpAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def getLetterCount(message):
    letterCount = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0,
                   'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0,
                   'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0,
                   'Y':0, 'Z':0}
    for char in message.upper():
        if char in UpAlphabet:
            letterCount[char] += 1
    return letterCount

def getItemAtIndexZero(items):
    return items[0]

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

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

CTfreq = findfreq(CT)
print('CT frequency=', CTfreq)
#=============================================

#4. 빈도를 통해 E 찾기
CTL = CT.upper()
#암호된 부분은 대문자, 복호화된 부분은 소문자로 구분함

my_key = my_key.replace('E', CTfreq[0].lower())
#가장 빈도수가 높은 알파벳을 e로 변경

CTL = CTL.replace(CTfreq[0], 'e')
#암호문에서 빈도수가 높은 알파벳을 e로 변경

#print(CTL)
#=============================================

#5. the 찾기
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
#=============================================

#6. to 찾기
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

#7. of 찾기
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

#8. theWe HWe thWee라는 문장 발견
#W->r, H->a로 바꾸면 there are three라는 자연스러운 문장이 됨
my_key = my_key.replace('R', 'w')
my_key = my_key.replace('A', 'h')

CTL = CTL.replace('W', 'r')
CTL = CTL.replace('H', 'a')
#print(CTL)
#=============================================

#9. and 찾기
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

#10. Yhat doeN a XrDFtanaGDNt do?라는 문장 발견
#Y->w, N->s로 바꾸면 what does a XrDFtanaGDst do?라는 자연스러운 문장이 됨
my_key = my_key.replace('W', 'y')
my_key = my_key.replace('S', 'n')

CTL = CTL.replace('Y', 'w')
CTL = CTL.replace('N', 's')
#print(CTL)
#=============================================
#11. Vnown, Xhosen, wZth이라는 단어가 자주 보임
#V->k, X->c, Z->i로 바꾸면 known, chosen, with이라는 자연스러운 단어가 됨
my_key = my_key.replace('K', 'v')
my_key = my_key.replace('C', 'x')
my_key = my_key.replace('I', 'z')

CTL = CTL.replace('V', 'k')
CTL = CTL.replace('X', 'c')
CTL = CTL.replace('Z', 'i')
#print(CTL)
#=============================================

#12. wiGG aGso aGGow라는 문장 발견
#G->l로 바꾸면 will also allow라는 자연스러운 단어가 됨
my_key = my_key.replace('L', 'g')

CTL = CTL.replace('G', 'l')
#print(CTL)
#=============================================

#13. ciFherteEt/FlainteEt라는 단어 발견
#F->p, E->x로 바꾸면 ciphertext/plaintext라는 자연스러운 단어가 됨
my_key = my_key.replace('P', 'f')
my_key = my_key.replace('X', 'e')

CTL = CTL.replace('F', 'p')
CTL = CTL.replace('E', 'x')
#print(CTL)
#=============================================

#14. crDptanalDst라는 단어 발견
#D->y로 바꾸면 cryptanalyst라는 자연스러운 단어가 됨
my_key = my_key.replace('Y', 'd')

CTL = CTL.replace('D', 'y')
#print(CTL)
#=============================================

#15. 남은 단어들 확인
CTLslice=CTL.split()
lea_word=[]
for char in CTLslice:
    if char.islower() == False:
        lea_word.append(char)
    #대문자가 하나라도 있는 단어를 찾음

count_lword={}
for i in lea_word:
    try: count_lword[i] += 1
    except: count_lword[i]=1
    #찾은 단어들의 등장횟수를 사전 형태로 저장
print('remain word=',count_lword)
#=============================================

#16. decodinI, receiOer, UessaIe라는 단어 발견
#I->g, O->v, U->m으로 바꾸면 decoding, receiver, message라는 자연스러운 단어가 됨
my_key = my_key.replace('G', 'i')
my_key = my_key.replace('V', 'o')
my_key = my_key.replace('M', 'u')

CTL = CTL.replace('I', 'g')
CTL = CTL.replace('O', 'v')
CTL = CTL.replace('U', 'm')
#print(CTL)
#=============================================

#17. analyLing, inclRding, can Je라는 단어 발견
#L->z, R->u, J->b로 바꾸면 analyzing, including, can be라는 자연스러운 단어가 됨
my_key = my_key.replace('Z', 'l')
my_key = my_key.replace('U', 'r')
my_key = my_key.replace('B', 'j')

CTL = CTL.replace('L', 'z')
CTL = CTL.replace('R', 'u')
CTL = CTL.replace('J', 'b')
#print(CTL)
#=============================================

#18. 남은 키 찾기
new_key=my_key.upper()
othkey='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for ch in new_key:
    for i in UpAlphabet:
        if ch==i:
            othkey=othkey.replace(ch, '')
    #my_key에 아직 찾지 못한 알파벳을 othkey에 저장
        
ncha_key=[]
for ch in my_key:
    if ch.isupper()==True:
        ncha_key.append(ch)
        #my_key에서 대문자로 되어있는 알파벳을 ncha_key에 저장
            
print('remainkey=', othkey)
print('n_changedkey=', ncha_key)
print('my_key=', my_key)
#=============================================

#19. 남은 영단어 찾기
CTLslice=CTL.split()
engwords=[]
for char in CTLslice:
    if char.islower() == False:
        engwords.append(char)

engdic={}
for i in engwords:
    try: engdic[i] += 1
    except: engdic[i]=1
print('remainword=', engdic)
#=============================================

#20. 임의로 키 설정하기
#남은 것들은 또 다른 암호문에 있는 것들 뿐
#임의로 B->j, C->q로 변경
my_key = my_key.replace('J', 'b')
my_key = my_key.replace('Q', 'c')

CTL = CTL.replace('B', 'j')
CTL = CTL.replace('C', 'q')

#print(CTL)
print('key=',my_key)
print(CTL)