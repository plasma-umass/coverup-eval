# file mimesis/providers/science.py:12-14
# lines [12, 13]
# branches []

import pytest
from mimesis.providers.science import Science

@pytest.fixture
def science_provider():
    return Science()

def test_chemical_element(science_provider):
    element = science_provider.chemical_element()
    elements = [e.split('|')[0] for e in science_provider._data['chemical_element']]
    assert element in elements
