# file tqdm/notebook.py:317-322
# lines [317, 322]
# branches []

import pytest
from unittest.mock import patch
from tqdm.notebook import tnrange, tqdm_notebook

# Define a test function for tnrange
def test_tnrange():
    with patch('tqdm.notebook.tqdm_notebook') as mock_tqdm_notebook:
        # Call the function with some arguments
        iterator = tnrange(5, desc='Test Description')

        # Check if tqdm_notebook was called with the correct arguments
        mock_tqdm_notebook.assert_called_once()
        args, kwargs = mock_tqdm_notebook.call_args
        assert args[0] == range(5)
        assert kwargs['desc'] == 'Test Description'

        # Check if the return value is from tqdm_notebook
        assert iterator == mock_tqdm_notebook.return_value

# Clean up after the test
@pytest.fixture(autouse=True)
def clean_up():
    yield
    # No cleanup needed for this test
