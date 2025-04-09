# file: tqdm/notebook.py:317-322
# asked: {"lines": [317, 322], "branches": []}
# gained: {"lines": [317, 322], "branches": []}

import pytest
from tqdm.notebook import tnrange
from tqdm.notebook import tqdm_notebook

def test_tnrange(monkeypatch):
    # Mock tqdm_notebook to verify it is called with the correct parameters
    def mock_tqdm_notebook(iterable, **kwargs):
        assert list(iterable) == list(range(5))
        assert kwargs == {'desc': 'test'}
        return "mocked_tqdm_notebook"
    
    monkeypatch.setattr('tqdm.notebook.tqdm_notebook', mock_tqdm_notebook)
    
    result = tnrange(5, desc='test')
    assert result == "mocked_tqdm_notebook"
