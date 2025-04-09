# file: tqdm/notebook.py:296-314
# asked: {"lines": [296, 306, 307, 308, 309, 310, 311, 312, 313, 314], "branches": [[306, 307], [306, 308], [310, 311], [310, 314], [312, 313], [312, 314]]}
# gained: {"lines": [296, 306, 308, 309, 310, 311, 312, 313, 314], "branches": [[306, 308], [310, 311], [310, 314], [312, 313]]}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.notebook import tqdm_notebook

@pytest.fixture
def mock_tqdm_notebook():
    with patch('tqdm.notebook.std_tqdm') as MockTqdm:
        yield MockTqdm

def test_reset_disable(mock_tqdm_notebook):
    instance = tqdm_notebook()
    instance.disable = True
    with patch.object(tqdm_notebook, 'reset', return_value=None) as mock_reset:
        instance.reset(total=10)
        mock_reset.assert_called_once_with(total=10)

def test_reset_enable_no_total(mock_tqdm_notebook):
    instance = tqdm_notebook()
    instance.disable = False
    instance.container = MagicMock()
    instance.container.children = [MagicMock(), MagicMock(), MagicMock()]
    pbar = instance.container.children[1]
    instance.reset(total=None)
    assert pbar.bar_style == ''
    with patch.object(tqdm_notebook, 'reset', return_value=None) as mock_reset:
        instance.reset(total=None)
        mock_reset.assert_called_once_with(total=None)

def test_reset_enable_with_total(mock_tqdm_notebook):
    instance = tqdm_notebook()
    instance.disable = False
    instance.container = MagicMock()
    instance.container.children = [MagicMock(), MagicMock(), MagicMock()]
    pbar = instance.container.children[1]
    instance.total = None
    instance.ncols = None
    instance.reset(total=10)
    assert pbar.bar_style == ''
    assert pbar.max == 10
    assert pbar.layout.width is None
    with patch.object(tqdm_notebook, 'reset', return_value=None) as mock_reset:
        instance.reset(total=10)
        mock_reset.assert_called_once_with(total=10)
