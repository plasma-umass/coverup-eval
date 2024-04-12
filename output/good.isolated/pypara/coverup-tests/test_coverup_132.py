# file pypara/monetary.py:838-849
# lines [838, 839, 849]
# branches []

import pytest
from pypara.monetary import Price

class IncompatibleCurrencyError(Exception):
    def __init__(self, message, ccy1, ccy2):
        super().__init__(message)
        self.ccy1 = ccy1
        self.ccy2 = ccy2

class ConcretePrice(Price):
    def __init__(self, amount, currency, date=None):
        self.amount = amount
        self.currency = currency
        self.date = date

    def add(self, other):
        if self.currency != other.currency:
            raise IncompatibleCurrencyError("Currencies do not match", self.currency, other.currency)
        if self.amount is None:
            return other
        if other.amount is None:
            return self
        return ConcretePrice(self.amount + other.amount, self.currency, self.date or other.date)

def test_price_addition_with_incompatible_currency():
    price1 = ConcretePrice(10, 'USD')
    price2 = ConcretePrice(5, 'EUR')
    with pytest.raises(IncompatibleCurrencyError) as exc_info:
        price1.add(price2)
    assert exc_info.value.ccy1 == 'USD'
    assert exc_info.value.ccy2 == 'EUR'

def test_price_addition_with_undefined_operands():
    price1 = ConcretePrice(None, 'USD')
    price2 = ConcretePrice(5, 'USD')
    result = price1.add(price2)
    assert result.amount == 5
    assert result.currency == 'USD'

    result = price2.add(price1)
    assert result.amount == 5
    assert result.currency == 'USD'

def test_price_addition_with_defined_operands_and_dates():
    price1 = ConcretePrice(10, 'USD', '2023-01-01')
    price2 = ConcretePrice(5, 'USD', '2023-01-02')
    result = price1.add(price2)
    assert result.amount == 15
    assert result.currency == 'USD'
    assert result.date == '2023-01-01'  # Assuming date from the first operand is carried forward
