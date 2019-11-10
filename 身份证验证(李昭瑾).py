import re

dict={}
def AddtoDict(file):
    with open(file,'r',encoding='utf-8') as f:
        for line in f:
            list_line = []
            list_line = line.split('	',2)
            dict[list_line[0]]=list_line[1][:-1]

def verify_idcard():
    
    s=input('身份证号为:')
    AddtoDict(r'GBT2260.txt')

    key1=''.join(re.findall(r'^[1-9]\d{5}',s))
    if key1 in dict:
        print('出生地区：',end='')
        key2=key1[:2]+'0000'
        if key2 in dict:
            print(dict[key2]+'\\',end='')
        key3=key1[:4]+'00'
        if key3 in dict:
            print(dict[key3]+'\\',end='')
        print(dict[key1])
        year = int(s[6:10])
        if year % 4 == 0 or (year % 100 == 0 and year % 4 == 0):
            if re.match(
                r'[1-2]\d{3}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))',s[6:14]):
                date=1
        elif re.match(
                r'[1-2]\d{3}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))',s[6:14]):
             date=1
        if date:
            print('出生年份：',s[6:10],'月份：',s[10:12],'日：',s[12:14])

            if re.match('\d{3}',s[14:17]):
                sex=int(s[16])
                if sex % 2 == 0:
                    print('性别：女')
                else:
                    print('性别：男')
                
                if re.match('[0-9Xx]',s[17]):
                    key2=(int(s[0])*7+int(s[1])*9+int(s[2])*10+int(s[3])*5+int(s[4])*8+int(s[5])*4+int(s[6])*2+int(s[7])*1+int(s[8])*6+int(s[9])*3+int(s[10])*7
                          +int(s[11])*9+int(s[12])*10+int(s[13])*5+int(s[14])*8+int(s[15])*4+int(s[16])*2) % 11
                    cached2={0:1, 1:0, 2:'x|X', 3:9, 4:8, 5:7, 6:6, 7:5, 8:4, 9:3, 10:2}
                    if s[17]== str(cached2[key2]) :
                        print('身份验证成功')
                   
                    else:   
                        print('身份验证错误')


verify_idcard()
