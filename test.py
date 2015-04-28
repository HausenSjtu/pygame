<<<<<<< HEAD
##l=[1,2,3,4]
##d={1:2,3:6,4:8}
##print l
##print d
##print d.get(5)==None
##try:
##    print l.index(5)
##except:
##    print "can't find"


class A:
    a = 10

    def __init__(self):
        print self.a
        self.a = 20

    def p(self):
        print self.a


a=A()
a.p()
=======
import numpy as np
import matplotlib.pyplot as plt
 
N = 5
menMeans = (20, 35, 30, 35, 27)
menStd =   (2, 3, 4, 1, 2)
 
ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars
 
fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)
 
womenMeans = (25, 32, 34, 20, 25)
womenStd =   (3, 5, 2, 3, 3)
rects2 = ax.bar(ind+width, womenMeans, width, color='y', yerr=womenStd)
 
# add some
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )
 
ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )
 
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')
 
autolabel(rects1)
autolabel(rects2)
 
plt.show()
>>>>>>> origin/master
