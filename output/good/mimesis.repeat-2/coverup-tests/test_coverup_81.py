# file mimesis/providers/text.py:102-111
# lines [102, 110, 111]
# branches []

import pytest
from mimesis.providers.text import Text
from mimesis import Generic

@pytest.fixture
def text_provider():
    generic = Generic('en')
    return generic.text

def test_swear_word(text_provider):
    swear_word = text_provider.swear_word()
    assert swear_word is not None
    assert isinstance(swear_word, str)
    assert swear_word in text_provider._data['words'].get('bad')
