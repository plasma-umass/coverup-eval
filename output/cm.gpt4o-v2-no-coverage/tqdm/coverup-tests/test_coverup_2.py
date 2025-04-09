# file: tqdm/notebook.py:317-322
# asked: {"lines": [317, 322], "branches": []}
# gained: {"lines": [317, 322], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from tqdm.notebook import tnrange

def test_tnrange():
    with patch('tqdm.notebook.tqdm_notebook') as mock_tqdm_notebook:
        mock_instance = MagicMock()
        mock_tqdm_notebook.return_value = mock_instance

        # Call tnrange with specific arguments
        result = tnrange(10, desc="Test")

        # Assertions to verify the behavior
        mock_tqdm_notebook.assert_called_once_with(range(10), desc="Test")
        assert result == mock_instance
