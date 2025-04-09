# file mimesis/providers/person.py:146-169
# lines [146, 147, 157, 158, 160, 161, 163, 165, 166, 167, 168]
# branches ['157->158', '157->160', '160->161', '160->163']

import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender
from mimesis.exceptions import NonEnumerableError

def test_full_name_with_gender():
    person = Person()
    full_name = person.full_name(gender=Gender.MALE)
    assert isinstance(full_name, str)
    assert len(full_name.split()) == 2

def test_full_name_with_reverse():
    person = Person()
    full_name = person.full_name(reverse=True)
    assert isinstance(full_name, str)
    assert len(full_name.split()) == 2
    first_name, last_name = full_name.split()
    assert first_name != '' and last_name != ''

def test_full_name_with_invalid_gender():
    person = Person()
    with pytest.raises(NonEnumerableError):
        person.full_name(gender="invalid_gender")

def test_full_name_without_gender():
    person = Person()
    full_name = person.full_name()
    assert isinstance(full_name, str)
    assert len(full_name.split()) == 2

@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
