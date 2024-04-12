# file pypara/monetary.py:629-630
# lines [629, 630]
# branches []

import pytest
from pypara.monetary import NoneMoney

def test_none_money_as_boolean():
    none_money = NoneMoney()
    assert none_money.as_boolean() is False
