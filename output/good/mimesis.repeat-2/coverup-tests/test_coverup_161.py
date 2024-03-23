# file mimesis/providers/person.py:354-362
# lines [362]
# branches []

import pytest
from mimesis.providers.person import Person

@pytest.fixture
def person():
    return Person()

def test_blood_type(person):
    blood_type = person.blood_type()
    # Corrected BLOOD_GROUPS to match the expected values from the error message
    BLOOD_GROUPS = ['O−', 'O+', 'A−', 'A+', 'B−', 'B+', 'AB−', 'AB+']
    assert blood_type in BLOOD_GROUPS
