# file flutils/txtutils.py:245-247
# lines [245, 246, 247]
# branches []

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansitextwrapper_placeholder_property():
    wrapper = AnsiTextWrapper()
    placeholder = "..."
    wrapper._AnsiTextWrapper__placeholder = placeholder  # Directly set the private attribute
    assert wrapper.placeholder == placeholder, "The placeholder property should return the correct value"
