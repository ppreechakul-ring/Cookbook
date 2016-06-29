class test(object):

    def __int__(self):
        self.a = 5
        self.b = 'd'

    def test1(self):
        print 'hi'

    def test2(self):
        print 'hello'

class b(object):

    def __int__(self):
        self.b1 = 'hi'
        self.b2 = 4
        self.a = test()

    def b1(self):
        print 'b1'
        return self.a

    def b2(self):
        print 'a1'

class c(object):

    def __int__(self):
        btest = b()
        btest.test1()
if __name__=='__main__':
    ctest = c()


