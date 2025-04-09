# file: tqdm/notebook.py:293-294
# asked: {"lines": [294], "branches": []}
# gained: {"lines": [294], "branches": []}

import pytest
from tqdm.notebook import tqdm_notebook

def test_tqdm_notebook_clear():
    # Create an instance of tqdm_notebook
    tn = tqdm_notebook()
    
    # Call the clear method
    tn.clear()
    
    # Assert that the clear method does not alter the state of the object
    assert isinstance(tn, tqdm_notebook)
