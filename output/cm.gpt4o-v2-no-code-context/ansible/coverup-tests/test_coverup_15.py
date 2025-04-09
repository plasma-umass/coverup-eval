# file: lib/ansible/module_utils/facts/virtual/hpux.py:25-67
# asked: {"lines": [25, 26, 31, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67], "branches": [[38, 39], [38, 44], [40, 41], [40, 44], [44, 45], [44, 58], [46, 47], [46, 50], [50, 51], [50, 54], [54, 55], [54, 58], [58, 59], [58, 65], [60, 61], [60, 65]]}
# gained: {"lines": [25, 26, 31, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67], "branches": [[38, 39], [38, 44], [40, 41], [44, 45], [44, 58], [46, 47], [46, 50], [50, 51], [50, 54], [54, 55], [58, 59], [58, 65], [60, 61]]}

import pytest
import os
import re
from unittest.mock import MagicMock, patch

# Assuming the HPUXVirtual class is imported from the module
from ansible.module_utils.facts.virtual.hpux import HPUXVirtual

@pytest.fixture
def hpux_virtual():
    module = MagicMock()
    return HPUXVirtual(module)

def test_vecheck_exists_and_succeeds(hpux_virtual, monkeypatch):
    def mock_exists(path):
        return path == '/usr/sbin/vecheck'

    def mock_run_command(cmd):
        return (0, 'output', '')

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(hpux_virtual.module, 'run_command', mock_run_command)

    virtual_facts = hpux_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'
    assert 'HP vPar' in virtual_facts['virtualization_tech_guest']

def test_hpvminfo_exists_and_matches_vpar(hpux_virtual, monkeypatch):
    def mock_exists(path):
        return path == '/opt/hpvm/bin/hpvminfo'

    def mock_run_command(cmd):
        return (0, 'Running HPVM vPar', '')

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(hpux_virtual.module, 'run_command', mock_run_command)

    virtual_facts = hpux_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HPVM vPar'
    assert 'HPVM vPar' in virtual_facts['virtualization_tech_guest']

def test_hpvminfo_exists_and_matches_ivm(hpux_virtual, monkeypatch):
    def mock_exists(path):
        return path == '/opt/hpvm/bin/hpvminfo'

    def mock_run_command(cmd):
        return (0, 'Running HPVM guest', '')

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(hpux_virtual.module, 'run_command', mock_run_command)

    virtual_facts = hpux_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HPVM IVM'
    assert 'HPVM IVM' in virtual_facts['virtualization_tech_guest']

def test_hpvminfo_exists_and_matches_host(hpux_virtual, monkeypatch):
    def mock_exists(path):
        return path == '/opt/hpvm/bin/hpvminfo'

    def mock_run_command(cmd):
        return (0, 'Running HPVM host', '')

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(hpux_virtual.module, 'run_command', mock_run_command)

    virtual_facts = hpux_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'host'
    assert virtual_facts['virtualization_role'] == 'HPVM'
    assert 'HPVM' in virtual_facts['virtualization_tech_guest']

def test_parstatus_exists_and_succeeds(hpux_virtual, monkeypatch):
    def mock_exists(path):
        return path == '/usr/sbin/parstatus'

    def mock_run_command(cmd):
        return (0, 'output', '')

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(hpux_virtual.module, 'run_command', mock_run_command)

    virtual_facts = hpux_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP nPar'
    assert 'HP nPar' in virtual_facts['virtualization_tech_guest']

def test_no_virtualization_tools_exist(hpux_virtual, monkeypatch):
    def mock_exists(path):
        return False

    monkeypatch.setattr(os.path, 'exists', mock_exists)

    virtual_facts = hpux_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()
