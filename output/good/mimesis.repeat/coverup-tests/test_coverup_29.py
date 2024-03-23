# file mimesis/providers/person.py:62-72
# lines [62, 68, 69, 70, 72]
# branches ['69->70', '69->72']

import pytest
from mimesis.providers import Person

@pytest.fixture
def person(mocker):
    mocker.patch('mimesis.providers.person.Person.age', return_value=25)
    return Person()

def test_work_experience_with_age_zero(person):
    person._store['age'] = 0
    experience = person.work_experience()
    assert experience == 3  # 25 (mocked age) - 22 (default working_start_age)

def test_work_experience_with_non_zero_age(person):
    person._store['age'] = 30
    experience = person.work_experience()
    assert experience == 8  # 30 (stored age) - 22 (default working_start_age)

def test_work_experience_with_age_less_than_working_start_age(person):
    person._store['age'] = 20
    experience = person.work_experience()
    assert experience == 0  # max(20 - 22, 0) = 0
