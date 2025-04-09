# file flutils/txtutils.py:239-243
# lines [241, 242, 243]
# branches ['241->242', '241->243']

import pytest
from flutils.txtutils import AnsiTextWrapper
from unittest.mock import patch, PropertyMock

def test_subsequent_indent_len_no_indent():
    wrapper = AnsiTextWrapper()
    with patch.object(wrapper.__class__, 'subsequent_indent', new_callable=PropertyMock) as mock_subsequent_indent:
        mock_subsequent_indent.return_value = ''
        assert wrapper.subsequent_indent_len == 0

def test_subsequent_indent_len_with_indent():
    wrapper = AnsiTextWrapper()
    with patch.object(wrapper.__class__, 'subsequent_indent', new_callable=PropertyMock) as mock_subsequent_indent:
        mock_subsequent_indent.return_value = '    '
        with patch('flutils.txtutils.len_without_ansi', return_value=4) as mock_len_without_ansi:
            assert wrapper.subsequent_indent_len == 4
            mock_len_without_ansi.assert_called_once_with('    ')
