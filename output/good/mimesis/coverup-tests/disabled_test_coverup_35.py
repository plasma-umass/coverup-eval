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

def test_full_name_with_reverse():
    person = Person()
    with patch.object(person, 'name', return_value='John') as mock_name, \
         patch.object(person, 'surname', return_value='Doe') as mock_surname:
        full_name = person.full_name(reverse=True)
        assert full_name == 'Doe John'
        mock_name.assert_called_once_with(Gender.MALE)
        mock_surname.assert_called_once_with(Gender.MALE)

def test_full_name_without_gender():
    person = Person()
    with patch.object(person, 'name', return_value='John') as mock_name, \
         patch.object(person, 'surname', return_value='Doe') as mock_surname:
        full_name = person.full_name()
        assert full_name == 'John Doe'
        assert mock_name.call_count == 1
        assert mock_surname.call_count == 1

def test_full_name_with_specific_gender():
    person = Person()
    with patch.object(person, 'name', return_value='Jane') as mock_name, \
         patch.object(person, 'surname', return_value='Doe') as mock_surname:
        full_name = person.full_name(gender=Gender.FEMALE)
        assert full_name == 'Jane Doe'
        mock_name.assert_called_once_with(Gender.FEMALE)
        mock_surname.assert_called_once_with(Gender.FEMALE)
