# file: pypara/dcc.py:310-330
# asked: {"lines": [310, 315, 317, 320, 323, 325, 327, 330], "branches": [[315, 317], [315, 320], [323, 0], [323, 325], [325, 327], [325, 330]]}
# gained: {"lines": [310, 315, 317, 320, 323, 325, 327, 330], "branches": [[315, 317], [315, 320], [323, 0], [323, 325], [325, 327], [325, 330]]}

import pytest
from pypara.dcc import DCCRegistryMachinery, DCC
from pypara.currencies import Currency, CurrencyType
from decimal import Decimal
from unittest.mock import MagicMock

@pytest.fixture
def dcc_registry():
    return DCCRegistryMachinery()

def test_register_new_dcc(dcc_registry):
    dcc = DCC(
        name="TestDCC",
        altnames={"AltTestDCC"},
        currencies={Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)},
        calculate_fraction_method=MagicMock()
    )

    dcc_registry._is_registered = MagicMock(return_value=False)
    dcc_registry.register(dcc)

    assert dcc_registry._buffer_main["TestDCC"] == dcc
    assert dcc_registry._buffer_altn["AltTestDCC"] == dcc

def test_register_existing_main_name(dcc_registry):
    dcc = DCC(
        name="TestDCC",
        altnames={"AltTestDCC"},
        currencies={Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)},
        calculate_fraction_method=MagicMock()
    )

    dcc_registry._is_registered = MagicMock(side_effect=lambda name: name == "TestDCC")

    with pytest.raises(TypeError, match="Day count convention 'TestDCC' is already registered"):
        dcc_registry.register(dcc)

def test_register_existing_alt_name(dcc_registry):
    dcc = DCC(
        name="TestDCC",
        altnames={"AltTestDCC"},
        currencies={Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)},
        calculate_fraction_method=MagicMock()
    )

    dcc_registry._is_registered = MagicMock(side_effect=lambda name: name == "AltTestDCC")

    with pytest.raises(TypeError, match="Day count convention 'TestDCC' is already registered"):
        dcc_registry.register(dcc)
