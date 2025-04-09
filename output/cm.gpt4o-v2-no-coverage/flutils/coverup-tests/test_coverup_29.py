# file: flutils/txtutils.py:245-247
# asked: {"lines": [245, 246, 247], "branches": []}
# gained: {"lines": [245, 246, 247], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_placeholder():
    wrapper = AnsiTextWrapper(placeholder=' [truncated]')
    assert wrapper.placeholder == ' [truncated]'

    wrapper.placeholder = ' [cut]'
    assert wrapper.placeholder == ' [cut]'

    wrapper = AnsiTextWrapper()
    assert wrapper.placeholder == ' [...]'
