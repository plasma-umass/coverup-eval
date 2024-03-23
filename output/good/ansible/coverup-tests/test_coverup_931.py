# file lib/ansible/plugins/action/yum.py:29-32
# lines [29, 31]
# branches []

import pytest
from ansible.plugins.action.yum import ActionModule as YumActionModule
from ansible.plugins.loader import action_loader

# Mock the Ansible action plugin base classes
@pytest.fixture
def action_plugin_cls(mocker):
    mocker.patch('ansible.plugins.action.ActionBase')
    return YumActionModule

# Test to ensure the TRANSFERS_FILES attribute is set to False
def test_yum_action_module_transfers_files(action_plugin_cls):
    assert not action_plugin_cls.TRANSFERS_FILES, "YumActionModule should not transfer files"
