# file mimesis/providers/person.py:477-493
# lines [477, 487, 488, 489, 490, 491, 493]
# branches ['487->488', '487->493']

import pytest
from mimesis.providers.person import Person
from mimesis.data import CALLING_CODES

@pytest.fixture
def person():
    return Person()

def test_telephone_with_default_mask(person, mocker):
    # Mock the random.choice method to control the output
    mocker.patch.object(person.random, 'choice', side_effect=[CALLING_CODES[0], '###-###-####'])
    mocker.patch.object(person.random, 'custom_code', return_value='123-456-7890')

    phone_number = person.telephone()
    assert phone_number == '123-456-7890'

def test_telephone_with_custom_mask(person, mocker):
    custom_mask = '+1-(###)-###-####'
    mocker.patch.object(person.random, 'custom_code', return_value='+1-(123)-456-7890')

    phone_number = person.telephone(mask=custom_mask)
    assert phone_number == '+1-(123)-456-7890'

def test_telephone_with_custom_placeholder(person, mocker):
    custom_mask = '###-###-####'
    custom_placeholder = '*'
    mocker.patch.object(person.random, 'custom_code', return_value='123-456-7890')

    phone_number = person.telephone(mask=custom_mask, placeholder=custom_placeholder)
    assert phone_number == '123-456-7890'
