# file pypara/monetary.py:1249-1276
# lines [1263]
# branches ['1260->1263']

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomePrice, Currency, FXRateService, ProgrammingError, Price

class MockCurrency(Currency):
    def __init__(self, code):
        super().__init__(code, 'Test Currency', 2, 'fiat', lambda x: x, {})

@pytest.fixture
def mock_fx_rate_service(mocker):
    service = mocker.Mock()
    mocker.patch('pypara.monetary.FXRateService.default', new=service)
    return service

def test_convert_raises_programming_error_when_default_service_not_set(mock_fx_rate_service):
    # Set the default FX rate service to None to simulate it not being implemented
    FXRateService.default = None

    some_price = SomePrice(MockCurrency('USD'), Decimal('100.00'), date(2023, 1, 1))
    with pytest.raises(ProgrammingError):
        some_price.convert(MockCurrency('EUR'))

    # Clean up by removing the mock
    del FXRateService.default

def test_convert_raises_original_exception(mock_fx_rate_service):
    # Simulate an AttributeError that is not due to FXRateService.default being None
    mock_fx_rate_service.query.side_effect = AttributeError('test error')

    some_price = SomePrice(MockCurrency('USD'), Decimal('100.00'), date(2023, 1, 1))
    with pytest.raises(AttributeError) as exc_info:
        some_price.convert(MockCurrency('EUR'))
    assert str(exc_info.value) == 'test error'

    # Clean up by removing the mock
    del FXRateService.default
