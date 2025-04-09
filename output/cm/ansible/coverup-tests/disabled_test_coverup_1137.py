# file lib/ansible/inventory/data.py:191-234
# lines [194, 195, 196, 199, 200, 201, 202, 204, 206, 207, 208, 209, 210, 211, 213, 214, 215, 218, 219, 220, 221, 223, 225, 227, 228, 229, 230, 232, 234]
# branches ['194->195', '194->232', '195->196', '195->199', '200->201', '200->206', '201->202', '201->204', '206->207', '206->225', '209->210', '209->213', '218->219', '218->227', '219->220', '219->223', '227->228', '227->234']

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData
from ansible.inventory.host import Host
from ansible.module_utils._text import to_text
from ansible.utils.display import Display

# Mock the global display object to prevent output during tests
display = Display()
display.debug = lambda x: None
display.vvvv = lambda x: None
display.warning = lambda x: None

# Mock the constants module
class C:
    LOCALHOST = ('localhost', '127.0.0.1', '::1')

# Mock the basedir function
def basedir(source):
    return '/fake/dir'

# Apply the mocks
@pytest.fixture(autouse=True)
def apply_mocks(mocker):
    mocker.patch('ansible.inventory.data.display', new=display)
    mocker.patch('ansible.inventory.data.C', new=C)
    mocker.patch('ansible.inventory.data.basedir', new=basedir)

def test_add_host_with_group(mocker):
    inventory_data = InventoryData()
    mock_group = mocker.Mock()
    inventory_data.groups = {'testgroup': mock_group}
    inventory_data.hosts = {}
    inventory_data.current_source = '/fake/source'

    host_name = 'testhost'
    group_name = 'testgroup'

    # Test adding a host with a group
    result = inventory_data.add_host(host=host_name, group=group_name)
    assert result == host_name
    assert host_name in inventory_data.hosts
    assert mock_group.add_host.called

def test_add_host_without_group():
    inventory_data = InventoryData()
    inventory_data.groups = {}
    inventory_data.hosts = {}
    inventory_data.current_source = None

    host_name = 'testhost'

    # Test adding a host without a group
    result = inventory_data.add_host(host=host_name)
    assert result == host_name
    assert host_name in inventory_data.hosts
    assert inventory_data.hosts[host_name].name == host_name

def test_add_host_invalid_name():
    inventory_data = InventoryData()

    # Test adding a host with an invalid name
    with pytest.raises(AnsibleError):
        inventory_data.add_host(host=None)

def test_add_host_to_nonexistent_group():
    inventory_data = InventoryData()
    inventory_data.groups = {}
    inventory_data.hosts = {}

    host_name = 'testhost'
    group_name = 'nonexistentgroup'

    # Test adding a host to a nonexistent group
    with pytest.raises(AnsibleError):
        inventory_data.add_host(host=host_name, group=group_name)

def test_add_host_duplicate_localhost():
    inventory_data = InventoryData()
    inventory_data.groups = {}
    inventory_data.hosts = {'localhost': Host('localhost')}
    inventory_data.localhost = inventory_data.hosts['localhost']
    inventory_data.current_source = '/fake/source'

    # Test adding a duplicate localhost
    result = inventory_data.add_host(host='127.0.0.1')
    assert result == '127.0.0.1'
    assert inventory_data.localhost.name == 'localhost'
