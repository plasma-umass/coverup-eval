# file: pypara/monetary.py:635-636
# asked: {"lines": [635, 636], "branches": []}
# gained: {"lines": [635, 636], "branches": []}

import pytest
from pypara.monetary import NoneMoney

def test_none_money_abs():
    none_money = NoneMoney()
    result = none_money.abs()
    assert result is none_money
