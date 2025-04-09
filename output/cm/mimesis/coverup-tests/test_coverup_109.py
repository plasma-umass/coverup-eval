# file mimesis/providers/person.py:62-72
# lines [62, 68, 69, 70, 72]
# branches ['69->70', '69->72']

import pytest
from mimesis.providers import Person

@pytest.fixture
def person():
    return Person()

def test_work_experience_with_age_zero(mocker, person):
    # Mock the age to return 0 and then a specific value
    age_mock = mocker.patch.object(person, 'age', return_value=30)

    # Set the age in the store to 0 to trigger the condition
    person._store['age'] = 0

    # Call work_experience when age is 0, which should trigger the age() method
    experience = person.work_experience()

    # Assert that the age method was called and the experience is correctly calculated
    assert age_mock.call_count == 1
    assert experience == 8  # 30 (mocked age) - 22 (default working_start_age)

def test_work_experience_with_non_zero_age(person):
    # Set the age in the store directly
    person._store['age'] = 35

    # Call work_experience when age is not 0
    experience = person.work_experience()

    # Assert that the experience is correctly calculated without calling age()
    assert experience == 13  # 35 (set age) - 22 (default working_start_age)
