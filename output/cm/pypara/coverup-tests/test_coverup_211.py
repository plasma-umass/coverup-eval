# file pypara/monetary.py:217-225
# lines [225]
# branches []

import pytest
from pypara.monetary import Money

class DummyMoney(Money):
    pass

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_money_floor_divide_not_implemented(cleanup):
    money = DummyMoney()
    with pytest.raises(NotImplementedError):
        money.floor_divide(1)
