code0 = ['0','111','00','1']
code1 = []
code2 = []
code = [['0','111','00','1'],['1','0','1','0']]

length = int(input())
cnt = length//56
code_dic = {}
for i in code :
    code_password = ''
    for j in i :
        code_password += (cnt+1) * j
    code_dic[code_password] = code.index(i)
print(code_dic)


code0_dic = {}
code0_password = ''
for i in code0 :
    code0_password += i * (cnt+1)
code0_dic[code0_password] = 0
print(code0_dic)