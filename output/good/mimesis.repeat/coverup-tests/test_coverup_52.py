# file mimesis/providers/person.py:146-169
# lines [146, 147, 157, 158, 160, 161, 163, 165, 166, 167, 168]
# branches ['157->158', '157->160', '160->161', '160->163']

import pytest
from mimesis.enums import Gender
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.person import Person
from unittest.mock import patch

def test_full_name_with_invalid_gender():
    person = Person()
    with pytest.raises(NonEnumerableError):
        person.full_name(gender="not_a_gender")

def test_full_name_with_none_gender(mocker):
    mocker.patch('mimesis.providers.person.get_random_item', return_value=Gender.MALE)
    person = Person()
    full_name = person.full_name()
    assert isinstance(full_name, str)
    assert full_name.split(' ')[0] != full_name.split(' ')[1]  # Assuming name and surname are different

def test_full_name_with_specific_gender():
    person = Person()
    full_name_male = person.full_name(gender=Gender.MALE)
    full_name_female = person.full_name(gender=Gender.FEMALE)
    assert isinstance(full_name_male, str)
    assert isinstance(full_name_female, str)
    assert full_name_male.split(' ')[0] != full_name_male.split(' ')[1]  # Assuming name and surname are different
    assert full_name_female.split(' ')[0] != full_name_female.split(' ')[1]  # Assuming name and surname are different

def test_full_name_with_reverse(mocker):
    mocker.patch('mimesis.providers.person.get_random_item', return_value=Gender.MALE)
    person = Person()
    mocker.patch.object(person, 'name', return_value='John')
    mocker.patch.object(person, 'surname', return_value='Doe')
    full_name_reversed = person.full_name(reverse=True)
    assert full_name_reversed == 'Doe John'
    full_name = person.full_name(reverse=False)
    assert full_name == 'John Doe'
