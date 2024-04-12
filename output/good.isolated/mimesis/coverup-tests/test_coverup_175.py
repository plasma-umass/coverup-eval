# file mimesis/providers/person.py:477-493
# lines [487, 488, 489, 490, 491, 493]
# branches ['487->488', '487->493']

import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender
from mimesis import Generic

@pytest.fixture
def person():
    return Person(seed=0)

def test_telephone_without_mask(person):
    # Mock the _data attribute to ensure that 'telephone_fmt' key is missing
    person._data = {}
    # Call the telephone method without a mask to trigger the default mask creation
    phone_number = person.telephone()
    # Assert that the phone number matches the expected pattern
    assert phone_number.startswith('+')
    assert len(phone_number) > 10  # Assuming phone numbers are longer than 10 digits
