# file mimesis/providers/person.py:444-453
# lines [444, 452, 453]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person():
    return Person()

def test_university(person):
    university = person.university()
    assert university in person._data['university']
