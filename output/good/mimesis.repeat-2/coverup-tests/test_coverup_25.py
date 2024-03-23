# file mimesis/providers/person.py:62-72
# lines [62, 68, 69, 70, 72]
# branches ['69->70', '69->72']

import pytest
from mimesis.providers import Person

@pytest.fixture
def person(mocker):
    mocker.patch('mimesis.providers.person.Person.age', return_value=25)
    return Person()

def test_work_experience_with_age_set(person):
    person._store['age'] = 30
    assert person.work_experience() == 8

def test_work_experience_with_age_not_set(person):
    person._store['age'] = 0
    assert person.work_experience() == 3

def test_work_experience_with_age_less_than_working_start_age(person):
    person._store['age'] = 20
    assert person.work_experience(working_start_age=22) == 0
