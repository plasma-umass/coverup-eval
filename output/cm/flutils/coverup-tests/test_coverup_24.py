# file flutils/txtutils.py:249-253
# lines [249, 250, 251, 252, 253]
# branches ['252->exit', '252->253']

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_placeholder_setter():
    wrapper = AnsiTextWrapper()
    original_placeholder = wrapper.placeholder
    new_placeholder = 'new_placeholder'

    # Set the new placeholder
    wrapper.placeholder = new_placeholder

    # Check if the placeholder is set correctly
    assert wrapper.placeholder == new_placeholder

    # Now, manually set the 'placeholder_len' attribute to simulate the condition
    wrapper.__dict__['placeholder_len'] = 10

    # Set the placeholder again to trigger the 'if' condition
    wrapper.placeholder = original_placeholder

    # Check if the 'placeholder_len' attribute is deleted
    assert 'placeholder_len' not in wrapper.__dict__
