# file: flutils/txtutils.py:255-259
# asked: {"lines": [255, 256, 257, 258, 259], "branches": [[257, 258], [257, 259]]}
# gained: {"lines": [255, 256, 257, 258, 259], "branches": [[257, 258], [257, 259]]}

import pytest
from flutils.txtutils import AnsiTextWrapper
from unittest.mock import patch

def test_placeholder_len_with_non_empty_placeholder():
    wrapper = AnsiTextWrapper()
    wrapper.placeholder = "\x1b[31mtest\x1b[0m"
    with patch('flutils.txtutils.len_without_ansi', return_value=4) as mock_len_without_ansi:
        assert wrapper.placeholder_len == 4
        mock_len_without_ansi.assert_called_once_with("\x1b[31mtest\x1b[0m")

def test_placeholder_len_with_empty_placeholder():
    wrapper = AnsiTextWrapper()
    wrapper.placeholder = "   "
    assert wrapper.placeholder_len == 0

def test_placeholder_len_with_no_ansi():
    wrapper = AnsiTextWrapper()
    wrapper.placeholder = "test"
    with patch('flutils.txtutils.len_without_ansi', return_value=4) as mock_len_without_ansi:
        assert wrapper.placeholder_len == 4
        mock_len_without_ansi.assert_called_once_with("test")
