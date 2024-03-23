# file mimesis/providers/person.py:354-362
# lines [354, 362]
# branches []

import pytest
from mimesis.providers.person import Person

@pytest.fixture
def person():
    return Person()

def test_blood_type(person):
    blood_type = person.blood_type()
    # Assuming BLOOD_GROUPS is a constant defined in the mimesis.providers.person module
    # If it's not accessible, we can define it here for the sake of the test
    BLOOD_GROUPS = ['0−', '0+', 'A−', 'A+', 'B−', 'B+', 'AB−', 'AB+']
    assert blood_type in BLOOD_GROUPS
