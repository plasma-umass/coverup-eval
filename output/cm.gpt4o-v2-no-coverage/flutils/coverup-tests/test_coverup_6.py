# file: flutils/txtutils.py:217-221
# asked: {"lines": [217, 218, 219, 220, 221], "branches": [[220, 0], [220, 221]]}
# gained: {"lines": [217, 218, 219, 220, 221], "branches": [[220, 0], [220, 221]]}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_initial_indent_setter():
    wrapper = AnsiTextWrapper()
    wrapper.initial_indent = "  "
    assert wrapper.initial_indent == "  "
    assert 'initial_indent_len' not in wrapper.__dict__

    # Set initial_indent_len to test deletion
    wrapper.__dict__['initial_indent_len'] = 2
    wrapper.initial_indent = "    "
    assert wrapper.initial_indent == "    "
    assert 'initial_indent_len' not in wrapper.__dict__
