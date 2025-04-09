# file mimesis/providers/person.py:328-339
# lines [328, 338, 339]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person():
    generic = Generic('en')
    return generic.person

def test_height_default(person):
    height = person.height()
    assert 1.5 <= float(height) <= 2.0
    assert isinstance(height, str)
    assert len(height.split('.')) == 2
    assert len(height.split('.')[1]) == 2

def test_height_custom_range(person):
    height = person.height(1.6, 1.8)
    assert 1.6 <= float(height) <= 1.8
    assert isinstance(height, str)
    assert len(height.split('.')) == 2
    assert len(height.split('.')[1]) == 2

def test_height_invalid_range(person, mocker):
    mocker.patch('mimesis.providers.person.Person.height', side_effect=ValueError)
    with pytest.raises(ValueError):
        person.height(2.0, 1.5)
