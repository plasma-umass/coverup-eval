# file: pypara/monetary.py:632-633
# asked: {"lines": [632, 633], "branches": []}
# gained: {"lines": [632, 633], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

def test_none_money_is_equal_with_none_money():
    none_money1 = NoneMoney()
    none_money2 = NoneMoney()
    assert none_money1.is_equal(none_money2) == True

def test_none_money_is_equal_with_other_money():
    none_money = NoneMoney()
    other_money = Money()
    assert none_money.is_equal(other_money) == False

def test_none_money_is_equal_with_non_money():
    none_money = NoneMoney()
    non_money = "Not a Money instance"
    assert none_money.is_equal(non_money) == False
