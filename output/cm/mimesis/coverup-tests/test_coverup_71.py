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
    # Ensure that the swear_word method returns a string
    swear_word = text_provider.swear_word()
    assert isinstance(swear_word, str)
    # Ensure that the swear_word is in the list of bad words
    bad_words = text_provider._data['words'].get('bad')
    assert swear_word in bad_words
