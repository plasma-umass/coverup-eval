# file: lib/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [24, 25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}
# gained: {"lines": [24, 25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 44, 48, 49, 51, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 44], [44, 48], [44, 51], [51, 54], [59, 60], [59, 62]]}

import pytest
import re
from unittest.mock import Mock

# Mock module to simulate Ansible module behavior
class MockModule:
    def get_bin_path(self, binary):
        return f"/usr/sbin/{binary}"

    def run_command(self, cmd):
        if cmd == ["/usr/sbin/sysctl", "net.ipv4.ip_forward"]:
            return 0, "net.ipv4.ip_forward = 1\n", ""
        elif cmd == ["/usr/sbin/sysctl", "net.ipv4.conf.all.rp_filter"]:
            return 0, "net.ipv4.conf.all.rp_filter = 1\n net.ipv4.conf.all.rp_filter = 2\n", ""
        elif cmd == ["/usr/sbin/sysctl", "invalid"]:
            return 1, "", "error"
        else:
            raise IOError("Command not found")

    def warn(self, msg):
        print(f"Warning: {msg}")

@pytest.fixture
def module():
    return MockModule()

def test_get_sysctl_single_line(module):
    from ansible.module_utils.facts.sysctl import get_sysctl
    result = get_sysctl(module, ["net.ipv4.ip_forward"])
    assert result == {"net.ipv4.ip_forward": "1"}

def test_get_sysctl_multiline(module):
    from ansible.module_utils.facts.sysctl import get_sysctl
    result = get_sysctl(module, ["net.ipv4.conf.all.rp_filter"])
    assert result == {"net.ipv4.conf.all.rp_filter": "1\n net.ipv4.conf.all.rp_filter = 2"}

def test_get_sysctl_invalid_command(module):
    from ansible.module_utils.facts.sysctl import get_sysctl
    result = get_sysctl(module, ["invalid"])
    assert result == {}

def test_get_sysctl_ioerror(module, monkeypatch):
    from ansible.module_utils.facts.sysctl import get_sysctl

    def mock_run_command(cmd):
        raise IOError("IOError")

    monkeypatch.setattr(module, "run_command", mock_run_command)
    result = get_sysctl(module, ["net.ipv4.ip_forward"])
    assert result == {}

def test_get_sysctl_oserror(module, monkeypatch):
    from ansible.module_utils.facts.sysctl import get_sysctl

    def mock_run_command(cmd):
        raise OSError("OSError")

    monkeypatch.setattr(module, "run_command", mock_run_command)
    result = get_sysctl(module, ["net.ipv4.ip_forward"])
    assert result == {}

def test_get_sysctl_split_error(module, monkeypatch):
    from ansible.module_utils.facts.sysctl import get_sysctl

    def mock_run_command(cmd):
        return 0, "invalid_line_without_equals", ""

    monkeypatch.setattr(module, "run_command", mock_run_command)
    result = get_sysctl(module, ["net.ipv4.ip_forward"])
    assert result == {}
