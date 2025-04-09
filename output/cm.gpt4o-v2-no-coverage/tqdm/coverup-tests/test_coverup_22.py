# file: tqdm/notebook.py:255-263
# asked: {"lines": [256, 257, 259, 261, 262, 263], "branches": [[257, 0], [257, 259]]}
# gained: {"lines": [256, 257, 259, 261, 262, 263], "branches": [[257, 0], [257, 259]]}

import pytest
from tqdm.notebook import tqdm_notebook
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_super_iter():
    with patch('tqdm.std.tqdm.__iter__', return_value=iter([1, 2, 3])) as mock_iter:
        yield mock_iter

def test_tqdm_notebook_iter_success(mock_super_iter):
    tn = tqdm_notebook()
    result = list(tn)
    assert result == [1, 2, 3]
    mock_super_iter.assert_called_once()

def test_tqdm_notebook_iter_exception(mock_super_iter):
    mock_super_iter.side_effect = Exception("Test Exception")
    tn = tqdm_notebook()
    tn.disp = MagicMock()
    
    with pytest.raises(Exception, match="Test Exception"):
        list(tn)
    
    tn.disp.assert_called_once_with(bar_style='danger')
