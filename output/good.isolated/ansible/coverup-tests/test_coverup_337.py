# file lib/ansible/module_utils/facts/system/apparmor.py:26-39
# lines [26, 27, 28, 30, 31, 32, 33, 34, 36, 38, 39]
# branches ['33->34', '33->36']

import os
import pytest
from ansible.module_utils.facts.system.apparmor import ApparmorFactCollector

# Mock os.path.exists to control the existence of the apparmor path
@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists')

# Test when apparmor is enabled
def test_apparmor_enabled(mock_os_path_exists):
    mock_os_path_exists.return_value = True
    collector = ApparmorFactCollector()
    facts = collector.collect()
    assert facts['apparmor']['status'] == 'enabled'
    mock_os_path_exists.assert_called_once_with('/sys/kernel/security/apparmor')

# Test when apparmor is disabled
def test_apparmor_disabled(mock_os_path_exists):
    mock_os_path_exists.return_value = False
    collector = ApparmorFactCollector()
    facts = collector.collect()
    assert facts['apparmor']['status'] == 'disabled'
    mock_os_path_exists.assert_called_once_with('/sys/kernel/security/apparmor')
