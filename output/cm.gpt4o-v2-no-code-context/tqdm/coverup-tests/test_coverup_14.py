# file: tqdm/auto.py:38-42
# asked: {"lines": [42], "branches": []}
# gained: {"lines": [42], "branches": []}

import pytest
from unittest.mock import patch
from tqdm.auto import tqdm

# Import the trange function from the module where it is defined
from tqdm.auto import trange

def test_trange(monkeypatch):
    # Mock the tqdm function to ensure it is called correctly
    with patch('tqdm.auto.tqdm') as mock_tqdm:
        # Call the trange function with specific arguments
        trange(10, desc="Test")
        
        # Assert that tqdm was called with the correct arguments
        mock_tqdm.assert_called_once_with(range(10), desc="Test")
