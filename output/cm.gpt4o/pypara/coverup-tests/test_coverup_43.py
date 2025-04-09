# file pypara/monetary.py:1249-1276
# lines [1249, 1251, 1254, 1257, 1258, 1259, 1260, 1261, 1263, 1266, 1268, 1270, 1273, 1276]
# branches ['1260->1261', '1260->1263', '1266->1268', '1266->1276', '1268->1270', '1268->1273']

import pytest
from decimal import Decimal
from datetime import date as Date
from unittest.mock import Mock, patch

# Assuming these classes and exceptions are defined somewhere in pypara.monetary
from pypara.monetary import SomePrice, Currency, FXRateService, ProgrammingError, FXRateLookupError, NoPrice

@pytest.fixture
def mock_fx_rate_service():
    with patch('pypara.monetary.FXRateService.default') as mock_service:
        yield mock_service

@pytest.fixture
def mock_currency_usd():
    return Currency(code='USD', name='US Dollar', decimals=2, type='fiat', quantizer=Decimal('0.01'), hashcache={})

@pytest.fixture
def mock_currency_eur():
    return Currency(code='EUR', name='Euro', decimals=2, type='fiat', quantizer=Decimal('0.01'), hashcache={})

def test_someprice_convert_success(mock_fx_rate_service, mock_currency_usd, mock_currency_eur):
    mock_fx_rate_service.query.return_value = Mock(value=Decimal('1.2'))
    
    price = SomePrice(mock_currency_usd, Decimal('100.00'), Date(2023, 1, 1))
    converted_price = price.convert(mock_currency_eur)
    
    assert converted_price.ccy.code == 'EUR'
    assert converted_price.qty == Decimal('120.00')
    assert converted_price.dov == Date(2023, 1, 1)

def test_someprice_convert_no_rate_strict(mock_fx_rate_service, mock_currency_usd, mock_currency_eur):
    mock_fx_rate_service.query.return_value = None
    
    price = SomePrice(mock_currency_usd, Decimal('100.00'), Date(2023, 1, 1))
    
    with pytest.raises(FXRateLookupError):
        price.convert(mock_currency_eur, strict=True)

def test_someprice_convert_no_rate_non_strict(mock_fx_rate_service, mock_currency_usd, mock_currency_eur):
    mock_fx_rate_service.query.return_value = None
    
    price = SomePrice(mock_currency_usd, Decimal('100.00'), Date(2023, 1, 1))
    converted_price = price.convert(mock_currency_eur, strict=False)
    
    assert converted_price == NoPrice

def test_someprice_convert_fx_service_not_set(mock_currency_usd, mock_currency_eur):
    with patch('pypara.monetary.FXRateService.default', None):
        price = SomePrice(mock_currency_usd, Decimal('100.00'), Date(2023, 1, 1))
        
        with pytest.raises(ProgrammingError):
            price.convert(mock_currency_eur)
