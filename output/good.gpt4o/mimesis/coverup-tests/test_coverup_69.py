# file mimesis/providers/person.py:125-144
# lines [125, 126, 140, 141, 143, 144]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender, TitleType
from mimesis.exceptions import NonEnumerableError

@pytest.fixture
def person():
    return Person()

def test_title_with_valid_gender_and_title_type(person):
    title = person.title(gender=Gender.MALE, title_type=TitleType.TYPICAL)
    assert title in person._data['title']['male']['typical']

def test_title_with_invalid_gender(person):
    with pytest.raises(NonEnumerableError):
        person.title(gender="invalid_gender")

def test_title_with_invalid_title_type(person):
    with pytest.raises(NonEnumerableError):
        person.title(title_type="invalid_title_type")

def test_title_with_none_gender_and_title_type(person):
    title = person.title(gender=None, title_type=None)
    all_titles = (
        person._data['title']['male']['typical'] +
        person._data['title']['female']['typical'] +
        person._data['title']['male']['academic'] +
        person._data['title']['female']['academic']
    )
    assert title in all_titles
