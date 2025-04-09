# file: lib/ansible/module_utils/facts/virtual/hpux.py:25-67
# asked: {"lines": [25, 26, 31, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67], "branches": [[38, 39], [38, 44], [40, 41], [40, 44], [44, 45], [44, 58], [46, 47], [46, 50], [50, 51], [50, 54], [54, 55], [54, 58], [58, 59], [58, 65], [60, 61], [60, 65]]}
# gained: {"lines": [25, 26, 31, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67], "branches": [[38, 39], [38, 44], [40, 41], [44, 45], [44, 58], [46, 47], [46, 50], [50, 51], [50, 54], [54, 55], [58, 59], [58, 65], [60, 61]]}

import os
import re
import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.virtual.hpux import HPUXVirtual

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def hpux_virtual(mock_module):
    return HPUXVirtual(module=mock_module)

def test_get_virtual_facts_vecheck_exists(hpux_virtual, mock_module):
    with patch('os.path.exists', side_effect=lambda x: x == '/usr/sbin/vecheck'), \
         patch.object(mock_module, 'run_command', return_value=(0, '', '')):
        facts = hpux_virtual.get_virtual_facts()
        assert facts['virtualization_type'] == 'guest'
        assert facts['virtualization_role'] == 'HP vPar'
        assert 'HP vPar' in facts['virtualization_tech_guest']

def test_get_virtual_facts_hpvminfo_vpar(hpux_virtual, mock_module):
    with patch('os.path.exists', side_effect=lambda x: x == '/opt/hpvm/bin/hpvminfo'), \
         patch.object(mock_module, 'run_command', return_value=(0, 'Running HPVM vPar', '')):
        facts = hpux_virtual.get_virtual_facts()
        assert facts['virtualization_type'] == 'guest'
        assert facts['virtualization_role'] == 'HPVM vPar'
        assert 'HPVM vPar' in facts['virtualization_tech_guest']

def test_get_virtual_facts_hpvminfo_ivm(hpux_virtual, mock_module):
    with patch('os.path.exists', side_effect=lambda x: x == '/opt/hpvm/bin/hpvminfo'), \
         patch.object(mock_module, 'run_command', return_value=(0, 'Running HPVM guest', '')):
        facts = hpux_virtual.get_virtual_facts()
        assert facts['virtualization_type'] == 'guest'
        assert facts['virtualization_role'] == 'HPVM IVM'
        assert 'HPVM IVM' in facts['virtualization_tech_guest']

def test_get_virtual_facts_hpvminfo_host(hpux_virtual, mock_module):
    with patch('os.path.exists', side_effect=lambda x: x == '/opt/hpvm/bin/hpvminfo'), \
         patch.object(mock_module, 'run_command', return_value=(0, 'Running HPVM host', '')):
        facts = hpux_virtual.get_virtual_facts()
        assert facts['virtualization_type'] == 'host'
        assert facts['virtualization_role'] == 'HPVM'
        assert 'HPVM' in facts['virtualization_tech_guest']

def test_get_virtual_facts_parstatus_exists(hpux_virtual, mock_module):
    with patch('os.path.exists', side_effect=lambda x: x == '/usr/sbin/parstatus'), \
         patch.object(mock_module, 'run_command', return_value=(0, '', '')):
        facts = hpux_virtual.get_virtual_facts()
        assert facts['virtualization_type'] == 'guest'
        assert facts['virtualization_role'] == 'HP nPar'
        assert 'HP nPar' in facts['virtualization_tech_guest']

def test_get_virtual_facts_no_virtualization(hpux_virtual, mock_module):
    with patch('os.path.exists', return_value=False):
        facts = hpux_virtual.get_virtual_facts()
        assert 'virtualization_type' not in facts
        assert 'virtualization_role' not in facts
        assert facts['virtualization_tech_guest'] == set()
        assert facts['virtualization_tech_host'] == set()
