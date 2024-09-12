# file: pypara/monetary.py:629-630
# asked: {"lines": [629, 630], "branches": []}
# gained: {"lines": [629, 630], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

@pytest.fixture
def none_money():
    return NoneMoney()

def test_none_money_as_boolean(none_money):
    assert not none_money.as_boolean()
