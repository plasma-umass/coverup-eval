# file pypara/monetary.py:365-367
# lines [365, 366, 367]
# branches []

import pytest
from pypara.monetary import Money

def test_money_neg_abstract_method():
    class TestMoney(Money):
        def __neg__(self):
            return self

    test_money_instance = TestMoney()
    assert isinstance(-test_money_instance, TestMoney)
