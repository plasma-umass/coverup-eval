# file mimesis/providers/person.py:146-169
# lines [158, 163]
# branches ['157->158', '160->163']

import pytest
from mimesis.enums import Gender
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.person import Person

def test_full_name_with_random_gender(mocker):
    # Mock the random choice function to return a specific gender
    mocker.patch('mimesis.providers.person.get_random_item', return_value=Gender.MALE)
    
    person = Person()
    # Call full_name without specifying gender to trigger line 158
    name = person.full_name()
    assert name  # Assert that a name is returned

def test_full_name_with_invalid_gender():
    person = Person()
    # Pass an invalid gender to trigger line 163
    with pytest.raises(NonEnumerableError):
        person.full_name(gender="not_a_gender")
