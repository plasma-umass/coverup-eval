# file mimesis/providers/text.py:124-133
# lines [124, 132, 133]
# branches []

import pytest
from mimesis.providers.text import Text
from mimesis import Generic

@pytest.fixture
def text_provider():
    generic = Generic()
    return generic.text

def test_color(text_provider):
    color = text_provider.color()
    assert color in text_provider._data['color']
