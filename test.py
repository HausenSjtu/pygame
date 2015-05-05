<<<<<<< HEAD
dic={}
dic['1']='a'
dic['2']='b'
=======
f_score = file('scoreForWugui.txt')
scoreLines = f_score.readlines()
f_score.close()
>>>>>>> origin/master

print scoreLines

<<<<<<< HEAD
for k in dic:
    print dic[k]


print dic.get('3')==None

try:
    print dic['3']
except:
    print 'no 3'
=======
playersInform = {}

for line in scoreLines:
    data =  line.split('\t') 
    playersInform[data[0]] = data[1:3]

print playersInform
>>>>>>> origin/master
