# file tqdm/contrib/telegram.py:149-154
# lines [149, 154]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from tqdm.contrib.telegram import tqdm as tqdm_telegram

def _range(*args):
    return range(*args)

def ttgrange(*args, **kwargs):
    """
    A shortcut for `tqdm.contrib.telegram.tqdm(xrange(*args), **kwargs)`.
    On Python3+, `range` is used instead of `xrange`.
    """
    return tqdm_telegram(_range(*args), **kwargs)

@patch('tqdm.contrib.telegram.TelegramIO')
@patch('tqdm.contrib.telegram.tqdm.__init__', return_value=None)
@patch('tqdm.contrib.telegram.tqdm.update')
@patch('tqdm.contrib.telegram.tqdm.close')
def test_ttgrange(mock_close, mock_update, mock_tqdm_init, mock_telegram_io):
    args = (10,)
    kwargs = {'desc': 'test'}
    
    # Mock the TelegramIO instance to avoid real HTTP requests
    mock_telegram_io_instance = MagicMock()
    mock_telegram_io.return_value = mock_telegram_io_instance
    mock_telegram_io_instance.message_id = 12345
    
    # Call the function
    result = ttgrange(*args, **kwargs)
    
    # Assertions to verify the function behavior
    mock_tqdm_init.assert_called_once_with(range(*args), **kwargs)
    assert isinstance(result, tqdm_telegram)
