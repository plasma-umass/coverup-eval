# file mimesis/providers/person.py:455-464
# lines [455, 463, 464]
# branches []

import pytest
from mimesis import locales
from mimesis.providers.person import Person

@pytest.fixture
def person():
    return Person(locale=locales.DEFAULT_LOCALE)

def test_academic_degree(person):
    degree = person.academic_degree()
    assert degree in person._data['academic_degree']
