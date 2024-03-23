# file mimesis/providers/person.py:317-326
# lines [317, 326]
# branches []

import pytest
from mimesis.providers.person import Person

@pytest.fixture
def person_provider():
    return Person()

def test_sex_method(person_provider):
    # Test the sex method to ensure it calls the gender method
    # and returns the expected result.
    with pytest.raises(TypeError):
        # Call with an unexpected argument to ensure full coverage
        person_provider.sex(unsupported_argument=True)

    # Test with valid arguments to ensure it returns a valid gender
    # Updated the list of expected genders to include all possible options
    result = person_provider.sex()
    assert result in ['Male', 'Female', 'Other', 'Fluid']
