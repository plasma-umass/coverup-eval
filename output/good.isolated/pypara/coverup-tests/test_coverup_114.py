# file pypara/monetary.py:177-188
# lines [177, 178, 188]
# branches []

import pytest
from pypara.monetary import Money

class IncompatibleCurrencyError(Exception):
    def __init__(self, message, ccy1, ccy2):
        super().__init__(message)
        self.ccy1 = ccy1
        self.ccy2 = ccy2

class ConcreteMoney(Money):
    def __init__(self, amount, currency, date=None):
        self.amount = amount
        self.currency = currency
        self.date = date

    def subtract(self, other):
        if self.currency != other.currency:
            raise IncompatibleCurrencyError("Currencies must match", self.currency, other.currency)
        if self.amount is None:
            return other
        if other.amount is None:
            return self
        return ConcreteMoney(self.amount - other.amount, self.currency, self.date or other.date)

def test_money_subtract_with_incompatible_currency():
    money1 = ConcreteMoney(10, 'USD')
    money2 = ConcreteMoney(5, 'EUR')
    with pytest.raises(IncompatibleCurrencyError) as exc_info:
        money1.subtract(money2)
    assert exc_info.value.ccy1 == 'USD'
    assert exc_info.value.ccy2 == 'EUR'

def test_money_subtract_with_one_operand_undefined():
    money1 = ConcreteMoney(None, 'USD')
    money2 = ConcreteMoney(5, 'USD')
    result = money1.subtract(money2)
    assert result.amount == 5
    assert result.currency == 'USD'

    result = money2.subtract(money1)
    assert result.amount == 5
    assert result.currency == 'USD'

def test_money_subtract_with_both_operands_defined():
    money1 = ConcreteMoney(10, 'USD')
    money2 = ConcreteMoney(5, 'USD')
    result = money1.subtract(money2)
    assert result.amount == 5
    assert result.currency == 'USD'

def test_money_subtract_with_date_carried_forward():
    money1 = ConcreteMoney(10, 'USD', date='2023-01-01')
    money2 = ConcreteMoney(5, 'USD')
    result = money1.subtract(money2)
    assert result.date == '2023-01-01'

    money1 = ConcreteMoney(10, 'USD')
    money2 = ConcreteMoney(5, 'USD', date='2023-01-02')
    result = money1.subtract(money2)
    assert result.date == '2023-01-02'
