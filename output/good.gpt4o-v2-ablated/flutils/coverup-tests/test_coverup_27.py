# file: flutils/txtutils.py:229-231
# asked: {"lines": [229, 230, 231], "branches": []}
# gained: {"lines": [229, 230, 231], "branches": []}

import pytest
from textwrap import TextWrapper
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_subsequent_indent():
    wrapper = AnsiTextWrapper()
    wrapper._AnsiTextWrapper__subsequent_indent = '  '
    assert wrapper.subsequent_indent == '  '
