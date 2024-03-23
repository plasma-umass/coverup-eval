# file mimesis/providers/text.py:43-52
# lines [43, 51, 52]
# branches []

import pytest
from mimesis.providers.text import Text
from mimesis import Generic

@pytest.fixture
def text_provider():
    return Text()

def test_level(text_provider):
    level = text_provider.level()
    assert level in text_provider._data['level']
