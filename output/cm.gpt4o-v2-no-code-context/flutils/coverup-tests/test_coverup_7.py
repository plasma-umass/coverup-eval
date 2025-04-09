# file: flutils/txtutils.py:249-253
# asked: {"lines": [249, 250, 251, 252, 253], "branches": [[252, 0], [252, 253]]}
# gained: {"lines": [249, 250, 251, 252, 253], "branches": [[252, 0], [252, 253]]}

import pytest
from flutils.txtutils import AnsiTextWrapper
from textwrap import TextWrapper

@pytest.fixture
def ansi_text_wrapper():
    return AnsiTextWrapper()

def test_placeholder_setter(ansi_text_wrapper):
    # Set the placeholder to a new value
    ansi_text_wrapper.placeholder = "new_placeholder"
    
    # Verify that the placeholder is set correctly
    assert ansi_text_wrapper._AnsiTextWrapper__placeholder == "new_placeholder"
    
    # Manually set placeholder_len to simulate its existence in __dict__
    ansi_text_wrapper.__dict__['placeholder_len'] = 10
    
    # Set the placeholder again to trigger the deletion of placeholder_len
    ansi_text_wrapper.placeholder = "another_placeholder"
    
    # Verify that placeholder_len is deleted from __dict__
    assert 'placeholder_len' not in ansi_text_wrapper.__dict__

