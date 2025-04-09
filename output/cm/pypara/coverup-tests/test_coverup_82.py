# file pypara/monetary.py:281-286
# lines [281, 282, 286]
# branches []

import pytest
from pypara.monetary import Money, Currency

# Mock Currency class for testing purposes
class MockCurrency(Currency):
    def __init__(self):
        super().__init__(code='USD', name='Dollar', decimals=2, type='fiat', quantizer='0.01', hashcache=None)

# Concrete implementation of Money for testing purposes
class ConcreteMoney(Money):
    def __init__(self, defined=True):
        self.defined = defined
        self.currency = None

    def with_ccy(self, ccy: Currency) -> "Money":
        if self.defined:
            new_money = ConcreteMoney()
            new_money.currency = ccy
            return new_money
        return self

def test_with_ccy_defined_money():
    # Setup
    mock_currency = MockCurrency()
    defined_money = ConcreteMoney(defined=True)

    # Exercise
    new_money = defined_money.with_ccy(mock_currency)

    # Verify
    assert new_money is not defined_money
    assert new_money.currency is mock_currency

def test_with_ccy_undefined_money():
    # Setup
    mock_currency = MockCurrency()
    undefined_money = ConcreteMoney(defined=False)

    # Exercise
    same_money = undefined_money.with_ccy(mock_currency)

    # Verify
    assert same_money is undefined_money
    assert same_money.currency is None
