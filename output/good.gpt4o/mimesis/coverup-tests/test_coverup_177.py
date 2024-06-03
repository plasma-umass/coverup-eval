# file mimesis/providers/person.py:62-72
# lines []
# branches ['69->72']

import pytest
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person(mocker):
    generic = Generic()
    person = generic.person
    mocker.patch.object(person, '_store', {'age': 0})
    mocker.patch.object(person, 'age', return_value=30)
    return person

def test_work_experience_with_age_zero(person):
    experience = person.work_experience(working_start_age=22)
    assert experience == 8

def test_work_experience_with_non_zero_age(mocker):
    generic = Generic()
    person = generic.person
    mocker.patch.object(person, '_store', {'age': 40})
    experience = person.work_experience(working_start_age=22)
    assert experience == 18
