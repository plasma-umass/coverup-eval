# file mimesis/providers/text.py:72-77
# lines [72, 77]
# branches []

import pytest
from mimesis.providers.text import Text
from mimesis import Generic

@pytest.fixture
def text_provider():
    return Text('en')

def test_title(text_provider, mocker):
    mocker.patch.object(Text, 'text', return_value='Test Title')
    title = text_provider.title()
    assert title == 'Test Title'
    Text.text.assert_called_once_with(quantity=1)
