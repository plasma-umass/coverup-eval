# file: tqdm/auto.py:38-42
# asked: {"lines": [38, 42], "branches": []}
# gained: {"lines": [38, 42], "branches": []}

import pytest
from tqdm.auto import tqdm
from unittest.mock import patch

# Import the trange function from the module where it is defined
from tqdm.auto import trange

def test_trange_basic():
    with patch('tqdm.auto.tqdm') as mock_tqdm:
        result = trange(10)
        mock_tqdm.assert_called_once_with(range(10))
        assert result == mock_tqdm.return_value

def test_trange_with_args():
    with patch('tqdm.auto.tqdm') as mock_tqdm:
        result = trange(1, 10, 2)
        mock_tqdm.assert_called_once_with(range(1, 10, 2))
        assert result == mock_tqdm.return_value

def test_trange_with_kwargs():
    with patch('tqdm.auto.tqdm') as mock_tqdm:
        result = trange(10, desc="Progress")
        mock_tqdm.assert_called_once_with(range(10), desc="Progress")
        assert result == mock_tqdm.return_value

def test_trange_with_args_and_kwargs():
    with patch('tqdm.auto.tqdm') as mock_tqdm:
        result = trange(1, 10, 2, desc="Progress")
        mock_tqdm.assert_called_once_with(range(1, 10, 2), desc="Progress")
        assert result == mock_tqdm.return_value
