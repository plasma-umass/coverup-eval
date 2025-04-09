# file: flutils/txtutils.py:217-221
# asked: {"lines": [221], "branches": [[220, 221]]}
# gained: {"lines": [221], "branches": [[220, 221]]}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_initial_indent_deletion():
    wrapper = AnsiTextWrapper()
    wrapper.initial_indent = "test"
    wrapper.__dict__['initial_indent_len'] = 10  # Manually add the key to trigger deletion
    assert 'initial_indent_len' in wrapper.__dict__
    wrapper.initial_indent = "new_test"
    assert 'initial_indent_len' not in wrapper.__dict__
