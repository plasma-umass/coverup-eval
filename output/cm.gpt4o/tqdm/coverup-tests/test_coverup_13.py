# file tqdm/rich.py:142-147
# lines [147]
# branches []

import pytest
from unittest.mock import patch
from tqdm.rich import trrange

@patch('tqdm.rich.tqdm_rich')
def test_trrange(mock_tqdm_rich):
    # Call trrange with some arguments
    trrange(10, desc="Test")

    # Assert that tqdm_rich was called with the correct arguments
    mock_tqdm_rich.assert_called_once()
    args, kwargs = mock_tqdm_rich.call_args
    assert list(args[0]) == list(range(10))
    assert kwargs['desc'] == "Test"
