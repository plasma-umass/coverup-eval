# file: lib/ansible/module_utils/facts/virtual/hpux.py:25-67
# asked: {"lines": [], "branches": [[40, 44], [54, 58], [60, 65]]}
# gained: {"lines": [], "branches": [[40, 44], [54, 58], [60, 65]]}

import os
import re
import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.virtual.hpux import HPUXVirtual

@pytest.fixture
def hpux_virtual():
    module = Mock()
    return HPUXVirtual(module)

def test_vecheck_exists_and_succeeds(hpux_virtual):
    with patch('os.path.exists', side_effect=lambda x: x == '/usr/sbin/vecheck' or x == '/opt/hpvm/bin/hpvminfo' or x == '/usr/sbin/parstatus'), \
         patch.object(hpux_virtual.module, 'run_command', side_effect=[
             (0, '', ''),  # vecheck
             (1, '', ''),  # hpvminfo
             (1, '', '')   # parstatus
         ]):
        facts = hpux_virtual.get_virtual_facts()
        assert facts['virtualization_type'] == 'guest'
        assert facts['virtualization_role'] == 'HP vPar'
        assert 'HP vPar' in facts['virtualization_tech_guest']

def test_hpvminfo_exists_and_matches_vpar(hpux_virtual):
    with patch('os.path.exists', side_effect=lambda x: x == '/opt/hpvm/bin/hpvminfo' or x == '/usr/sbin/vecheck' or x == '/usr/sbin/parstatus'), \
         patch.object(hpux_virtual.module, 'run_command', side_effect=[
             (1, '', ''),  # vecheck
             (0, 'Running HPVM vPar', ''),  # hpvminfo
             (1, '', '')   # parstatus
         ]):
        facts = hpux_virtual.get_virtual_facts()
        assert facts['virtualization_type'] == 'guest'
        assert facts['virtualization_role'] == 'HPVM vPar'
        assert 'HPVM vPar' in facts['virtualization_tech_guest']

def test_hpvminfo_exists_and_matches_guest(hpux_virtual):
    with patch('os.path.exists', side_effect=lambda x: x == '/opt/hpvm/bin/hpvminfo' or x == '/usr/sbin/vecheck' or x == '/usr/sbin/parstatus'), \
         patch.object(hpux_virtual.module, 'run_command', side_effect=[
             (1, '', ''),  # vecheck
             (0, 'Running HPVM guest', ''),  # hpvminfo
             (1, '', '')   # parstatus
         ]):
        facts = hpux_virtual.get_virtual_facts()
        assert facts['virtualization_type'] == 'guest'
        assert facts['virtualization_role'] == 'HPVM IVM'
        assert 'HPVM IVM' in facts['virtualization_tech_guest']

def test_hpvminfo_exists_and_matches_host(hpux_virtual):
    with patch('os.path.exists', side_effect=lambda x: x == '/opt/hpvm/bin/hpvminfo' or x == '/usr/sbin/vecheck' or x == '/usr/sbin/parstatus'), \
         patch.object(hpux_virtual.module, 'run_command', side_effect=[
             (1, '', ''),  # vecheck
             (0, 'Running HPVM host', ''),  # hpvminfo
             (1, '', '')   # parstatus
         ]):
        facts = hpux_virtual.get_virtual_facts()
        assert facts['virtualization_type'] == 'host'
        assert facts['virtualization_role'] == 'HPVM'
        assert 'HPVM' in facts['virtualization_tech_guest']

def test_parstatus_exists_and_succeeds(hpux_virtual):
    with patch('os.path.exists', side_effect=lambda x: x == '/usr/sbin/parstatus' or x == '/usr/sbin/vecheck' or x == '/opt/hpvm/bin/hpvminfo'), \
         patch.object(hpux_virtual.module, 'run_command', side_effect=[
             (1, '', ''),  # vecheck
             (1, '', ''),  # hpvminfo
             (0, '', '')   # parstatus
         ]):
        facts = hpux_virtual.get_virtual_facts()
        assert facts['virtualization_type'] == 'guest'
        assert facts['virtualization_role'] == 'HP nPar'
        assert 'HP nPar' in facts['virtualization_tech_guest']
