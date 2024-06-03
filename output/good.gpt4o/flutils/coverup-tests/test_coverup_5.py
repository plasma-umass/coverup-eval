# file flutils/txtutils.py:249-253
# lines [249, 250, 251, 252, 253]
# branches ['252->exit', '252->253']

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_AnsiTextWrapper_placeholder_setter():
    wrapper = AnsiTextWrapper()
    wrapper.placeholder = "test"
    
    assert wrapper._AnsiTextWrapper__placeholder == "test"
    
    wrapper.__dict__['placeholder_len'] = 10
    wrapper.placeholder = "new_test"
    
    assert wrapper._AnsiTextWrapper__placeholder == "new_test"
    assert 'placeholder_len' not in wrapper.__dict__
