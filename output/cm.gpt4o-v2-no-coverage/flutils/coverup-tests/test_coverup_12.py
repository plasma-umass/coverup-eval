# file: flutils/txtutils.py:249-253
# asked: {"lines": [249, 250, 251, 252, 253], "branches": [[252, 0], [252, 253]]}
# gained: {"lines": [249, 250, 251, 252, 253], "branches": [[252, 0], [252, 253]]}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_placeholder_setter():
    wrapper = AnsiTextWrapper()
    wrapper.placeholder = "test"
    assert wrapper.placeholder == "test"
    assert 'placeholder_len' not in wrapper.__dict__

    wrapper.__dict__['placeholder_len'] = 4
    wrapper.placeholder = "new_test"
    assert wrapper.placeholder == "new_test"
    assert 'placeholder_len' not in wrapper.__dict__
