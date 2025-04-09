# file thefuck/entrypoints/alias.py:25-26
# lines [25, 26]
# branches []

import pytest
from unittest.mock import patch
from thefuck.entrypoints.alias import print_alias

def _get_alias(known_args):
    return f"alias {known_args}"

@pytest.fixture
def mock_get_alias(mocker):
    return mocker.patch('thefuck.entrypoints.alias._get_alias', side_effect=_get_alias)

def test_print_alias(mocker, mock_get_alias):
    known_args = "test_alias"
    expected_output = f"alias {known_args}"
    
    mock_print = mocker.patch("builtins.print")
    
    print_alias(known_args)
    
    mock_print.assert_called_once_with(expected_output)
