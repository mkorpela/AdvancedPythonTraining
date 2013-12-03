from nose.tools import eq_

def fibs():
    raise NotImplementedError('Implement this')

def test_fibonacci_generator():
    fibos = fibs()
    eq_(fibos.next(), 1)
    eq_(fibos.next(), 1)
    prev, prev2 = 1, 1
    for i in xrange(100):
        f = fibos.next()
        eq_(f, prev+prev2)
        prev, prev2 = f, prev


