# file: flutils/txtutils.py:239-243
# asked: {"lines": [239, 240, 241, 242, 243], "branches": [[241, 242], [241, 243]]}
# gained: {"lines": [239, 240, 241, 242, 243], "branches": [[241, 242], [241, 243]]}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_subsequent_indent_len_with_indent():
    wrapper = AnsiTextWrapper(subsequent_indent='    ')
    assert wrapper.subsequent_indent_len == 4

def test_subsequent_indent_len_without_indent():
    wrapper = AnsiTextWrapper(subsequent_indent='')
    assert wrapper.subsequent_indent_len == 0
