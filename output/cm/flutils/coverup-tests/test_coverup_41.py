# file flutils/txtutils.py:229-231
# lines [229, 230, 231]
# branches []

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansitextwrapper_subsequent_indent():
    wrapper = AnsiTextWrapper()
    initial_subsequent_indent = '    '  # Four spaces
    # Use the _AnsiTextWrapper__subsequent_indent to access the private variable
    setattr(wrapper, '_AnsiTextWrapper__subsequent_indent', initial_subsequent_indent)
    assert wrapper.subsequent_indent == initial_subsequent_indent, "The subsequent_indent property should return the value set in __subsequent_indent"

    # Now change the subsequent_indent and assert it changed
    new_subsequent_indent = '  '  # Two spaces
    setattr(wrapper, '_AnsiTextWrapper__subsequent_indent', new_subsequent_indent)
    assert wrapper.subsequent_indent == new_subsequent_indent, "The subsequent_indent property should reflect the new value set in __subsequent_indent"
