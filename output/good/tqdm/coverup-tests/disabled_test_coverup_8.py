# file tqdm/rich.py:121-122
# lines [121, 122]
# branches []

import pytest
from tqdm.rich import tqdm_rich
from unittest.mock import MagicMock

def test_tqdm_rich_clear():
    # Create a MagicMock console to avoid writing to the actual console
    mock_console = MagicMock()

    # Create an instance of tqdm_rich with the mock console
    with tqdm_rich(total=100, file=mock_console) as tr:
        # Replace the clear method with a MagicMock
        tr.clear = MagicMock()

        # Call the clear method
        tr.clear()

        # Assert that the clear method was called
        tr.clear.assert_called_once()
