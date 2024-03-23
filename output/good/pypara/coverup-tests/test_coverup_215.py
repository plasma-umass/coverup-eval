# file pypara/monetary.py:302-311
# lines [311]
# branches []

import pytest
from pypara.monetary import Money, FXRateLookupError
from typing import Optional
from datetime import date as Date

class DummyCurrency:
    pass

class UnimplementedMoney(Money):
    pass

@pytest.fixture
def unimplemented_money():
    return UnimplementedMoney()

def test_money_convert_not_implemented(unimplemented_money):
    with pytest.raises(NotImplementedError):
        unimplemented_money.convert(DummyCurrency())
