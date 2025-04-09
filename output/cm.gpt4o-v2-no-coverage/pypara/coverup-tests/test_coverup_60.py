# file: pypara/dcc.py:294-302
# asked: {"lines": [294, 299, 302], "branches": []}
# gained: {"lines": [294, 299, 302], "branches": []}

import pytest
from pypara.dcc import DCCRegistryMachinery, DCC
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date
from pypara.monetary import Money
from decimal import Decimal

@pytest.fixture
def sample_dcc():
    usd_currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    return DCC(
        name="Act/Act",
        altnames={"Actual/Actual"},
        currencies={usd_currency},
        calculate_fraction_method=lambda start, asof, end, freq=None: Decimal("0.16942884946478")
    )

def test_dcc_registry_machinery_initialization():
    registry = DCCRegistryMachinery()
    assert registry._buffer_main == {}
    assert registry._buffer_altn == {}

def test_dcc_registry_machinery_is_registered(monkeypatch, sample_dcc):
    registry = DCCRegistryMachinery()
    monkeypatch.setattr(registry, '_buffer_main', {'Act/Act': sample_dcc})
    assert registry._is_registered('Act/Act') is True
    assert registry._is_registered('30/360') is False

def test_dcc_registry_machinery_register(monkeypatch, sample_dcc):
    registry = DCCRegistryMachinery()
    registry.register(sample_dcc)
    assert sample_dcc.name in registry._buffer_main

def test_dcc_registry_machinery_find_strict(monkeypatch, sample_dcc):
    registry = DCCRegistryMachinery()
    monkeypatch.setattr(registry, '_buffer_main', {'Act/Act': sample_dcc})
    assert registry._find_strict('Act/Act') is sample_dcc
    assert registry._find_strict('30/360') is None

def test_dcc_registry_machinery_find(monkeypatch, sample_dcc):
    registry = DCCRegistryMachinery()
    monkeypatch.setattr(registry, '_buffer_main', {'Act/Act': sample_dcc})
    assert registry.find('Act/Act') is sample_dcc
    assert registry.find('30/360') is None

def test_dcc_registry_machinery_registry(monkeypatch, sample_dcc):
    registry = DCCRegistryMachinery()
    monkeypatch.setattr(registry, '_buffer_main', {'Act/Act': sample_dcc})
    assert registry.registry == [sample_dcc]

def test_dcc_registry_machinery_table(monkeypatch, sample_dcc):
    registry = DCCRegistryMachinery()
    monkeypatch.setattr(registry, '_buffer_main', {'Act/Act': sample_dcc})
    assert registry.table == {'Act/Act': sample_dcc}
