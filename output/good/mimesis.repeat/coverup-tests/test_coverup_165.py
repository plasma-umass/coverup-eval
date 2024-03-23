# file mimesis/providers/person.py:504-518
# lines [518]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person():
    return Person()

def test_identifier_execution(person):
    mask = '##-##/##'
    identifier = person.identifier(mask)
    assert len(identifier) == len(mask)
    for i, char in enumerate(mask):
        if char == '#':
            assert identifier[i].isdigit()
        elif char == '@':
            assert identifier[i].isalpha()
        else:
            assert identifier[i] == char
