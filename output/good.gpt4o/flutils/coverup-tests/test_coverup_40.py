# file flutils/txtutils.py:229-231
# lines [229, 230, 231]
# branches []

import pytest
from flutils.txtutils import AnsiTextWrapper
from textwrap import TextWrapper

def test_ansi_text_wrapper_subsequent_indent():
    wrapper = AnsiTextWrapper()
    wrapper._AnsiTextWrapper__subsequent_indent = '    '
    assert wrapper.subsequent_indent == '    '
