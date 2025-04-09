# file: tqdm/rich.py:121-122
# asked: {"lines": [122], "branches": []}
# gained: {"lines": [122], "branches": []}

import pytest
from tqdm.rich import tqdm_rich

def test_tqdm_rich_clear():
    # Create an instance of tqdm_rich
    progress_bar = tqdm_rich(total=100)

    # Call the clear method
    progress_bar.clear()

    # Assert that the clear method does not alter the state
    assert progress_bar.n == 0
    assert progress_bar.total == 100

    # Clean up
    progress_bar.close()
