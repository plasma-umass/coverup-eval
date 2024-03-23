# file mimesis/providers/text.py:16-24
# lines [16, 22, 23, 24]
# branches []

import pytest
from mimesis.providers.text import Text
from unittest.mock import patch

# Test function to cover the __init__ method of Text class
def test_text_init(mocker):
    # Mock the _pull method to ensure it's called with 'text.json'
    mock_pull = mocker.patch.object(Text, '_pull')

    # Create an instance of Text without specifying locale and seed
    text_provider = Text()

    # Assert that the _pull method was called with 'text.json'
    mock_pull.assert_called_once_with('text.json')

    # Assert that the _datafile attribute is set to 'text.json'
    assert text_provider._datafile == 'text.json'

    # Clean up by removing the mock
    mocker.stopall()
