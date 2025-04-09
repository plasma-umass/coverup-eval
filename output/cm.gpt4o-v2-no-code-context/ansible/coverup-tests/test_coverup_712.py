# file: lib/ansible/inventory/group.py:73-74
# asked: {"lines": [73, 74], "branches": []}
# gained: {"lines": [73, 74], "branches": []}

import pytest
from ansible.inventory.group import Group

class TestGroup:
    def test_repr(self, mocker):
        # Mock the get_name method to ensure it returns a predictable value
        group = Group()
        mocker.patch.object(group, 'get_name', return_value='test_group')
        
        # Call the __repr__ method and assert the expected result
        assert repr(group) == 'test_group'
