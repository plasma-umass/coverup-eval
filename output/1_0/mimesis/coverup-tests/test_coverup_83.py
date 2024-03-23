# file mimesis/providers/file.py:19-26
# lines [19, 25, 26]
# branches []

import pytest
from mimesis.providers import File
from unittest.mock import MagicMock

def test_file_provider_initialization(mocker):
    # Mock the Text class to ensure it's being called with correct parameters
    text_mock = mocker.patch('mimesis.providers.file.Text', return_value=MagicMock())

    # Create an instance of the File provider with a specific seed
    seed = 42
    file_provider = File(seed=seed)

    # Assert that the Text class was instantiated with the correct locale and seed
    text_mock.assert_called_once_with('en', seed=seed)

    # Assert that the file_provider has an attribute _File__text which is an instance of MagicMock
    assert isinstance(file_provider._File__text, MagicMock)
