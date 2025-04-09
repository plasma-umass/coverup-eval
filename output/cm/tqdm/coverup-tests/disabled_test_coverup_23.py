# file tqdm/rich.py:121-122
# lines [122]
# branches []

import pytest
from tqdm.rich import tqdm_rich

def test_tqdm_rich_clear():
    tr = tqdm_rich(total=100)  # Set total to avoid TypeError
    tr.clear()  # Call the clear method to ensure line 122 is executed
    assert tr.last_print_n == 0  # Postcondition: last_print_n should be reset to 0 after clear
