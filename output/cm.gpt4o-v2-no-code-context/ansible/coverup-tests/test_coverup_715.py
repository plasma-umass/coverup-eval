# file: lib/ansible/inventory/group.py:82-83
# asked: {"lines": [82, 83], "branches": []}
# gained: {"lines": [82, 83], "branches": []}

import pytest
from ansible.inventory.group import Group

class TestGroup:
    def test___setstate__(self, mocker):
        group = Group()
        mock_deserialize = mocker.patch.object(group, 'deserialize', return_value=None)
        
        data = {'some_key': 'some_value'}
        group.__setstate__(data)
        
        mock_deserialize.assert_called_once_with(data)
