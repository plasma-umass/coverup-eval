# file pymonet/utils.py:9-22
# lines [9, 15, 16, 18, 19, 20, 21, 22]
# branches ['15->16', '15->18', '19->20', '19->21']

import pytest
from pymonet.utils import curry

def test_curry_with_specified_args_count():
    def add(a, b, c):
        return a + b + c

    curried_add = curry(add, args_count=3)
    add_1 = curried_add(1)
    add_1_2 = add_1(2)
    result = add_1_2(3)

    assert result == 6

def test_curry_with_default_args_count():
    def multiply(a, b):
        return a * b

    curried_multiply = curry(multiply)
    multiply_by_2 = curried_multiply(2)
    result = multiply_by_2(3)

    assert result == 6

def test_curry_with_partial_application():
    def concat(a, b, c, d):
        return a + b + c + d

    curried_concat = curry(concat)
    concat_a = curried_concat('a')
    concat_ab = concat_a('b')
    concat_abc = concat_ab('c')
    result = concat_abc('d')

    assert result == 'abcd'

def test_curry_with_full_application():
    def subtract(a, b):
        return a - b

    curried_subtract = curry(subtract)
    result = curried_subtract(10, 3)

    assert result == 7

def test_curry_with_over_application():
    def divide(a, b):
        return a / b

    curried_divide = curry(divide)
    divide_by_2 = curried_divide(2)
    result = divide_by_2(10)

    assert result == 0.2

def test_curry_with_no_arguments():
    def no_args():
        return True

    curried_no_args = curry(no_args)
    result = curried_no_args()

    assert result is True

# Run the tests
if __name__ == "__main__":
    pytest.main()
