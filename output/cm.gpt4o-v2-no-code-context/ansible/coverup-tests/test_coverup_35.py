# file: lib/ansible/module_utils/facts/hardware/netbsd.py:67-99
# asked: {"lines": [67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 99], "branches": [[73, 74], [73, 75], [76, 77], [76, 92], [81, 82], [81, 86], [82, 83], [82, 84], [86, 87], [86, 90], [88, 76], [88, 89], [90, 76], [90, 91], [92, 93], [92, 96]]}
# gained: {"lines": [67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 99], "branches": [[73, 74], [73, 75], [76, 77], [76, 92], [81, 82], [81, 86], [82, 84], [86, 87], [86, 90], [88, 76], [88, 89], [90, 76], [90, 91], [92, 93], [92, 96]]}

import pytest
import os
from unittest.mock import mock_open, patch, MagicMock
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware

@pytest.fixture
def netbsd_hardware():
    module = MagicMock()
    return NetBSDHardware(module)

def test_get_cpu_facts_no_access(monkeypatch, netbsd_hardware):
    def mock_access(path, mode):
        return False

    monkeypatch.setattr(os, 'access', mock_access)
    result = netbsd_hardware.get_cpu_facts()
    assert result == {}

def test_get_cpu_facts_empty_file(monkeypatch, netbsd_hardware):
    def mock_access(path, mode):
        return True

    monkeypatch.setattr(os, 'access', mock_access)
    monkeypatch.setattr('builtins.open', mock_open(read_data=''))
    result = netbsd_hardware.get_cpu_facts()
    assert result == {'processor': [], 'processor_count': 0, 'processor_cores': 'NA'}

def test_get_cpu_facts_with_data(monkeypatch, netbsd_hardware):
    cpuinfo_data = """
    processor   : 0
    model name  : Intel(R) Xeon(R) CPU
    physical id : 0
    cpu cores   : 4
    processor   : 1
    model name  : Intel(R) Xeon(R) CPU
    physical id : 0
    cpu cores   : 4
    """

    def mock_access(path, mode):
        return True

    monkeypatch.setattr(os, 'access', mock_access)
    monkeypatch.setattr('builtins.open', mock_open(read_data=cpuinfo_data))
    result = netbsd_hardware.get_cpu_facts()
    assert result['processor'] == ['Intel(R) Xeon(R) CPU', 'Intel(R) Xeon(R) CPU']
    assert result['processor_count'] == 1
    assert result['processor_cores'] == 4

def test_get_cpu_facts_multiple_sockets(monkeypatch, netbsd_hardware):
    cpuinfo_data = """
    processor   : 0
    model name  : Intel(R) Xeon(R) CPU
    physical id : 0
    cpu cores   : 4
    processor   : 1
    model name  : Intel(R) Xeon(R) CPU
    physical id : 1
    cpu cores   : 4
    """

    def mock_access(path, mode):
        return True

    monkeypatch.setattr(os, 'access', mock_access)
    monkeypatch.setattr('builtins.open', mock_open(read_data=cpuinfo_data))
    result = netbsd_hardware.get_cpu_facts()
    assert result['processor'] == ['Intel(R) Xeon(R) CPU', 'Intel(R) Xeon(R) CPU']
    assert result['processor_count'] == 2
    assert result['processor_cores'] == 8
