# file: flutils/txtutils.py:245-247
# asked: {"lines": [245, 246, 247], "branches": []}
# gained: {"lines": [245, 246, 247], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper
from textwrap import TextWrapper

def test_ansi_text_wrapper_placeholder_property():
    wrapper = AnsiTextWrapper()
    wrapper._AnsiTextWrapper__placeholder = 'test_placeholder'
    assert wrapper.placeholder == 'test_placeholder'
