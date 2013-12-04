# Database Exercises
from nose.tools import eq_
import sqlite3
import os
from xml_exercises import MY_SMALL_XML, get_names_and_types

DATABASE_FILE = 'my_database.db'

def create_database_for_tests():
    if os.path.isfile(DATABASE_FILE):
        os.remove(DATABASE_FILE)
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute('CREATE TABLE books (name text, type text)')
    for name, book_type in get_names_and_types(MY_SMALL_XML):
        c.execute("INSERT INTO books VALUES ('%s', '%s')" % (name, book_type))
    conn.commit()
    conn.close()

create_database_for_tests()

def find_type_by_name(name):
    raise NotImplementedError('Implement this')

def test_finding_type_by_name():
    eq_(find_type_by_name('aku ankka'), 'facts')
    eq_(find_type_by_name('Iltalehti'), 'fiction')
    eq_(find_type_by_name('NOT THERE'), None)

def add_book(name, book_type):
    raise NotImplementedError('Implement this')

def test_inserting_data():
    add_book('my book', 'data')
    eq_(find_type_by_name('my book') , 'data')
    book_type = "foo'; DROP TABLE books; --"
    add_book('some other book', book_type)
    eq_(find_type_by_name('some other book', book_type))
