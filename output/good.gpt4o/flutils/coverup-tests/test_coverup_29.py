# file flutils/txtutils.py:245-247
# lines [245, 246, 247]
# branches []

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_placeholder():
    wrapper = AnsiTextWrapper()
    wrapper._AnsiTextWrapper__placeholder = 'test_placeholder'
    assert wrapper.placeholder == 'test_placeholder'
