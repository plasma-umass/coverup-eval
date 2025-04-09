# file: flutils/txtutils.py:249-253
# asked: {"lines": [249, 250, 251, 252, 253], "branches": [[252, 0], [252, 253]]}
# gained: {"lines": [249, 250, 251, 252, 253], "branches": [[252, 0], [252, 253]]}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_placeholder_setter():
    wrapper = AnsiTextWrapper()
    wrapper.placeholder = "test_placeholder"
    assert wrapper._AnsiTextWrapper__placeholder == "test_placeholder"
    assert 'placeholder_len' not in wrapper.__dict__

    # Access placeholder_len to cache it
    _ = wrapper.placeholder_len
    assert 'placeholder_len' in wrapper.__dict__

    # Change placeholder and check if placeholder_len is removed from __dict__
    wrapper.placeholder = "new_placeholder"
    assert wrapper._AnsiTextWrapper__placeholder == "new_placeholder"
    assert 'placeholder_len' not in wrapper.__dict__
