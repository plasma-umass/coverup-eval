# file: lib/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [42], "branches": [[41, 42]]}
# gained: {"lines": [42], "branches": [[41, 42]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.sysctl import get_sysctl

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    return module

def test_get_sysctl_success(mock_module):
    mock_module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n', '')
    prefixes = ['net.ipv4.ip_forward', 'kernel.hostname']
    
    result = get_sysctl(mock_module, prefixes)
    
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost'
    }

def test_get_sysctl_multiline_value(mock_module):
    mock_module.run_command.return_value = (0, 'kernel.core_pattern = |/usr/share/apport/apport %p %s %c %d %P %E\n foo\n bar\n', '')
    prefixes = ['kernel.core_pattern']
    
    result = get_sysctl(mock_module, prefixes)
    
    assert result == {
        'kernel.core_pattern': '|/usr/share/apport/apport %p %s %c %d %P %E\n foo\n bar'
    }

def test_get_sysctl_empty_line(mock_module):
    mock_module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\n\nkernel.hostname = myhost\n', '')
    prefixes = ['net.ipv4.ip_forward', 'kernel.hostname']
    
    result = get_sysctl(mock_module, prefixes)
    
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost'
    }

def test_get_sysctl_split_error(mock_module):
    mock_module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\ninvalid_line\nkernel.hostname = myhost\n', '')
    prefixes = ['net.ipv4.ip_forward', 'kernel.hostname']
    
    with patch.object(mock_module, 'warn') as mock_warn:
        result = get_sysctl(mock_module, prefixes)
        mock_warn.assert_called_once_with('Unable to split sysctl line (invalid_line): not enough values to unpack (expected 2, got 1)')
    
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost'
    }

def test_get_sysctl_command_failure(mock_module):
    mock_module.run_command.return_value = (1, '', 'error')
    prefixes = ['net.ipv4.ip_forward', 'kernel.hostname']
    
    result = get_sysctl(mock_module, prefixes)
    
    assert result == {}

def test_get_sysctl_ioerror(mock_module):
    mock_module.run_command.side_effect = IOError('IOError')
    prefixes = ['net.ipv4.ip_forward', 'kernel.hostname']
    
    with patch.object(mock_module, 'warn') as mock_warn:
        result = get_sysctl(mock_module, prefixes)
        mock_warn.assert_called_once_with('Unable to read sysctl: IOError')
    
    assert result == {}

def test_get_sysctl_oserror(mock_module):
    mock_module.run_command.side_effect = OSError('OSError')
    prefixes = ['net.ipv4.ip_forward', 'kernel.hostname']
    
    with patch.object(mock_module, 'warn') as mock_warn:
        result = get_sysctl(mock_module, prefixes)
        mock_warn.assert_called_once_with('Unable to read sysctl: OSError')
    
    assert result == {}
