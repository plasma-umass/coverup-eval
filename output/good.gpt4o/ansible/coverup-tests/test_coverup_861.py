# file lib/ansible/plugins/callback/junit.py:251-253
# lines [251, 253]
# branches []

import pytest
from ansible.plugins.callback import junit
from ansible.utils.display import Display
from ansible.module_utils._text import to_bytes, to_text

@pytest.fixture
def callback_module():
    return junit.CallbackModule()

def test_cleanse_string(callback_module):
    # Test with a string containing surrogate escapes
    input_string = 'test\uDC80string'
    cleansed_string = callback_module._cleanse_string(input_string)
    
    # Verify the surrogate escape is replaced with the unicode replacement character
    assert cleansed_string == 'test\uFFFDstring'

    # Test with a normal string
    input_string = 'normal string'
    cleansed_string = callback_module._cleanse_string(input_string)
    
    # Verify the string remains unchanged
    assert cleansed_string == 'normal string'
