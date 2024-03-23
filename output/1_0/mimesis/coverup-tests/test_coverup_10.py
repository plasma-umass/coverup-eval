# file mimesis/providers/science.py:30-50
# lines [30, 40, 41, 43, 44, 45, 46, 47, 50]
# branches ['43->44', '43->50']

import pytest
from mimesis.providers.science import Science

@pytest.fixture
def science_provider():
    return Science()

def test_chemical_element_full_dict(science_provider):
    element = science_provider.chemical_element(name_only=False)
    assert isinstance(element, dict)
    assert 'name' in element
    assert 'symbol' in element
    assert 'atomic_number' in element
    assert isinstance(element['name'], str)
    assert isinstance(element['symbol'], str)
    assert isinstance(element['atomic_number'], str)
