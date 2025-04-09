# file: lib/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [33, 34, 35, 42, 48, 49, 56, 57], "branches": [[37, 62], [41, 42], [44, 48], [59, 62]]}
# gained: {"lines": [33, 34, 35, 48, 49, 56, 57], "branches": [[37, 62], [44, 48], [59, 62]]}

import pytest
from unittest.mock import Mock

def test_get_sysctl_success(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.ipv4.conf.all.rp_filter = 1', '')

    from ansible.module_utils.facts.sysctl import get_sysctl
    result = get_sysctl(module, ['net.ipv4'])

    assert result == {
        'net.ipv4.ip_forward': '1',
        'net.ipv4.conf.all.rp_filter': '1'
    }
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', 'net.ipv4'])

def test_get_sysctl_ioerror(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('Test IOError')

    from ansible.module_utils.facts.sysctl import get_sysctl
    result = get_sysctl(module, ['net.ipv4'])

    assert result == {}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', 'net.ipv4'])
    module.warn.assert_called_once_with('Unable to read sysctl: Test IOError')

def test_get_sysctl_oserror(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('Test OSError')

    from ansible.module_utils.facts.sysctl import get_sysctl
    result = get_sysctl(module, ['net.ipv4'])

    assert result == {}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', 'net.ipv4'])
    module.warn.assert_called_once_with('Unable to read sysctl: Test OSError')

def test_get_sysctl_multiline_value(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\n net.ipv4.conf.all.rp_filter = 1', '')

    from ansible.module_utils.facts.sysctl import get_sysctl
    result = get_sysctl(module, ['net.ipv4'])

    assert result == {
        'net.ipv4.ip_forward': '1\n net.ipv4.conf.all.rp_filter = 1'
    }
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', 'net.ipv4'])

def test_get_sysctl_split_error(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'invalid line', '')

    from ansible.module_utils.facts.sysctl import get_sysctl
    result = get_sysctl(module, ['net.ipv4'])

    assert result == {}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', 'net.ipv4'])
    module.warn.assert_called_once()
