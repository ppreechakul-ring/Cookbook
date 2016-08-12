class test(object):

    def __int__(self):
        self.a = 5
        self.b = 'd'
        b(self.a)

    def test1(self):
        print 'hi'

    def test2(self):
        print 'hello'

class b(object):

    def __int__(self,a):
        self.b1 = a
        self.b1 = 'hi'

class c(object):

    def __int__(self):
        btest = b()
        btest.test1()

class Node(object):


    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self,node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)

class DepthFirstIterator(object):

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node

        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)

from collections import deque

class LineHistory(object):

    def __init__(self, lines, histlen = 3):
        self.lines = lines
        self.history = deque(maxlen = histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines,1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

if __name__=='__main__':
    line = LineHistory