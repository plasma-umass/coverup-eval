# file: tqdm/notebook.py:317-322
# asked: {"lines": [322], "branches": []}
# gained: {"lines": [322], "branches": []}

import pytest
from unittest.mock import patch
from tqdm.notebook import tnrange, tqdm_notebook

def test_tnrange_executes_tqdm_notebook():
    with patch('tqdm.notebook.tqdm_notebook') as mock_tqdm_notebook:
        result = tnrange(10)
        mock_tqdm_notebook.assert_called_once()
        assert isinstance(result, mock_tqdm_notebook.return_value.__class__)

@pytest.mark.parametrize("args, kwargs", [
    ((10,), {}),
    ((5, 15), {'desc': 'test'}),
    ((0, 20, 2), {'disable': True}),
])
def test_tnrange_various_args(args, kwargs):
    with patch('tqdm.notebook.tqdm_notebook') as mock_tqdm_notebook:
        result = tnrange(*args, **kwargs)
        mock_tqdm_notebook.assert_called_once_with(range(*args), **kwargs)
        assert isinstance(result, mock_tqdm_notebook.return_value.__class__)
