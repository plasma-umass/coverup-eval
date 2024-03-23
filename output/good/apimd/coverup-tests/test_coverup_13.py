# file apimd/parser.py:51-53
# lines [51, 53]
# branches []

import pytest
from apimd.parser import parent

def test_parent():
    # Test with default level
    assert parent('apimd.parser.module') == 'apimd.parser'
    
    # Test with specified level
    assert parent('apimd.parser.module', level=2) == 'apimd'
    
    # Test with level higher than possible splits
    assert parent('apimd.parser.module', level=5) == 'apimd'
    
    # Test with empty string
    assert parent('', level=1) == ''
    
    # Test with no dots
    assert parent('apimd', level=1) == 'apimd'
    
    # Test with level 0
    assert parent('apimd.parser.module', level=0) == 'apimd.parser.module'
