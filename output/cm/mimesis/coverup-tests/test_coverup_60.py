# file mimesis/providers/person.py:382-391
# lines [382, 390, 391]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person_provider():
    generic = Generic()
    return generic.person

def test_occupation(person_provider):
    occupation = person_provider.occupation()
    assert occupation in person_provider._data['occupation']
