# file: pypara/monetary.py:313-320
# asked: {"lines": [313, 314, 318, 319, 320], "branches": [[318, 319], [318, 320]]}
# gained: {"lines": [313, 314, 318, 319, 320], "branches": [[318, 319], [318, 320]]}

import pytest
from decimal import Decimal
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency
from pypara.monetary import Money, NoMoney, SomeMoney

def test_money_of_with_none_values():
    result = Money.of(None, None, None)
    assert result is NoMoney

def test_money_of_with_valid_values(mocker):
    mock_currency = mocker.Mock(spec=Currency)
    mock_currency.quantize.return_value = Decimal('100.00')
    mock_qty = Decimal('100.00')
    mock_dov = mocker.Mock(spec=Date)

    result = Money.of(mock_currency, mock_qty, mock_dov)
    assert isinstance(result, SomeMoney)
    assert result.ccy == mock_currency
    assert result.qty == Decimal('100.00')
    assert result.dov == mock_dov
