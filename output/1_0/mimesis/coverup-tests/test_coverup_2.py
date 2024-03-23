# file mimesis/enums.py:38-46
# lines [38, 39, 45, 46]
# branches []

import pytest
from mimesis.enums import Gender

def test_gender_enum():
    assert Gender.FEMALE == Gender('female')
    assert Gender.MALE == Gender('male')
    assert Gender.FEMALE.value == 'female'
    assert Gender.MALE.value == 'male'
    assert len(Gender) == 2
