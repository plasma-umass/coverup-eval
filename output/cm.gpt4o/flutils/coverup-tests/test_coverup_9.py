# file flutils/txtutils.py:255-259
# lines [255, 256, 257, 258, 259]
# branches ['257->258', '257->259']

import pytest
from unittest.mock import patch
from flutils.txtutils import AnsiTextWrapper

@pytest.fixture
def mock_len_without_ansi(mocker):
    return mocker.patch('flutils.txtutils.len_without_ansi', return_value=5)

def test_placeholder_len_with_non_empty_placeholder(mock_len_without_ansi):
    wrapper = AnsiTextWrapper()
    wrapper.placeholder = 'test'
    assert wrapper.placeholder_len == 5
    mock_len_without_ansi.assert_called_once_with('test')

def test_placeholder_len_with_empty_placeholder():
    wrapper = AnsiTextWrapper()
    wrapper.placeholder = '   '
    assert wrapper.placeholder_len == 0
