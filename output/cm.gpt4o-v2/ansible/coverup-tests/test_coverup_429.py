# file: lib/ansible/plugins/action/reboot.py:104-114
# asked: {"lines": [104, 106, 107, 108, 109, 110, 111, 112, 113, 114], "branches": []}
# gained: {"lines": [104, 106, 107, 108, 109, 110, 111, 112, 113, 114], "branches": []}

import pytest
from ansible.plugins.action.reboot import ActionModule

class MockActionModule(ActionModule):
    def __init__(self):
        self.test_variable = {
            'Ubuntu20.04': 'value1',
            'Ubuntu': 'value2',
            'Debian': 'value3'
        }
        self.default_value = 'default_value'

@pytest.fixture
def action_module():
    return MockActionModule()

def test_get_value_from_facts_dist_version(action_module):
    distribution = {'name': 'Ubuntu', 'version': '20.04', 'family': 'Debian'}
    result = action_module._get_value_from_facts('test_variable', distribution, 'default_value')
    assert result == 'value1'

def test_get_value_from_facts_dist_name(action_module):
    distribution = {'name': 'Ubuntu', 'version': '18.04', 'family': 'Debian'}
    result = action_module._get_value_from_facts('test_variable', distribution, 'default_value')
    assert result == 'value2'

def test_get_value_from_facts_family(action_module):
    distribution = {'name': 'CentOS', 'version': '8', 'family': 'Debian'}
    result = action_module._get_value_from_facts('test_variable', distribution, 'default_value')
    assert result == 'value3'

def test_get_value_from_facts_default(action_module):
    distribution = {'name': 'CentOS', 'version': '8', 'family': 'RedHat'}
    result = action_module._get_value_from_facts('test_variable', distribution, 'default_value')
    assert result == 'default_value'
