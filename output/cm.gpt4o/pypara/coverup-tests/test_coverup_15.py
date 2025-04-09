# file pypara/monetary.py:621-628
# lines [621, 623, 625, 627]
# branches []

import pytest
from pypara.monetary import Money

def test_none_money_class():
    class NoneMoney(Money):
        __slots__ = ()
        defined = False
        undefined = True

    none_money_instance = NoneMoney()

    assert not none_money_instance.defined
    assert none_money_instance.undefined
