# file lib/ansible/inventory/host.py:71-84
# lines [72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84]
# branches ['81->exit', '81->82']

import pytest
from ansible.inventory.host import Host
from ansible.inventory.group import Group

@pytest.fixture
def host_data():
    return {
        'name': 'testhost',
        'vars': {'key': 'value'},
        'address': '123.123.123.123',
        'uuid': 'unique-uuid',
        'implicit': True,
        'groups': [
            {'name': 'group1', 'vars': {}},
            {'name': 'group2', 'vars': {}}
        ]
    }

def test_host_deserialize(mocker, host_data):
    # Mock the __init__ method of the Host class to prevent side effects
    mocker.patch.object(Host, '__init__', return_value=None)
    # Mock the Group class and its deserialize method to prevent side effects
    group_mock = mocker.MagicMock(spec=Group)
    group_deserialize_mock = group_mock.deserialize
    mocker.patch('ansible.inventory.host.Group', return_value=group_mock)

    host = Host()
    host.groups = []
    host.deserialize(host_data)

    # Assertions to check if the deserialize method works as expected
    assert host.name == 'testhost'
    assert host.vars == {'key': 'value'}
    assert host.address == '123.123.123.123'
    assert host._uuid == 'unique-uuid'
    assert host.implicit is True
    assert len(host.groups) == 2
    # Check if Group.deserialize was called for each group in the data
    assert group_deserialize_mock.call_count == 2
    # Check if the groups were appended to the host's groups list
    assert all(isinstance(g, mocker.MagicMock) for g in host.groups)

    # Cleanup is handled by the mocker fixture, which undoes all patches after the test
