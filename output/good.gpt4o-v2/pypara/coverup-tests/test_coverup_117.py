# file: pypara/monetary.py:632-633
# asked: {"lines": [632, 633], "branches": []}
# gained: {"lines": [632, 633], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

def test_none_money_is_equal():
    none_money_instance = NoneMoney()
    other_none_money_instance = NoneMoney()
    different_instance = Money()  # Assuming Money is the base class

    # Test when other is an instance of NoneMoney
    assert none_money_instance.is_equal(other_none_money_instance) is True

    # Test when other is not an instance of NoneMoney
    assert none_money_instance.is_equal(different_instance) is False
