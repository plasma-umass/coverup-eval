# file: pypara/dcc.py:367-396
# asked: {"lines": [367, 377, 385, 388, 391, 394, 396], "branches": []}
# gained: {"lines": [367, 377, 385, 388, 391, 394, 396], "branches": []}

import pytest
from pypara.dcc import dcc, DCCRegistry
from pypara.currencies import Currency, CurrencyType

@pytest.fixture
def mock_dcc_registry(mocker):
    """Fixture to mock the DCCRegistry."""
    mock_registry = mocker.patch.object(DCCRegistry, 'register', autospec=True)
    return mock_registry

@pytest.fixture
def usd_currency():
    """Fixture to create a USD currency instance."""
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def eur_currency():
    """Fixture to create a EUR currency instance."""
    return Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)

def test_dcc_registration(mock_dcc_registry, usd_currency, eur_currency):
    """Test the dcc decorator for registering a day count convention."""

    @dcc(name="TestDCC", altnames={"AltName1", "AltName2"}, ccys={usd_currency, eur_currency})
    def test_calculate_fraction(start, asof, end, freq=None):
        return 0.5

    # Check if the function is registered
    assert hasattr(test_calculate_fraction, "__dcc")
    dcc_instance = getattr(test_calculate_fraction, "__dcc")
    assert dcc_instance.name == "TestDCC"
    assert dcc_instance.altnames == {"AltName1", "AltName2"}
    assert dcc_instance.currencies == {usd_currency, eur_currency}
    assert dcc_instance.calculate_fraction_method == test_calculate_fraction

    # Ensure the DCCRegistry.register was called
    mock_dcc_registry.assert_called_once()
