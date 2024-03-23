# file mimesis/providers/person.py:415-424
# lines [415, 423, 424]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person_provider():
    generic = Generic('en')
    return generic.person

def test_views_on(person_provider):
    views_on_result = person_provider.views_on()
    assert views_on_result in person_provider._data['views_on']
