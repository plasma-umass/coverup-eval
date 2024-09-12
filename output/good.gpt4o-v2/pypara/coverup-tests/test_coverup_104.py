# file: pypara/monetary.py:362-363
# asked: {"lines": [362, 363], "branches": []}
# gained: {"lines": [362, 363], "branches": []}

import pytest
from pypara.monetary import Money

class TestMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def round(self, ndigits=0):
        return round(self.amount, ndigits)

def test_round_method():
    money = TestMoney(123.456)
    rounded_money = money.round(2)
    assert rounded_money == 123.46

def test___round__method():
    money = TestMoney(123.456)
    rounded_money = round(money, 2)
    assert rounded_money == 123.46

    rounded_money_default = round(money)
    assert rounded_money_default == 123
