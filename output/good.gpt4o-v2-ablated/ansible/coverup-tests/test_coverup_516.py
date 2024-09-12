# file: lib/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [42, 52], "branches": [[41, 42], [51, 52]]}
# gained: {"lines": [52], "branches": [[51, 52]]}

import pytest
import re
from unittest.mock import Mock

def test_get_sysctl_success(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nkernel.hostname = myhost\n', '')

    from ansible.module_utils.facts.sysctl import get_sysctl

    result = get_sysctl(module, ['net.ipv4.ip_forward', 'kernel.hostname'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'kernel.hostname': 'myhost'
    }

def test_get_sysctl_multiline_value(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'kernel.core_pattern = |/usr/lib/systemd/systemd-coredump\n --backtrace\n --max-size\n', '')

    from ansible.module_utils.facts.sysctl import get_sysctl

    result = get_sysctl(module, ['kernel.core_pattern'])
    assert result == {
        'kernel.core_pattern': '|/usr/lib/systemd/systemd-coredump\n --backtrace\n --max-size'
    }

def test_get_sysctl_command_failure(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, '', 'error')

    from ansible.module_utils.facts.sysctl import get_sysctl

    result = get_sysctl(module, ['net.ipv4.ip_forward'])
    assert result == {}

def test_get_sysctl_ioerror(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('mocked error')

    from ansible.module_utils.facts.sysctl import get_sysctl

    result = get_sysctl(module, ['net.ipv4.ip_forward'])
    assert result == {}

def test_get_sysctl_split_error(monkeypatch):
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'invalid line without separator', '')

    from ansible.module_utils.facts.sysctl import get_sysctl

    result = get_sysctl(module, ['net.ipv4.ip_forward'])
    assert result == {}
