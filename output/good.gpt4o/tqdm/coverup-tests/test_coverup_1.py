# file tqdm/notebook.py:317-322
# lines [317, 322]
# branches []

import pytest
from unittest.mock import patch
from tqdm.notebook import tqdm_notebook

def test_tnrange(mocker):
    # Mock the tqdm_notebook function to ensure it is called correctly
    mock_tqdm_notebook = mocker.patch('tqdm.notebook.tqdm_notebook')

    # Import the tnrange function from the module where it is defined
    from tqdm.notebook import tnrange

    # Call tnrange with some arguments
    result = tnrange(5, desc="Test")

    # Assert that tqdm_notebook was called with the correct arguments
    mock_tqdm_notebook.assert_called_once()
    args, kwargs = mock_tqdm_notebook.call_args
    assert list(args[0]) == list(range(5))
    assert kwargs['desc'] == "Test"

    # Assert that the result is the same as the mock return value
    assert result == mock_tqdm_notebook.return_value
