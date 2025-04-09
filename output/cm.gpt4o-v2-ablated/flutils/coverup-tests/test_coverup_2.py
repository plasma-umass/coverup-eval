# file: flutils/txtutils.py:249-253
# asked: {"lines": [249, 250, 251, 252, 253], "branches": [[252, 0], [252, 253]]}
# gained: {"lines": [249, 250, 251, 252, 253], "branches": [[252, 0], [252, 253]]}

import pytest
from flutils.txtutils import AnsiTextWrapper
from textwrap import TextWrapper

@pytest.fixture
def wrapper():
    return AnsiTextWrapper()

def test_placeholder_setter(wrapper):
    # Test setting placeholder and check if placeholder_len is deleted
    wrapper.__dict__['placeholder_len'] = 10
    wrapper.placeholder = "new_value"
    assert wrapper._AnsiTextWrapper__placeholder == "new_value"
    assert 'placeholder_len' not in wrapper.__dict__

def test_placeholder_setter_no_placeholder_len(wrapper):
    # Test setting placeholder when placeholder_len is not in __dict__
    wrapper.placeholder = "another_value"
    assert wrapper._AnsiTextWrapper__placeholder == "another_value"
    assert 'placeholder_len' not in wrapper.__dict__
