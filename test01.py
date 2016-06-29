class A(object):

    def __init__(self):
        self.A1 = 5
        self.A2 = 'd'

    def A_func1(self):
        self.A1 = self.A1 + 6
        return self.A1

    def A_func2(self):
        print 'hello'

class B(object):

    def __init__(self):
        self.B1 = 'hi'
        self.B2 = 4
        self.Bob = A()
        print type(self.Bob)

    def B_func1(self):
        print 'b1'
        return self.Bob


    def B_func2(self):
        print 'a1'

class C(object):

    def __init__(self):
        self.C1 = B()
        self.C2 = self.C1.B_func1()
        self.C2.A_func1()

if __name__=='__main__':
    temp = C()



