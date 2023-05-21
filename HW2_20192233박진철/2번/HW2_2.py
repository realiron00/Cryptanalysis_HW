import TC20_lib as TC20
import pickle # 변수저장
import random # 난수생성
import copy   # deep copy 
import os,sys

#- 파일에서 변수를 가져오기
def load_var_from_file(filename):
    f = open(filename, 'rb')
    var = pickle.load(f)
    f.close()
    return var

def Extract_RK(P,C):
    out1=[0,0,0,0]
    out2=[0,0,0,0]
    key=[0,0,0,0]

    out1=TC20.LM(C)
    out2=TC20.ISB(out1)
    key=TC20.AR(P,out2)

    return key

'''
PT=[1,2,3,4]
key=[5,6,7,8]
CT=TC20.Enc_Round(PT,key)
find_RK=Extract_RK(PT,CT)
print("Round key=",find_RK)
'''

def IsSlidPair(P1,C1,P2,C2):
    key=Extract_RK(P1,P2)
    if C2==TC20.Enc_Round(C1,key):
        return True
    else: 
        return False
    
'''
key=[5,6,7,8]
PT1=[0,1,2,3]
CT1=TC20.TC20_Enc(PT1,key)
PT2=TC20.Enc_Round(PT1,key)
CT2=TC20.TC20_Enc(PT2,key)
print(IsSlidPair(PT1,CT1,PT2,CT2))
'''

file_name = 'known_ptct.var'
item= load_var_from_file(file_name)

right_key=[]

for i in range(len(item)):
    print("attack ",i+1)
    print(item[i])
    for j in range(0,i):
        if IsSlidPair(item[i][0],item[i][1],item[j][0],item[j][1])==True:
            #Slid 쌍인지 확인
            print("find key!")
            right_key=Extract_RK(item[i][0],item[j][0])
            #Slid Pair라면, 라운드 키값을 획득
            break
    if right_key:
        break
    else:
        print("didn't find slide pair")

print("key=",right_key)

'''
ran_int=random.randint(0,len(item))
PT=item[ran_int][0]
print('PT=',PT)
CT=item[ran_int][1]
print('CT=',CT)
right_key=[0,5,0,9]
En_CT=TC20.TC20_Enc(PT,right_key)
print('En_CT=',En_CT)
if CT==En_CT:
    print("success")
else:
    print("Fail")
'''