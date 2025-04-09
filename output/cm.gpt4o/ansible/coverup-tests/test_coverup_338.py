# file lib/ansible/module_utils/facts/system/apparmor.py:26-39
# lines [26, 27, 28, 30, 31, 32, 33, 34, 36, 38, 39]
# branches ['33->34', '33->36']

import os
import pytest
from unittest.mock import patch
from ansible.module_utils.facts.system.apparmor import ApparmorFactCollector

@pytest.fixture
def mock_os_path_exists(mocker):
    original_os_path_exists = os.path.exists
    mocker.patch('os.path.exists')
    yield os.path.exists
    os.path.exists = original_os_path_exists

def test_apparmor_enabled(mock_os_path_exists):
    mock_os_path_exists.return_value = True
    collector = ApparmorFactCollector()
    facts = collector.collect()
    assert facts['apparmor']['status'] == 'enabled'

def test_apparmor_disabled(mock_os_path_exists):
    mock_os_path_exists.return_value = False
    collector = ApparmorFactCollector()
    facts = collector.collect()
    assert facts['apparmor']['status'] == 'disabled'
