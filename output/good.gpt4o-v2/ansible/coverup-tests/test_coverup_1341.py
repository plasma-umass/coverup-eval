# file: lib/ansible/module_utils/facts/system/caps.py:25-55
# asked: {"lines": [31, 32, 33, 35, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 52, 53, 55], "branches": [[32, 33], [32, 35], [37, 39], [37, 55], [42, 43], [42, 52], [43, 44], [43, 45], [45, 42], [45, 46], [46, 47], [46, 49]]}
# gained: {"lines": [31, 32, 33, 35, 37, 39, 40, 41, 42, 43, 45, 46, 47, 49, 50, 52, 53, 55], "branches": [[32, 33], [32, 35], [37, 39], [37, 55], [42, 43], [42, 52], [43, 45], [45, 46], [46, 47], [46, 49]]}

import pytest
from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
from unittest.mock import Mock

@pytest.fixture
def mock_module():
    return Mock()

def test_collect_no_module():
    collector = SystemCapabilitiesFactCollector()
    result = collector.collect()
    assert result == {}

def test_collect_no_capsh_path(mock_module):
    mock_module.get_bin_path.return_value = None
    collector = SystemCapabilitiesFactCollector()
    result = collector.collect(module=mock_module)
    assert result == {}

def test_collect_with_capsh_path_no_output(mock_module):
    mock_module.get_bin_path.return_value = '/usr/bin/capsh'
    mock_module.run_command.return_value = (0, '', '')
    collector = SystemCapabilitiesFactCollector()
    result = collector.collect(module=mock_module)
    assert result == {
        'system_capabilities_enforced': 'NA',
        'system_capabilities': []
    }

def test_collect_with_capsh_path_enforced_false(mock_module):
    mock_module.get_bin_path.return_value = '/usr/bin/capsh'
    mock_module.run_command.return_value = (0, 'Current: =ep\n', '')
    collector = SystemCapabilitiesFactCollector()
    result = collector.collect(module=mock_module)
    assert result == {
        'system_capabilities_enforced': 'False',
        'system_capabilities': []
    }

def test_collect_with_capsh_path_enforced_true(mock_module):
    mock_module.get_bin_path.return_value = '/usr/bin/capsh'
    mock_module.run_command.return_value = (0, 'Current: cap_net_bind_service=ep\n', '')
    collector = SystemCapabilitiesFactCollector()
    result = collector.collect(module=mock_module)
    assert result == {
        'system_capabilities_enforced': 'True',
        'system_capabilities': ['ep']
    }
