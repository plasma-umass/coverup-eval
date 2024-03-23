# file mimesis/providers/units.py:14-51
# lines [29, 31, 32, 33, 47, 48, 50, 51]
# branches ['31->32', '31->33']

import pytest
from mimesis.enums import UnitName, PrefixSign
from mimesis.providers.units import UnitSystem

@pytest.fixture
def unit_system():
    return UnitSystem()

def test_unit_with_symbol(unit_system):
    for unit in UnitName:
        symbol = unit_system.unit(name=unit, symbol=True)
        assert symbol == unit.value[1]

def test_unit_without_symbol(unit_system):
    for unit in UnitName:
        unit_name = unit_system.unit(name=unit, symbol=False)
        assert unit_name == unit.value[0]

def test_prefix_with_symbol(unit_system):
    for sign in PrefixSign:
        prefix_symbol = unit_system.prefix(sign=sign, symbol=True)
        assert isinstance(prefix_symbol, str) and len(prefix_symbol) <= 2

def test_prefix_without_symbol(unit_system):
    for sign in PrefixSign:
        prefix = unit_system.prefix(sign=sign, symbol=False)
        assert isinstance(prefix, str) and len(prefix) > 2
