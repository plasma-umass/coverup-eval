# file mimesis/providers/text.py:173-182
# lines [173, 181, 182]
# branches []

import pytest
from mimesis.providers.text import Text
from mimesis import Generic

@pytest.fixture
def text_provider():
    generic = Generic('en')
    return generic.text

def test_answer(text_provider):
    answer = text_provider.answer()
    assert answer in text_provider._data['answers']
