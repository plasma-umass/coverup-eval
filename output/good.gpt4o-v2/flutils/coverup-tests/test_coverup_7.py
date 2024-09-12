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

    # Set a cached property to test its deletion
    wrapper.__dict__['subsequent_indent_len'] = 2
    wrapper.subsequent_indent = "    "
    assert wrapper.subsequent_indent == "    "
    assert 'subsequent_indent_len' not in wrapper.__dict__
