# XML exercises
from nose.tools import ok_, eq_

MY_SMALL_XML = """
<books>
    <book type="fiction">
        <name>Iltalehti</name>
    </book>
    <book type="facts">
        <name>aku ankka</name>
    </book>
    <book type="documentation">
        <name>Robot Framework User Guide</name>
    </book>
</books>
"""

def get_names(xml_string):
    raise NotImplementedError('Implement this')

def test_parsing_book_names():
    names = get_names(MY_SMALL_XML)
    ok_('aku ankka' in names)
    ok_('Iltalehti' in names)
    ok_('Robot Framework User Guide' in names)

def get_type_by_name(name, xml_string):
    raise NotImplementedError('Implement this')

def test_getting_type_by_name():
    eq_('facts', get_type_by_name('aku ankka', MY_SMALL_XML))
    eq_('documentation', get_type_by_name('Robot Framework User Guide', MY_SMALL_XML))

def get_names_and_types(xml_string):
    raise NotImplementedError('Implement this')

def test_getting_names_and_types():
    ok_(('aku ankka', 'facts') in get_names_and_types(MY_SMALL_XML))

# SHOW ROBOT FRAMEWORK REPORTING AND HOW XML IS HANDLED THERE!!!!!!

