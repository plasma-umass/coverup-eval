# file: lib/ansible/module_utils/facts/hardware/netbsd.py:67-99
# asked: {"lines": [67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 99], "branches": [[73, 74], [73, 75], [76, 77], [76, 92], [81, 82], [81, 86], [82, 83], [82, 84], [86, 87], [86, 90], [88, 76], [88, 89], [90, 76], [90, 91], [92, 93], [92, 96]]}
# gained: {"lines": [67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 99], "branches": [[73, 74], [73, 75], [76, 77], [76, 92], [81, 82], [81, 86], [82, 84], [86, 87], [86, 90], [88, 76], [88, 89], [90, 76], [90, 91], [92, 93], [92, 96]]}

import os
import pytest
from unittest.mock import patch, mock_open, MagicMock
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware

@pytest.fixture
def netbsd_hardware():
    module = MagicMock()
    return NetBSDHardware(module)

def test_get_cpu_facts_no_access(monkeypatch, netbsd_hardware):
    def mock_access(path, mode):
        return False

    monkeypatch.setattr(os, 'access', mock_access)
    cpu_facts = netbsd_hardware.get_cpu_facts()
    assert cpu_facts == {}

def test_get_cpu_facts_with_data(monkeypatch, netbsd_hardware):
    cpuinfo_content = """\
processor   : 0
model name  : Intel(R) Xeon(R) CPU
physical id : 0
cpu cores   : 4
processor   : 1
model name  : Intel(R) Xeon(R) CPU
physical id : 0
cpu cores   : 4
"""
    monkeypatch.setattr(os, 'access', lambda path, mode: True)
    monkeypatch.setattr('builtins.open', mock_open(read_data=cpuinfo_content))
    monkeypatch.setattr('ansible.module_utils.facts.utils.get_file_lines', lambda path: cpuinfo_content.splitlines())

    cpu_facts = netbsd_hardware.get_cpu_facts()
    assert cpu_facts['processor'] == ['Intel(R) Xeon(R) CPU', 'Intel(R) Xeon(R) CPU']
    assert cpu_facts['processor_count'] == 1
    assert cpu_facts['processor_cores'] == 4

def test_get_cpu_facts_no_sockets(monkeypatch, netbsd_hardware):
    cpuinfo_content = """\
processor   : 0
model name  : Intel(R) Xeon(R) CPU
"""
    monkeypatch.setattr(os, 'access', lambda path, mode: True)
    monkeypatch.setattr('builtins.open', mock_open(read_data=cpuinfo_content))
    monkeypatch.setattr('ansible.module_utils.facts.utils.get_file_lines', lambda path: cpuinfo_content.splitlines())

    cpu_facts = netbsd_hardware.get_cpu_facts()
    assert cpu_facts['processor'] == ['Intel(R) Xeon(R) CPU']
    assert cpu_facts['processor_count'] == 1
    assert cpu_facts['processor_cores'] == 'NA'
