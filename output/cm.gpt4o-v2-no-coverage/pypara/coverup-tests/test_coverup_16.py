# file: pypara/dcc.py:367-396
# asked: {"lines": [367, 377, 385, 388, 391, 394, 396], "branches": []}
# gained: {"lines": [367, 377, 385, 388, 391, 394, 396], "branches": []}

import pytest
from pypara.dcc import dcc
from pypara.currencies import Currency, CurrencyType

class MockDCCRegistry:
    registry = []

    @classmethod
    def register(cls, dcc_instance):
        cls.registry.append(dcc_instance)

@pytest.fixture
def mock_dcc_registry(monkeypatch):
    monkeypatch.setattr("pypara.dcc.DCCRegistry", MockDCCRegistry)
    yield
    MockDCCRegistry.registry.clear()

def test_dcc_registration(mock_dcc_registry):
    USD = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    EUR = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)

    @dcc(name="TestDCC", altnames={"AltName1", "AltName2"}, ccys={USD, EUR})
    def dummy_dcfc():
        pass

    assert hasattr(dummy_dcfc, "__dcc")
    dcc_instance = getattr(dummy_dcfc, "__dcc")
    assert dcc_instance.name == "TestDCC"
    assert dcc_instance.altnames == {"AltName1", "AltName2"}
    assert dcc_instance.currencies == {USD, EUR}
    assert dcc_instance.calculate_fraction_method == dummy_dcfc
    assert dcc_instance in MockDCCRegistry.registry
