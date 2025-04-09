# file: flutils/txtutils.py:233-237
# asked: {"lines": [233, 234, 235, 236, 237], "branches": [[236, 0], [236, 237]]}
# gained: {"lines": [233, 234, 235, 236, 237], "branches": [[236, 0], [236, 237]]}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_subsequent_indent_setter():
    wrapper = AnsiTextWrapper()
    wrapper.subsequent_indent = "  "
    assert wrapper.subsequent_indent == "  "
    assert 'subsequent_indent_len' not in wrapper.__dict__

    # Access the cached property to set it
    _ = wrapper.subsequent_indent_len
    assert 'subsequent_indent_len' in wrapper.__dict__

    # Change the subsequent_indent to trigger the deletion of the cached property
    wrapper.subsequent_indent = "    "
    assert wrapper.subsequent_indent == "    "
    assert 'subsequent_indent_len' not in wrapper.__dict__
