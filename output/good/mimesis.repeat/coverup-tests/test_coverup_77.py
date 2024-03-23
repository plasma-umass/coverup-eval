# file mimesis/providers/person.py:404-413
# lines [404, 412, 413]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person():
    return Person()

def test_worldview(person):
    worldview = person.worldview()
    assert worldview in person._data['worldview']
