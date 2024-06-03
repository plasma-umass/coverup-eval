# file mimesis/providers/person.py:62-72
# lines [62, 68, 69, 70, 72]
# branches ['69->70', '69->72']

import pytest
from mimesis.providers.person import Person

@pytest.fixture
def person(mocker):
    person_instance = Person()
    mocker.patch.object(person_instance, '_store', {'age': 0})
    return person_instance

def test_work_experience_with_default_start_age(person, mocker):
    mocker.patch.object(person, 'age', return_value=30)
    experience = person.work_experience()
    assert experience == 8

def test_work_experience_with_custom_start_age(person, mocker):
    mocker.patch.object(person, 'age', return_value=40)
    experience = person.work_experience(working_start_age=25)
    assert experience == 15

def test_work_experience_with_no_age_in_store(person, mocker):
    mocker.patch.object(person, 'age', return_value=0)
    experience = person.work_experience()
    assert experience == 0

def test_work_experience_with_age_less_than_start_age(person, mocker):
    mocker.patch.object(person, 'age', return_value=20)
    experience = person.work_experience()
    assert experience == 0
