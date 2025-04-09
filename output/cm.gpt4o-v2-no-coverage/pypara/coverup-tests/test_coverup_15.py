# file: pypara/dcc.py:310-330
# asked: {"lines": [310, 315, 317, 320, 323, 325, 327, 330], "branches": [[315, 317], [315, 320], [323, 0], [323, 325], [325, 327], [325, 330]]}
# gained: {"lines": [310, 315, 317, 320, 323, 325, 327, 330], "branches": [[315, 317], [315, 320], [323, 0], [323, 325], [325, 327], [325, 330]]}

import pytest
from decimal import Decimal
from unittest.mock import MagicMock
from pypara.dcc import DCCRegistryMachinery, DCC
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import Money
from pypara.commons.zeitgeist import Date

@pytest.fixture
def dcc_registry():
    return DCCRegistryMachinery()

@pytest.fixture
def dcc():
    usd_currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    return DCC(
        name="TestDCC",
        altnames={"AltName1", "AltName2"},
        currencies={usd_currency},
        calculate_fraction_method=MagicMock()
    )

def test_register_new_dcc(dcc_registry, dcc):
    dcc_registry._is_registered = MagicMock(return_value=False)
    
    dcc_registry.register(dcc)
    
    assert dcc_registry._buffer_main[dcc.name] == dcc
    for altname in dcc.altnames:
        assert dcc_registry._buffer_altn[altname] == dcc

def test_register_existing_main_name(dcc_registry, dcc):
    dcc_registry._is_registered = MagicMock(side_effect=lambda name: name == dcc.name)
    
    with pytest.raises(TypeError, match=f"Day count convention '{dcc.name}' is already registered"):
        dcc_registry.register(dcc)

def test_register_existing_alt_name(dcc_registry, dcc):
    dcc_registry._is_registered = MagicMock(side_effect=lambda name: name in dcc.altnames)
    
    with pytest.raises(TypeError, match=f"Day count convention '{dcc.name}' is already registered"):
        dcc_registry.register(dcc)
