# file pypara/monetary.py:501-507
# lines [501, 503, 504, 505, 506, 507]
# branches []

import pytest
from decimal import Decimal, DivisionByZero, InvalidOperation
from pypara.monetary import SomeMoney, NoMoney, Currency, Money, Date

@pytest.fixture
def mock_currency(mocker):
    mock_currency = mocker.Mock(spec=Currency)
    mock_currency.quantizer = Decimal('0.01')
    return mock_currency

@pytest.fixture
def some_money_instance(mock_currency):
    return SomeMoney(mock_currency, Decimal('100'), Date(2023, 1, 1))

def test_divide_by_zero_returns_no_money(some_money_instance):
    result = some_money_instance.divide(0)
    assert result == NoMoney

def test_divide_by_invalid_operation_returns_no_money(some_money_instance):
    result = some_money_instance.divide('invalid')
    assert result == NoMoney

def test_divide_by_decimal(some_money_instance):
    result = some_money_instance.divide(Decimal('2'))
    assert isinstance(result, SomeMoney)
    assert result.qty == Decimal('50.00')

def test_divide_by_int(some_money_instance):
    result = some_money_instance.divide(2)
    assert isinstance(result, SomeMoney)
    assert result.qty == Decimal('50.00')

def test_divide_by_float(some_money_instance):
    result = some_money_instance.divide(2.0)
    assert isinstance(result, SomeMoney)
    assert result.qty == Decimal('50.00')
