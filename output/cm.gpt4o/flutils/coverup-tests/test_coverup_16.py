# file flutils/txtutils.py:233-237
# lines [233, 234, 235, 236, 237]
# branches ['236->exit', '236->237']

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_subsequent_indent(mocker):
    # Create an instance of AnsiTextWrapper
    wrapper = AnsiTextWrapper()

    # Mock the __dict__ attribute to control its contents
    mocker.patch.object(wrapper, '__dict__', {'subsequent_indent_len': 10})

    # Set the subsequent_indent property
    wrapper.subsequent_indent = '  '

    # Assert that the subsequent_indent was set correctly
    assert wrapper._AnsiTextWrapper__subsequent_indent == '  '

    # Assert that 'subsequent_indent_len' was removed from __dict__
    assert 'subsequent_indent_len' not in wrapper.__dict__

    # Clean up by resetting the __dict__ to its original state
    mocker.stopall()
