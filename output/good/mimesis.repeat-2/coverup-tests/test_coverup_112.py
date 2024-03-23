# file mimesis/providers/choice.py:12-14
# lines [12, 13]
# branches []

import pytest
from mimesis.providers.choice import Choice

@pytest.fixture
def choice_provider():
    return Choice()

def test_choice(choice_provider):
    items = ['a', 'b', 'c']
    selected = choice_provider(items)
    assert selected in items

    # Test for empty list
    with pytest.raises(ValueError):
        choice_provider([])

    # Test for None
    with pytest.raises(TypeError):
        choice_provider(None)
