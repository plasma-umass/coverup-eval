# file mimesis/providers/person.py:455-464
# lines [463, 464]
# branches []

import pytest
from mimesis.providers import Person
from unittest.mock import patch

@pytest.fixture
def person():
    return Person()

def test_academic_degree(person, mocker):
    mock_data = {'academic_degree': ['Bachelor', 'Master', 'PhD']}
    mocker.patch.object(person, '_data', mock_data)
    mocker.patch.object(person.random, 'choice', side_effect=lambda x: x[0])

    degree = person.academic_degree()
    assert degree == 'Bachelor'
