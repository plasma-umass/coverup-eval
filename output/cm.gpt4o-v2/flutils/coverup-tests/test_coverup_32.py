# file: flutils/txtutils.py:229-231
# asked: {"lines": [229, 230, 231], "branches": []}
# gained: {"lines": [229, 230, 231], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_subsequent_indent_property():
    wrapper = AnsiTextWrapper(subsequent_indent='    ')
    assert wrapper.subsequent_indent == '    '

    wrapper.subsequent_indent = '>> '
    assert wrapper.subsequent_indent == '>> '
