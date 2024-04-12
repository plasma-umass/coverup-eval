# file lib/ansible/plugins/action/reboot.py:104-114
# lines [104, 106, 107, 108, 109, 110, 111, 112, 113, 114]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def action_module(mocker):
    mocker.patch.multiple(ActionModule, __abstractmethods__=set())
    fake_loader = MagicMock()
    fake_templar = MagicMock()
    fake_shared_loader_obj = MagicMock()
    action_module = ActionModule(task={}, connection=None, play_context=None, loader=fake_loader, templar=fake_templar, shared_loader_obj=fake_shared_loader_obj)
    action_module._get_value_from_facts = ActionModule._get_value_from_facts.__get__(action_module)
    return action_module

def test_get_value_from_facts(action_module):
    distribution = {'name': 'testdistro', 'version': '1.0', 'family': 'testfamily'}
    action_module.test_variable = {
        'testdistro1.0': 'specific_version_value',
        'testdistro': 'distribution_value',
        'testfamily': 'family_value'
    }
    action_module.default_test_variable = 'default_value'

    # Test getting specific version value
    value = action_module._get_value_from_facts('test_variable', distribution, 'default_test_variable')
    assert value == 'specific_version_value'

    # Test getting distribution value when specific version is not present
    distribution['version'] = '2.0'
    value = action_module._get_value_from_facts('test_variable', distribution, 'default_test_variable')
    assert value == 'distribution_value'

    # Test getting family value when specific version and distribution are not present
    distribution['name'] = 'unknown_distro'
    value = action_module._get_value_from_facts('test_variable', distribution, 'default_test_variable')
    assert value == 'family_value'

    # Test getting default value when specific version, distribution, and family are not present
    distribution['family'] = 'unknown_family'
    value = action_module._get_value_from_facts('test_variable', distribution, 'default_test_variable')
    assert value == 'default_value'
