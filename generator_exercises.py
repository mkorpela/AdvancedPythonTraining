from nose.tools import eq_, ok_

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

def primes():
    raise NotImplementedError('Implement this')

def test_primes_generator():
    prims = primes()
    eq_(prims.next(), 2)
    eq_(prims.next(), 3)
    eq_(prims.next(), 5)
    p = prims.next()
    eq_(prims.next(), p)
    while p < 1000:
        p, previous = prims.next(), p
        ok_(p > previous)
        for p2 in primes():
            if p2**2 > p:
                break
            ok_(p % p2 != 0)

