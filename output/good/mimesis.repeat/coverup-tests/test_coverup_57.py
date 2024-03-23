# file mimesis/providers/person.py:426-442
# lines [426, 435, 438, 439, 440, 442]
# branches ['438->439', '438->442']

import pytest
from mimesis.enums import Gender
from mimesis.providers.person import Person

@pytest.fixture
def person():
    return Person()

def test_nationality_with_gender(person):
    # Assuming the data structure is a dictionary with gender keys
    # and the values are lists of nationalities
    if isinstance(person._data['nationality'], dict):
        male_nationality = person.nationality(gender=Gender.MALE)
        female_nationality = person.nationality(gender=Gender.FEMALE)

        assert male_nationality in person._data['nationality'][Gender.MALE.name]
        assert female_nationality in person._data['nationality'][Gender.FEMALE.name]
    else:
        pytest.skip("Nationality data is not separated by gender")

def test_nationality_without_gender(person):
    # Assuming the data structure is a list of nationalities
    if not isinstance(person._data['nationality'], dict):
        generic_nationality = person.nationality()
        assert generic_nationality in person._data['nationality']
    else:
        pytest.skip("Nationality data is separated by gender")

def test_nationality_with_invalid_gender(person, mocker):
    # Assuming the data structure is a dictionary with gender keys
    # and the values are lists of nationalities
    if isinstance(person._data['nationality'], dict):
        mocker.patch.object(Person, '_validate_enum', side_effect=KeyError('invalid_gender'))
        with pytest.raises(KeyError):
            person.nationality(gender='invalid_gender')
    else:
        pytest.skip("Nationality data is not separated by gender")
