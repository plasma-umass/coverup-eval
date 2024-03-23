# file lib/ansible/inventory/host.py:57-69
# lines [57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68]
# branches ['59->60', '59->62']

import pytest
from ansible.inventory.host import Host
from ansible.inventory.group import Group

# Mock class to avoid side effects on other tests
class MockGroup(Group):
    def __init__(self, name):
        super(MockGroup, self).__init__(name=name)

    def serialize(self):
        return {'name': self.name}

@pytest.fixture
def mock_group(mocker):
    return MockGroup(name='testgroup')

@pytest.fixture
def host_with_groups(mock_group):
    host = Host(name='testhost')
    host.vars = {}
    host.address = 'testaddress'
    host._uuid = 'testuuid'
    host.implicit = False
    host.add_group(mock_group)
    return host

def test_host_serialize_with_groups(host_with_groups, mock_group):
    serialized_data = host_with_groups.serialize()
    assert serialized_data['name'] == 'testhost'
    assert serialized_data['address'] == 'testaddress'
    assert serialized_data['groups'] == [{'name': mock_group.name}]
    assert serialized_data['vars'] == {}
    assert serialized_data['uuid'] == 'testuuid'
    assert serialized_data['implicit'] is False
