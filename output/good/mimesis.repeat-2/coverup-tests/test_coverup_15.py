# file mimesis/providers/person.py:146-169
# lines [146, 147, 157, 158, 160, 161, 163, 165, 166, 167, 168]
# branches ['157->158', '157->160', '160->161', '160->163']

import pytest
from mimesis.enums import Gender
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person():
    return Generic().person

def test_full_name_with_invalid_gender(person):
    with pytest.raises(NonEnumerableError):
        person.full_name(gender="not_a_gender")

def test_full_name_with_valid_genders(person):
    for gender in Gender:
        full_name = person.full_name(gender=gender)
        assert isinstance(full_name, str)
        assert full_name

def test_full_name_with_reverse(person):
    for gender in Gender:
        full_name = person.full_name(gender=gender, reverse=True)
        assert isinstance(full_name, str)
        assert full_name
        parts = full_name.split()
        assert len(parts) == 2
        assert parts[0] != parts[1]

def test_full_name_without_gender(person):
    full_name = person.full_name()
    assert isinstance(full_name, str)
    assert full_name
