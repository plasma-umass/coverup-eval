# file: tqdm/notebook.py:267-275
# asked: {"lines": [267, 268, 269, 271, 274, 275], "branches": []}
# gained: {"lines": [267, 268, 269, 271, 274, 275], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.notebook import tqdm_notebook

@pytest.fixture
def mock_super_update(monkeypatch):
    mock_update = MagicMock()
    monkeypatch.setattr('tqdm.notebook.std_tqdm.update', mock_update)
    return mock_update

def test_tqdm_notebook_update_success(mock_super_update):
    tn = tqdm_notebook()
    tn.update(5)
    mock_super_update.assert_called_once_with(n=5)

def test_tqdm_notebook_update_exception(mock_super_update):
    mock_super_update.side_effect = Exception("Test Exception")
    tn = tqdm_notebook()
    with patch.object(tn, 'disp') as mock_disp:
        with pytest.raises(Exception, match="Test Exception"):
            tn.update(5)
        mock_disp.assert_called_once_with(bar_style='danger')
