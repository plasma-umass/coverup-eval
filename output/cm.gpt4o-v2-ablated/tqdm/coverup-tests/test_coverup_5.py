# file: tqdm/notebook.py:293-294
# asked: {"lines": [293, 294], "branches": []}
# gained: {"lines": [293, 294], "branches": []}

import pytest
from unittest.mock import MagicMock

# Assuming std_tqdm is defined somewhere in tqdm/notebook.py
class std_tqdm:
    def clear(self, *args, **kwargs):
        raise NotImplementedError

from tqdm.notebook import tqdm_notebook

@pytest.fixture
def mock_std_tqdm(monkeypatch):
    mock = MagicMock(spec=std_tqdm)
    monkeypatch.setattr('tqdm.notebook.std_tqdm', mock)
    return mock

def test_tqdm_notebook_clear(mock_std_tqdm):
    tn = tqdm_notebook()
    tn.clear()
    # Ensure that the clear method in tqdm_notebook does not call the parent class's clear method
    mock_std_tqdm.clear.assert_not_called()
