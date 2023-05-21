import TC20_lib as TC20
import pickle # 변수저장
import random # 난수생성
import copy   # deep copy 
import os,sys
from matplotlib import pyplot as plt

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
# chain에서 암호키들을 리스트에 저장
def chain_EP(SP, P0, t):
    key_list=[]
    Xj = SP
    for j in range(0,t):
        key_list.append(Xj)
        ct = TC20.TC20_Enc(P0, Xj)
        Xj=ct
    return key_list
#----------------------

#--------------------------------
# 한개의 테이블에서 얻어지는 모든 암호키를 리스트로 저장
#저장한 암호키를 이용하여 한개의 테이블의 ECR 반환
def make_one_tmto_table(P0, m, t, ell):
    table_list = []
    table_dic={}
    for i in range(0,m): 
        # 랜덤한 시작점
        SP = [random.randint(0,255), random.randint(0,255), random.randint(0,255), random.randint(0,255) ]
        key_list=chain_EP(SP,P0,t)
        for i in range(0,len(key_list)):
            table_list.append(key_list[i])
    for i in range(0,len(table_list)):
        key_int=list2int(table_list[i])
        table_dic[key_int]=i
    H=len(table_dic)
    ECR=H/(m*t)
    return ECR
#--------------------------------

#---------------------
# TMTO 테이블 전체 만들기
# 입력:
#   P0: 고정평문 
#   m: 행(row)의 개수 (체인의 개수)
#   t: 열(col)의 개수 (체인의 길이)
#   num_of_tables: TMTO 테이블 개수 (=256)   
def make_all_tmto_tables(P0, m, t, num_of_tables):
    print('making TMTO tables', end='')
    a=[]
    ECR_list=[]
    for ell in range(0, num_of_tables):
        ECR=make_one_tmto_table(P0,m,t,ell)
        ECR_list.append(ECR)
        print('.',end='')
    
    print('\n All TMTO tables are created.')
    return ECR_list
#---------------------

# 선택평문 (TMTO 테이블 전체에서 고정된 값으로 사용)
PT = [1,2,3,4]
# 공격 파라미터 설정
m = 1024             # m: 한 테이블에 들어가는 체인의 개수
t = 1024             # t: 체인의 길이
num_of_tables = 10 # 테이블 개수

ECR=make_all_tmto_tables(PT, m, t, num_of_tables)
print('ECR=',ECR)

x=[i for i in range(1,1025)]
y=ECR
"""
plt.ylim(0,1)
plt.xlim(1,1024)
plt.plot(x,y)
plt.show()
"""
ECR_sum=0
print(len(ECR))
for i in range(0,len(ECR)):
    ECR_sum+=ECR[i]
print("ECR 평균=",ECR_sum/len(ECR))
