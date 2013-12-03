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

