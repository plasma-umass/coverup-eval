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
    assert len(identifier) == len(mask), "Identifier length does not match mask length"
    assert identifier[2] == '-', "Identifier format does not match mask format"
    assert identifier[5] == '/', "Identifier format does not match mask format"
    assert identifier[:2].isdigit(), "Identifier digits do not match mask digits"
    assert identifier[6:].isdigit(), "Identifier digits do not match mask digits"
    assert identifier[3:5].isalpha(), "Identifier characters do not match mask characters"
