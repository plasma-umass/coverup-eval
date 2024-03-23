# file mimesis/providers/text.py:72-77
# lines [72, 77]
# branches []

import pytest
from mimesis.providers.text import Text
from unittest.mock import Mock


@pytest.fixture
def text_provider():
    return Text('en')


def test_title(text_provider):
    text_provider.text = Mock(return_value='Test Title')
    title = text_provider.title()
    assert title == 'Test Title'
    text_provider.text.assert_called_once_with(quantity=1)
