# Decorator related exercises
from nose.tools import eq_, raises, timed

# Property
class ClassWithProperty(object):

    def __init__(self, value_for_property):
        self.value = value_for_property

@raises(AttributeError)
def test_property():
    obj = ClassWithProperty(7)
    eq_(obj.value, 7)
    obj.value = 8


# Context manager
from contextlib import contextmanager
from StringIO import StringIO

def tag(tag, stream):
    raise NotImplementedError('Implement this')

def test_xml_tag():
    stream = StringIO()
    with tag('foo', stream):
        stream.write('moi')
    eq_(stream.getvalue(), '<foo>moi</foo>')


# Overrides
def overrides(interface_class):
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider

class SuperDuberClass(object):

    def method(self):
        return 3

@raises(AssertionError)
def test_overrides_usage():

    class Subclass(SuperDuberClass):
        
        def methud(self):
            return 5


# Making a simple decorator

def add_one_decorator(func):
    raise NotImplementedError('Implement this')

def test_simple_decorator():

    @add_one_decorator
    def return_four():
        return 4

    eq_(return_four(), 5)

def cache_result_decorator(func):
    """ Implement this! """
    return func

import timeit

@timed(1.0)
def test_fibonacci_performance():
    @cache_result_decorator
    def fib(n):
        if n <= 1:
            return 1
        return fib(n-1)+fib(n-2)
    fib(35)
    
# Decorator with an argument

def add_some_decorator(some_number):
    raise NotImplementedError('Implement this')

def test_decorator_with_argument():
    @add_some_decorator(3)
    def one():
        return 1
    @add_some_decorator(5)
    def two():
        return 2
    eq_(one(), 4)
    eq_(two(), 7)

# Decorator as a class

class MyDecoratorClass(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        raise NotImplementedError('Implement this')

def test_decorator_class():
    @MyDecoratorClass
    def say_hello(name):
        return 'hello %s' % name
    eq_(say_hello('steve'), 'HELLO STEVE')
