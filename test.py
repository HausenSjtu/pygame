dic={}
dic['1']='a'
dic['2']='b'


for k in dic:
    print dic[k]


print dic.get('3')==None

try:
    print dic['3']
except:
    print 'no 3'
