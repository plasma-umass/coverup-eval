# file: tqdm/contrib/telegram.py:149-154
# asked: {"lines": [149, 154], "branches": []}
# gained: {"lines": [149, 154], "branches": []}

import pytest
from tqdm.contrib.telegram import ttgrange
from tqdm.contrib.telegram import tqdm_telegram
from unittest.mock import patch

@pytest.fixture
def mock_tqdm_telegram():
    with patch('tqdm.contrib.telegram.tqdm_telegram', autospec=True) as mock:
        yield mock

def test_ttgrange(mock_tqdm_telegram):
    # Test ttgrange with a simple range
    result = ttgrange(5)
    mock_tqdm_telegram.assert_called_once_with(range(5))
    assert result == mock_tqdm_telegram.return_value

    # Test ttgrange with additional arguments
    result = ttgrange(1, 5, 2)
    mock_tqdm_telegram.assert_called_with(range(1, 5, 2))
    assert result == mock_tqdm_telegram.return_value

    # Test ttgrange with keyword arguments
    result = ttgrange(5, foo='bar')
    mock_tqdm_telegram.assert_called_with(range(5), foo='bar')
    assert result == mock_tqdm_telegram.return_value
