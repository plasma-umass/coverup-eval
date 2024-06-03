# file mimesis/providers/text.py:102-111
# lines [102, 110, 111]
# branches []

import pytest
from mimesis.providers.text import Text

@pytest.fixture
def text_provider():
    class MockRandom:
        def choice(self, seq):
            return seq[0]

    class MockText(Text):
        def __init__(self):
            self._data = {'words': {'bad': ['Damn', 'Hell', 'Crap']}}
            self.random = MockRandom()

    return MockText()

def test_swear_word(text_provider):
    swear_word = text_provider.swear_word()
    assert swear_word == 'Damn'
