import EngDicLib

in_file = "decryptedTEXT.txt"
InFileObj=open(in_file, 'rt', encoding='UTF8')
my_text = InFileObj.read()
InFileObj.close()

if EngDicLib.isEnglish(my_text):
    print('it is correct!')
else:
    print('it is wrong!')