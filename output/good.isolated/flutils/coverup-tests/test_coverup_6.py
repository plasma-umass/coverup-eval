# file flutils/txtutils.py:217-221
# lines [217, 218, 219, 220, 221]
# branches ['220->exit', '220->221']

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_initial_indent_setter():
    wrapper = AnsiTextWrapper()
    initial_value = '    '  # 4 spaces
    new_value = '--> '  # 4 characters with different content

    # Set initial indent and check if it's set correctly
    wrapper.initial_indent = initial_value
    assert wrapper.initial_indent == initial_value

    # Access the private attribute to simulate the condition for the branch
    wrapper.__dict__['initial_indent_len'] = len(initial_value)

    # Now set a new value and check if the branch is executed
    wrapper.initial_indent = new_value
    assert wrapper.initial_indent == new_value
    assert 'initial_indent_len' not in wrapper.__dict__
