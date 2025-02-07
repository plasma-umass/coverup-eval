# file: tqdm/notebook.py:255-263
# asked: {"lines": [256, 257, 259, 261, 262, 263], "branches": [[257, 0], [257, 259]]}
# gained: {"lines": [256, 257, 261, 262, 263], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.notebook import tqdm_notebook

class CustomException(Exception):
    pass

def test_tqdm_notebook_iter():
    # Mock the super class __iter__ method to raise an exception
    with patch('tqdm.std.tqdm.__iter__', side_effect=CustomException):
        tqdm_instance = tqdm_notebook(range(10))
        
        with pytest.raises(CustomException):
            list(tqdm_instance)
        
        # Verify that disp was called with the correct argument
        tqdm_instance.disp = MagicMock()
        try:
            list(tqdm_instance)
        except CustomException:
            pass
        tqdm_instance.disp.assert_called_once_with(bar_style='danger')
