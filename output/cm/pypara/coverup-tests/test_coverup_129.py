# file pypara/monetary.py:635-636
# lines [635, 636]
# branches []

import pytest
from pypara.monetary import NoneMoney

def test_nonemoney_abs():
    none_money = NoneMoney()
    result = none_money.abs()
    assert result is none_money, "The abs method should return the same NoneMoney instance"
