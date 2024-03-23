# file mimesis/providers/person.py:504-518
# lines [504, 518]
# branches []

import pytest
from mimesis.providers.person import Person

@pytest.fixture
def person():
    return Person(seed=0)

def test_identifier_with_custom_mask(person):
    mask = '##-@@/##'
    identifier = person.identifier(mask=mask)
    assert len(identifier) == len(mask)
    assert identifier[2] == '-'
    assert identifier[5] == '/'
    assert identifier[:2].isdigit()
    assert identifier[6:].isdigit()
    assert identifier[3:5].isalpha()

def test_identifier_with_default_mask(person):
    identifier = person.identifier()
    assert len(identifier) == 8
    assert identifier[2] == '-'
    assert identifier[5] == '/'
    assert all(char.isdigit() for char in identifier if char not in '-/')
