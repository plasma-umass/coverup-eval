# file: flutils/txtutils.py:239-243
# asked: {"lines": [239, 240, 241, 242, 243], "branches": [[241, 242], [241, 243]]}
# gained: {"lines": [239, 240, 241, 242, 243], "branches": [[241, 242], [241, 243]]}

import pytest
from flutils.txtutils import AnsiTextWrapper
from textwrap import TextWrapper
from functools import cached_property

def len_without_ansi(text):
    # Dummy implementation for testing purposes
    return len(text)

class TestAnsiTextWrapper:
    @pytest.fixture
    def wrapper(self):
        return AnsiTextWrapper()

    def test_subsequent_indent_len_no_indent(self, wrapper):
        wrapper.subsequent_indent = ''
        assert wrapper.subsequent_indent_len == 0

    def test_subsequent_indent_len_with_indent(self, wrapper, mocker):
        mocker.patch('flutils.txtutils.len_without_ansi', side_effect=len_without_ansi)
        wrapper.subsequent_indent = '    '
        assert wrapper.subsequent_indent_len == 4
