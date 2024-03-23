# file mimesis/providers/person.py:393-402
# lines [393, 401, 402]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person():
    return Person()

def test_political_views(person):
    # Generate a political view
    political_view = person.political_views()

    # Check that the political view is in the predefined dataset
    assert political_view in person._data['political_views']
