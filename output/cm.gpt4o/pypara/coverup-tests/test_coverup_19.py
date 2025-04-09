# file pypara/monetary.py:1316-1323
# lines [1316, 1318, 1320, 1322]
# branches []

import pytest
from pypara.monetary import Price

def test_none_price_class():
    class NonePrice(Price):
        __slots__ = ()
        defined = False
        undefined = True

    none_price_instance = NonePrice()

    assert not none_price_instance.defined
    assert none_price_instance.undefined
