# file mimesis/providers/person.py:364-380
# lines [379, 380]
# branches ['376->379']

import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender
from mimesis import Generic

@pytest.fixture
def person():
    return Person()

def test_sexual_orientation_without_symbol(person):
    # This test aims to cover lines 379-380
    result = person.sexual_orientation(symbol=False)
    assert result in person._data['sexuality']

def test_sexual_orientation_with_symbol(mocker, person):
    # This test aims to cover lines 376-377
    mocker.patch('mimesis.providers.person.SEXUALITY_SYMBOLS', ['⚤', '⚢', '⚣'])
    result = person.sexual_orientation(symbol=True)
    assert result in ['⚤', '⚢', '⚣']
