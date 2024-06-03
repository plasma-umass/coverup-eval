# file lib/ansible/plugins/filter/core.py:173-180
# lines [173, 175, 176, 177, 178, 180]
# branches ['175->176', '175->177', '177->178', '177->180']

import pytest
from ansible.plugins.filter.core import ternary

def test_ternary():
    # Test when value is None and none_val is provided
    assert ternary(None, 'true', 'false', 'none') == 'none'
    
    # Test when value is None and none_val is not provided
    assert ternary(None, 'true', 'false') == 'false'
    
    # Test when value is True
    assert ternary(True, 'true', 'false') == 'true'
    
    # Test when value is False
    assert ternary(False, 'true', 'false') == 'false'
    
    # Test when value is a truthy value
    assert ternary(1, 'true', 'false') == 'true'
    
    # Test when value is a falsy value
    assert ternary(0, 'true', 'false') == 'false'
