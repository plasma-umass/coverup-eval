# file: lib/ansible/module_utils/common/sys_info.py:17-38
# asked: {"lines": [17, 28, 30, 31, 32, 33, 34, 35, 36, 38], "branches": [[30, 31], [30, 38], [31, 32], [31, 33], [33, 34], [33, 35], [35, 36], [35, 38]]}
# gained: {"lines": [17, 28, 30, 31, 32, 33, 34, 35, 36, 38], "branches": [[30, 31], [30, 38], [31, 32], [31, 33], [33, 34], [33, 35], [35, 36], [35, 38]]}

import pytest
import platform
from ansible.module_utils.common.sys_info import get_distribution

def test_get_distribution_linux_amzn(monkeypatch):
    monkeypatch.setattr('distro.id', lambda: 'amzn')
    monkeypatch.setattr('platform.system', lambda: 'Linux')
    assert get_distribution() == 'Amazon'

def test_get_distribution_linux_rhel(monkeypatch):
    monkeypatch.setattr('distro.id', lambda: 'rhel')
    monkeypatch.setattr('platform.system', lambda: 'Linux')
    assert get_distribution() == 'Redhat'

def test_get_distribution_linux_other(monkeypatch):
    monkeypatch.setattr('distro.id', lambda: '')
    monkeypatch.setattr('platform.system', lambda: 'Linux')
    assert get_distribution() == 'OtherLinux'

def test_get_distribution_linux_unknown(monkeypatch):
    monkeypatch.setattr('distro.id', lambda: 'unknown')
    monkeypatch.setattr('platform.system', lambda: 'Linux')
    assert get_distribution() == 'Unknown'

def test_get_distribution_non_linux(monkeypatch):
    monkeypatch.setattr('distro.id', lambda: 'nonlinux')
    monkeypatch.setattr('platform.system', lambda: 'Windows')
    assert get_distribution() == 'Nonlinux'
