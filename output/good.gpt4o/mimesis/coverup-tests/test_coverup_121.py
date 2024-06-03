# file mimesis/providers/person.py:415-424
# lines [415, 423, 424]
# branches []

import pytest
from mimesis.providers import Person

@pytest.fixture
def person(mocker):
    instance = Person()
    mocker.patch.object(instance, '_data', {'views_on': ['Positive', 'Negative', 'Neutral']})
    return instance

def test_views_on(person):
    view = person.views_on()
    assert view in ['Positive', 'Negative', 'Neutral']
