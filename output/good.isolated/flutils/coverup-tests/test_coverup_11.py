# file flutils/txtutils.py:233-237
# lines [233, 234, 235, 236, 237]
# branches ['236->exit', '236->237']

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansitextwrapper_subsequent_indent_setter():
    wrapper = AnsiTextWrapper()
    initial_subsequent_indent = wrapper.subsequent_indent
    new_subsequent_indent = '  '

    # Set the subsequent_indent to a new value
    wrapper.subsequent_indent = new_subsequent_indent

    # Check if the subsequent_indent has been updated
    assert wrapper.subsequent_indent == new_subsequent_indent

    # Check if the subsequent_indent_len attribute is deleted
    assert 'subsequent_indent_len' not in wrapper.__dict__

    # Reset the subsequent_indent to its initial value
    wrapper.subsequent_indent = initial_subsequent_indent

    # Check if the subsequent_indent has been reset correctly
    assert wrapper.subsequent_indent == initial_subsequent_indent
