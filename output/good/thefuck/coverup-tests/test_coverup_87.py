# file thefuck/entrypoints/alias.py:25-26
# lines [25, 26]
# branches []

import pytest
from thefuck.entrypoints.alias import print_alias
from unittest.mock import patch

@pytest.fixture
def mock_print(mocker):
    return mocker.patch('builtins.print')

@pytest.fixture
def mock_get_alias(mocker):
    return mocker.patch('thefuck.entrypoints.alias._get_alias', return_value='alias foo="bar"')

def test_print_alias(mock_print, mock_get_alias):
    known_args = 'known_args_placeholder'
    print_alias(known_args)
    mock_get_alias.assert_called_once_with(known_args)
    mock_print.assert_called_once_with('alias foo="bar"')
