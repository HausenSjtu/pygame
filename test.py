f_score = file('scoreForWugui.txt')
scoreLines = f_score.readlines()
f_score.close()

print scoreLines

playersInform = {}

for line in scoreLines:
    data =  line.split('\t') 
    playersInform[data[0]] = data[1:3]

print playersInform