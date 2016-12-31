class A(object):

    def __init__(self):
        self.A1 = 5
        self.A2 = 'd'
        B(self.A1)

    def A_func1(self):
        self.A1 = self.A1 + 6
        return self.A1

    def A_func2(self):
        print 'hello'

class B(object):

    def __init__(self,a):
        self.lpd = a
        self.B2 = 4
        self.B1 = 'hello'
    @property
    def B_func1(self):
        return 5
    @property
    def fw(selfs):
        return 511



    def __set__(self, instance, value):
         = value

    def __len__(self):

    def __ite
    @property
    def B_func2(self):
        print 'aaaaaaaasfd1' a

class C(object):

    def __init__(self):
        self.C1 = B()
        self.C2 = self.C1.B_func1()
        self.C2.A_func1()

    def add():
		pass
		a + b
		
if __name__=='__main__':
    temp = B(4)
    print temp.fw
    temp.B1 = 3
    temp.setFw()
	print 




