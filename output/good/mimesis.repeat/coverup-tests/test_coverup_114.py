# file mimesis/providers/person.py:455-464
# lines [455, 463, 464]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender

@pytest.fixture
def person():
    return Person()

def test_academic_degree(person):
    degree = person.academic_degree()
    assert degree in person._data['academic_degree']
