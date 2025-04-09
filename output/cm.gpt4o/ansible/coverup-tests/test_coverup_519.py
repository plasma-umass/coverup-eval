# file lib/ansible/plugins/filter/encryption.py:73-82
# lines [73, 74, 76, 77, 78, 79, 82]
# branches []

import pytest
from ansible.plugins.filter.encryption import FilterModule

def test_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'vault' in filters
    assert 'unvault' in filters
    assert callable(filters['vault'])
    assert callable(filters['unvault'])
