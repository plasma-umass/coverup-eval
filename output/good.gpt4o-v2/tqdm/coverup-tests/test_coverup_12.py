# file: tqdm/notebook.py:293-294
# asked: {"lines": [293, 294], "branches": []}
# gained: {"lines": [293, 294], "branches": []}

import pytest
from tqdm.notebook import tqdm_notebook

def test_tqdm_notebook_clear():
    # Create an instance of tqdm_notebook
    tn = tqdm_notebook(disable=True)
    
    # Ensure the instance is created with the expected initial state
    assert tn.disable is True
    
    # Call the clear method
    tn.clear()
    
    # Since clear() is a no-op, we just ensure no exceptions are raised and state remains unchanged
    assert tn.disable is True
