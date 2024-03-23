# file mimesis/providers/person.py:455-464
# lines [463, 464]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender
from mimesis import Generic

@pytest.fixture
def person():
    return Person()

def test_academic_degree(person, mocker):
    # Mock the _data to contain a specific set of academic degrees
    mocked_degrees = ['Bachelor', 'Master', 'PhD']
    mocker.patch.object(person, '_data', {'academic_degree': mocked_degrees})

    # Call the method under test
    degree = person.academic_degree()

    # Assert that the returned degree is one of the mocked degrees
    assert degree in mocked_degrees
