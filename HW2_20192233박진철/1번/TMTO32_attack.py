import TC20_lib as TC20
import pickle # 변수저장
import random # 난수생성
import copy   # deep copy 
import os,sys

#============================================================
#--- int(4bytes) to list 0x12345678 -> [ 0x12, 0x34, 0x56, 0x78 ]
def int2list(n):
    out_list = []
    out_list.append( (n >> 24) & 0xff )
    out_list.append( (n >> 16) & 0xff )
    out_list.append( (n >>  8) & 0xff )
    out_list.append( (n      ) & 0xff )

    return out_list

#--- list to int [ 0x12, 0x34, 0x56, 0x78 ] -> 0x12345678
def list2int(l):
    n = 0
    num_byte = len(l)
    for i in range(len(l)):
        n += l[i] << 8*(num_byte - i -1)
        
    return n

#- 변수를 파일에 저장하기
def save_var_to_file(var, filename):
    f = open(filename, 'w+b')
    pickle.dump(var, f)
    f.close()
    
#- 파일에서 변수를 가져오기
def load_var_from_file(filename):
    f = open(filename, 'rb')
    var = pickle.load(f)
    f.close()
    return var
#============================================================
key_bit = 32 

#----------------------
# Encryption key chain 만들기
#   SP = (24비트 랜덤키)
#   P0 = (선택평문, 고정값)    
#    t = 체인의 길이
def chain_EP(SP, P0, t):
    Xj = SP
    for j in range(0,t):
        ct = TC20.TC20_Enc(P0, Xj)
        Xj = ct  
    return Xj
#----------------------

#--------------
# 한개의 테이블에 대한 키 탐색 함수
def one_tmto_table_search(ct, P0, m, t, ell):
    key_candid_list = []
    file_name = 'tmto32_table/TMTO-' + str(ell) + '.dic'
    tmto_dic = load_var_from_file(file_name)

    Xj = ct
    current_j = t
    for idx in range(0,t):
        Xj_int = list2int(Xj)
        
        if Xj_int in tmto_dic: # Xj가 EP에 있는가?
            SP = int2list(tmto_dic[Xj_int]) # dic = { EP:SP }
            key_guess = chain_EP(SP, P0, current_j - 1)
            key_candid_list.append(key_guess)
        
        new_ct = TC20.TC20_Enc(P0,Xj)
        Xj = new_ct
        current_j = current_j - 1

    return key_candid_list
#--------------

#--------------
def attack(PT,num_of_tables):
    #찾아야 할 키 생성
    key=[random.randint(0,255), random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    C1=TC20.TC20_Enc(PT,key) #찾아야할 키로 PT를 암호화
    P2=[5,6,7,8] #key 후보들 중에서 정확한 키를 찾아줄 새로운 평문 생성
    C2=TC20.TC20_Enc(P2,key)
    print('key=',key)
    print('CT1=',C1)
    print('CT2=',C2)

    key_pool = [] #키 후보들
    print("TMTO Attack", end='')
    for ell in range(0, num_of_tables):
        key_list = one_tmto_table_search(C1, PT, m, t, ell)
        key_pool += key_list #key_pool에 후보키들이 들어감
        print('.', end='')
    print('Attack complete!')
    print('key_pool =', key_pool[0:4])

    final_key = [] #정확한 키
    for key in key_pool:
        ct_result = TC20.TC20_Enc(P2, key)
        if ct_result == C2: #C2와 후보키로 암호화한 ct_result가 같다면
            final_key.append(key) #후보키를 찾아야할 키로 결정

    print('Final key =', final_key) 
    if final_key:
        return True #키를 찾았다면, True를 반환
#--------------

# 선택평문 (TMTO 테이블 전체에서 고정된 값으로 사용)
PT = [1,2,3,4]
# 공격 파라미터 설정
m = 1024             # m: 한 테이블에 들어가는 체인의 개수
t = 1024             # t: 체인의 길이
num_of_tables = 1024 # 테이블 개수

counter=0 #성공 횟수
for i in range(100):
    print("attack ",i+1)
    chk=attack(PT,num_of_tables) #키를 찾았는지를 확인
    if chk==True:
        counter+=1 #키를 찾았다면, 성공 횟수에 추가
    print('counter=',counter,'\n')

print("성공 확률=", counter/100)