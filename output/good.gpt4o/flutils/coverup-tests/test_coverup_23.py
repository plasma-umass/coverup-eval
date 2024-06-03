# file flutils/txtutils.py:213-215
# lines [213, 214, 215]
# branches []

import pytest
from flutils.txtutils import AnsiTextWrapper
from textwrap import TextWrapper

def test_ansi_text_wrapper_initial_indent():
    wrapper = AnsiTextWrapper()
    wrapper._AnsiTextWrapper__initial_indent = ">>> "
    assert wrapper.initial_indent == ">>> "
