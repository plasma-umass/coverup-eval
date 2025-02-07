# file: tqdm/rich.py:115-119
# asked: {"lines": [115, 116, 117, 118, 119], "branches": [[116, 117], [116, 118]]}
# gained: {"lines": [115, 116, 117, 118, 119], "branches": [[116, 117], [116, 118]]}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.rich import tqdm_rich

@pytest.fixture
def tqdm_rich_instance():
    with patch('tqdm.rich.tqdm_rich.__init__', return_value=None):
        instance = tqdm_rich()
        instance.disable = False
        instance._prog = MagicMock()
        return instance

def test_tqdm_rich_close_disable(tqdm_rich_instance):
    tqdm_rich_instance.disable = True
    tqdm_rich_instance.close()
    tqdm_rich_instance._prog.__exit__.assert_not_called()

def test_tqdm_rich_close_enabled(tqdm_rich_instance):
    tqdm_rich_instance.disable = False
    with patch('tqdm.std.tqdm.close', return_value=None) as mock_close:
        tqdm_rich_instance.close()
        mock_close.assert_called_once()
        tqdm_rich_instance._prog.__exit__.assert_called_once_with(None, None, None)
