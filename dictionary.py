import re

fin = file('input.txt')
lines = fin.readlines()
fin.close()

dic={}

for line in lines:
    zf = re.findall(r':\d*',line)
    z = zf[0].strip(':')
    f = zf[1].strip(':')
    dic[z] = f

print dic

fout = file('output.txt','w')
for z in dic:
    fout.writelines('z'+z+'--f'+dic[z]+'\n')
fout.close()
