# file: flutils/txtutils.py:239-243
# asked: {"lines": [239, 240, 241, 242, 243], "branches": [[241, 242], [241, 243]]}
# gained: {"lines": [239, 240, 241, 242, 243], "branches": [[241, 242], [241, 243]]}

import pytest
from flutils.txtutils import AnsiTextWrapper
from unittest.mock import patch

def test_subsequent_indent_len_no_indent():
    wrapper = AnsiTextWrapper()
    wrapper.subsequent_indent = ""
    assert wrapper.subsequent_indent_len == 0

def test_subsequent_indent_len_with_indent():
    wrapper = AnsiTextWrapper()
    wrapper.subsequent_indent = "\x1b[31mtest\x1b[0m"
    with patch('flutils.txtutils.len_without_ansi', return_value=4) as mock_len:
        assert wrapper.subsequent_indent_len == 4
        mock_len.assert_called_once_with("\x1b[31mtest\x1b[0m")
