# file mimesis/providers/text.py:65-70
# lines [65, 70]
# branches []

import pytest
from mimesis.providers.text import Text

@pytest.fixture
def text_provider():
    return Text()

def test_sentence_method(text_provider):
    sentence = text_provider.sentence()
    assert isinstance(sentence, str)
    assert len(sentence) > 0

# Ensure that the text method is called with quantity=1
def test_sentence_calls_text_with_quantity_one(mocker, text_provider):
    mock_text = mocker.patch.object(Text, 'text', return_value='Mocked sentence')
    sentence = text_provider.sentence()
    mock_text.assert_called_once_with(quantity=1)
    assert sentence == 'Mocked sentence'
