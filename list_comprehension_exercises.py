# List comprehension
from nose.tools import eq_

# LIST COMPREHENSION
# [ RESULT(i) for i in iterable if CONDITION(i) ]

def make_this_work_with_list_comprehension(list_of_numbers):
    result = []
    for number in list_of_numbers:
        if number % 2 == 1:
            result.append((number+5) % 7)
    return result

def test_that_it_still_works():
    f = make_this_work_with_list_comprehension
    eq_(f([]), [])
    eq_(f([1,2,3,4,5]), [6,1,3])
    eq_(f([90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), [5, 0, 2, 4, 6])

