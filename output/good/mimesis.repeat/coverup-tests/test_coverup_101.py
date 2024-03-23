# file mimesis/providers/text.py:16-24
# lines [16, 22, 23, 24]
# branches []

import pytest
from mimesis.providers.text import Text
from unittest.mock import patch

# Test function to cover the __init__ method of the Text class
def test_text_init(mocker):
    # Mock the _pull method to ensure it is called with the correct datafile
    mock_pull = mocker.patch.object(Text, '_pull')

    # Create an instance of Text without specifying locale and seed
    text_provider = Text()

    # Assert that the _pull method was called once with 'text.json'
    mock_pull.assert_called_once_with('text.json')

    # Clean up by undoing the mocking
    mocker.stopall()
