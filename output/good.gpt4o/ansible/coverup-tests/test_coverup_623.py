# file lib/ansible/plugins/action/service.py:26-37
# lines [26, 28, 30, 31, 36]
# branches []

import pytest
from unittest.mock import patch
from ansible.plugins.action.service import ActionModule

@pytest.fixture
def action_module():
    return ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_action_module_transfers_files(action_module):
    assert action_module.TRANSFERS_FILES is False

def test_action_module_unused_params(action_module):
    assert 'systemd' in action_module.UNUSED_PARAMS
    assert action_module.UNUSED_PARAMS['systemd'] == ['pattern', 'runlevel', 'sleep', 'arguments', 'args']

def test_action_module_builtin_svc_mgr_modules(action_module):
    expected_modules = set(['openwrt_init', 'service', 'systemd', 'sysvinit'])
    assert action_module.BUILTIN_SVC_MGR_MODULES == expected_modules

@pytest.mark.parametrize("module_name", ['openwrt_init', 'service', 'systemd', 'sysvinit'])
def test_builtin_svc_mgr_modules_contains(action_module, module_name):
    assert module_name in action_module.BUILTIN_SVC_MGR_MODULES
