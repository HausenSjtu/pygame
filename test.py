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
