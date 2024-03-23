# file string_utils/validation.py:601-618
# lines [617, 618]
# branches []

import pytest
from unittest.mock import MagicMock
from string_utils.validation import is_isbn_10

@pytest.fixture
def mock_isbn_checker(mocker):
    mock_checker = MagicMock()
    mock_checker.is_isbn_10.return_value = True
    mocker.patch('string_utils.validation.__ISBNChecker', return_value=mock_checker)
    return mock_checker

def test_is_isbn_10_executes_missing_lines(mock_isbn_checker):
    assert is_isbn_10('1506715214') == True
    mock_isbn_checker.is_isbn_10.assert_called_once()
