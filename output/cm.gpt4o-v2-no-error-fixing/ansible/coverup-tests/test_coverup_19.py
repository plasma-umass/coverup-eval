# file: lib/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [24, 25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}
# gained: {"lines": [24, 25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.sysctl import get_sysctl

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    return module

def test_get_sysctl_success(mock_module):
    mock_module.run_command.return_value = (0, "net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n", "")
    prefixes = ["net.ipv4.ip_forward", "kernel.hostname"]
    
    result = get_sysctl(mock_module, prefixes)
    
    assert result == {
        "net.ipv4.ip_forward": "1",
        "kernel.hostname": "myhost"
    }

def test_get_sysctl_ioerror(mock_module):
    mock_module.run_command.side_effect = IOError("Test IOError")
    prefixes = ["net.ipv4.ip_forward"]
    
    result = get_sysctl(mock_module, prefixes)
    
    assert result == {}

def test_get_sysctl_oserror(mock_module):
    mock_module.run_command.side_effect = OSError("Test OSError")
    prefixes = ["net.ipv4.ip_forward"]
    
    result = get_sysctl(mock_module, prefixes)
    
    assert result == {}

def test_get_sysctl_multiline_value(mock_module):
    mock_module.run_command.return_value = (0, "kernel.core_pattern = |/usr/lib/systemd/systemd-coredump %p %u %g %s %t %e\n foo\n bar\n", "")
    prefixes = ["kernel.core_pattern"]
    
    result = get_sysctl(mock_module, prefixes)
    
    assert result == {
        "kernel.core_pattern": "|/usr/lib/systemd/systemd-coredump %p %u %g %s %t %e\n foo\n bar"
    }

def test_get_sysctl_split_error(mock_module):
    mock_module.run_command.return_value = (0, "invalid line without equals sign", "")
    prefixes = ["invalid"]
    
    result = get_sysctl(mock_module, prefixes)
    
    assert result == {}
