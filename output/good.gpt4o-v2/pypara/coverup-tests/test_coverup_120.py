# file: pypara/monetary.py:647-648
# asked: {"lines": [647, 648], "branches": []}
# gained: {"lines": [647, 648], "branches": []}

import pytest
from pypara.monetary import NoneMoney

def test_none_money_negative():
    none_money = NoneMoney()
    result = none_money.negative()
    assert result is none_money
