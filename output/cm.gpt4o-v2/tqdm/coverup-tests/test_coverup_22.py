# file: tqdm/notebook.py:267-275
# asked: {"lines": [268, 269, 271, 274, 275], "branches": []}
# gained: {"lines": [268, 269, 271, 274, 275], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from tqdm.notebook import tqdm_notebook

@pytest.fixture
def mock_super_update():
    with patch('tqdm.notebook.std_tqdm.update', side_effect=Exception("Test Exception")) as mock_update:
        yield mock_update

def test_tqdm_notebook_update_exception(mock_super_update):
    tqdm_instance = tqdm_notebook(total=10)
    with patch.object(tqdm_instance, 'disp', MagicMock()) as mock_disp:
        with pytest.raises(Exception, match="Test Exception"):
            tqdm_instance.update()
        mock_disp.assert_called_once_with(bar_style='danger')
