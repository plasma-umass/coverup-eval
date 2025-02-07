# file: lib/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [33, 34, 35, 42, 48, 49, 52, 56, 57], "branches": [[37, 62], [41, 42], [44, 48], [51, 52], [59, 62]]}
# gained: {"lines": [33, 34, 35, 42, 48, 49, 52, 56, 57], "branches": [[37, 62], [41, 42], [44, 48], [51, 52], [59, 62]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.sysctl import get_sysctl

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    return module

def test_get_sysctl_ioerror(mock_module):
    mock_module.run_command.side_effect = IOError("Test IOError")
    result = get_sysctl(mock_module, ['net.ipv4.ip_forward'])
    mock_module.warn.assert_called_once_with('Unable to read sysctl: Test IOError')
    assert result == {}

def test_get_sysctl_oserror(mock_module):
    mock_module.run_command.side_effect = OSError("Test OSError")
    result = get_sysctl(mock_module, ['net.ipv4.ip_forward'])
    mock_module.warn.assert_called_once_with('Unable to read sysctl: Test OSError')
    assert result == {}

def test_get_sysctl_empty_line(mock_module):
    mock_module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\n\nnet.ipv4.conf.all.forwarding = 0', '')
    result = get_sysctl(mock_module, ['net.ipv4.ip_forward'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'net.ipv4.conf.all.forwarding': '0'
    }

def test_get_sysctl_multiline_value(mock_module):
    mock_module.run_command.return_value = (0, 'kernel.core_pattern = |/usr/lib/systemd/systemd-coredump\n foo\n bar', '')
    result = get_sysctl(mock_module, ['kernel.core_pattern'])
    assert result == {
        'kernel.core_pattern': '|/usr/lib/systemd/systemd-coredump\n foo\n bar'
    }

def test_get_sysctl_split_exception(mock_module):
    mock_module.run_command.return_value = (0, 'invalid line without separator', '')
    result = get_sysctl(mock_module, ['net.ipv4.ip_forward'])
    mock_module.warn.assert_called_once_with('Unable to split sysctl line (invalid line without separator): not enough values to unpack (expected 2, got 1)')
    assert result == {}

def test_get_sysctl_final_key_value(mock_module):
    mock_module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1', '')
    result = get_sysctl(mock_module, ['net.ipv4.ip_forward'])
    assert result == {
        'net.ipv4.ip_forward': '1'
    }
