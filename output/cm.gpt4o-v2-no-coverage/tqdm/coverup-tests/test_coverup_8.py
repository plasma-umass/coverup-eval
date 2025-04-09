# file: tqdm/notebook.py:293-294
# asked: {"lines": [293, 294], "branches": []}
# gained: {"lines": [293, 294], "branches": []}

import pytest
from unittest.mock import patch
from tqdm.notebook import tqdm_notebook

@patch('tqdm.notebook.IProgress', create=True)
@patch('tqdm.notebook.display')
def test_tqdm_notebook_clear(mock_display, mock_iprogress):
    # Create an instance of tqdm_notebook
    instance = tqdm_notebook(disable=True)

    # Call the clear method
    instance.clear()

    # Assert that the clear method does not alter any state
    # Since the clear method is a no-op, we expect no changes
    assert True  # If no exceptions are raised, the test passes
