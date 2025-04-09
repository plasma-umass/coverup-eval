# file: pypara/monetary.py:632-633
# asked: {"lines": [632, 633], "branches": []}
# gained: {"lines": [632, 633], "branches": []}

import pytest
from pypara.monetary import NoneMoney

def test_none_money_is_equal_with_none_money():
    none_money_instance = NoneMoney()
    other_none_money_instance = NoneMoney()
    assert none_money_instance.is_equal(other_none_money_instance) == True

def test_none_money_is_equal_with_different_class():
    none_money_instance = NoneMoney()
    class DifferentClass:
        pass
    different_class_instance = DifferentClass()
    assert none_money_instance.is_equal(different_class_instance) == False
