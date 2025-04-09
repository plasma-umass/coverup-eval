# file: tqdm/rich.py:142-147
# asked: {"lines": [142, 147], "branches": []}
# gained: {"lines": [142, 147], "branches": []}

import pytest
from unittest.mock import patch
from tqdm.rich import trrange

def test_trrange_with_args():
    with patch('tqdm.rich.tqdm_rich') as mock_tqdm_rich:
        result = trrange(10)
        mock_tqdm_rich.assert_called_once_with(range(10))
        assert result == mock_tqdm_rich.return_value

def test_trrange_with_kwargs():
    with patch('tqdm.rich.tqdm_rich') as mock_tqdm_rich:
        result = trrange(10, foo='bar')
        mock_tqdm_rich.assert_called_once_with(range(10), foo='bar')
        assert result == mock_tqdm_rich.return_value
