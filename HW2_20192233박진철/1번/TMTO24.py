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

key_bit = 24 # 키공간 24비트 key = [0,*,*,*]
#----------------------
# 암호문(32비트)을 다음 단계 암호키(24비트)로 만드는 함수
# R: 32비트 -> 24비트 
def R(ct):
    #next_key = ct
    next_key = copy.deepcopy(ct)
    next_key[0] = 0
    return next_key
#----------------------

#----------------------
# Encryption key chain 만들기
#   SP = (24비트 랜덤키)
#   P0 = (선택평문, 고정값)    
#    t = 체인의 길이
def chain_EP(SP, P0, t):
    Xj = SP
    for j in range(0,t):
        ct = TC20.TC20_Enc(P0, Xj)
        Xj = R(ct)   # next Xj (출력 암호문 32비트를 암호키 24비트로)
    return Xj
#----------------------

#--------------------------------
# TMTO 테이블 한개 만들기 (번호=ell)
# 입력:
#      P0: 선택(고정)평문
#       m: #SP (행의 개수)    m=2^8: SP1 ~ SP2^8
#       t: 체인의 길이(열)    j=0, ... , j=t
#     ell: 테이블 번호        ell = 0 ~ 255
# 출력: 
#    사전    : { (Key=EP, Value=SP) }    
#    저장위치: ./tmto_table/TMTO-ell.dic
def make_one_tmto_table(P0, m, t, ell):
    tmto_dic = {}  # (SP,EP), 정렬기준 EP (EP를 검색하기 위해)
    for i in range(0,m): 
        # 랜덤한 시작점
        SP = [0, random.randint(0,255), random.randint(0,255), random.randint(0,255) ]
        EP = chain_EP(SP, P0, t)  
        
        # 정수로 만들어 (SP, EP)를 사전에 넣는다 { (Key=EP, Value=SP) }
        SP_int = list2int(SP)
        EP_int = list2int(EP)
        tmto_dic[EP_int] = SP_int
    # 만든 테이블 사전을 파일로 저장한다
    # 파일명: TMTO-0, TMTO-1, ... , TMTO-255
    file_name = 'tmto24_table/TMTO-' + str(ell) + '.dic'
    save_var_to_file(tmto_dic, file_name)
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
    for ell in range(0, num_of_tables):
        make_one_tmto_table(P0, m, t, ell)
        print('.', end='')
    print('\n All TMTO tables are created.')
#---------------------

# 선택평문 (TMTO 테이블 전체에서 고정된 값으로 사용)
PT = [1,2,3,4]
# 공격 파라미터 설정
m = 256             # m: 한 테이블에 들어가는 체인의 개수
t = 256             # t: 체인의 길이
num_of_tables = 256 # 테이블 개수

make_all_tmto_tables(PT, m, t, num_of_tables)