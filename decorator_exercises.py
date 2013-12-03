# Decorator related exercises
from nose.tools import eq_, raises

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


