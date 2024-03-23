# file mimesis/providers/person.py:466-475
# lines [466, 474, 475]
# branches []

import pytest
from mimesis import Person

@pytest.fixture
def person():
    return Person()

def test_language(person):
    language = person.language()
    assert language in person._data['language']
