# file flutils/txtutils.py:213-215
# lines [213, 214, 215]
# branches []

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_initial_indent_property():
    wrapper = AnsiTextWrapper()
    test_indent = "    "  # 4 spaces
    # Use object's __dict__ to bypass the attribute name mangling for private variables
    wrapper.__dict__['_AnsiTextWrapper__initial_indent'] = test_indent
    assert wrapper.initial_indent == test_indent, "The initial_indent property did not return the expected value."
