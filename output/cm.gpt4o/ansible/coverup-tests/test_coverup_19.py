# file lib/ansible/module_utils/facts/virtual/hpux.py:25-67
# lines [25, 26, 31, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67]
# branches ['38->39', '38->44', '40->41', '40->44', '44->45', '44->58', '46->47', '46->50', '50->51', '50->54', '54->55', '54->58', '58->59', '58->65', '60->61', '60->65']

import os
import re
import pytest
from unittest.mock import patch, MagicMock

# Assuming the HPUXVirtual class is imported from ansible.module_utils.facts.virtual.hpux
from ansible.module_utils.facts.virtual.hpux import HPUXVirtual

@pytest.fixture
def mock_module():
    return MagicMock()

@pytest.fixture
def hpux_virtual(mock_module):
    return HPUXVirtual(module=mock_module)

def test_get_virtual_facts_vecheck(hpux_virtual, mocker):
    mocker.patch('os.path.exists', side_effect=lambda path: path == '/usr/sbin/vecheck')
    hpux_virtual.module.run_command.return_value = (0, '', '')

    virtual_facts = hpux_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP vPar'
    assert 'HP vPar' in virtual_facts['virtualization_tech_guest']

def test_get_virtual_facts_hpvminfo_vpar(hpux_virtual, mocker):
    mocker.patch('os.path.exists', side_effect=lambda path: path == '/opt/hpvm/bin/hpvminfo')
    hpux_virtual.module.run_command.return_value = (0, 'Running HPVM vPar', '')

    virtual_facts = hpux_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HPVM vPar'
    assert 'HPVM vPar' in virtual_facts['virtualization_tech_guest']

def test_get_virtual_facts_hpvminfo_ivm(hpux_virtual, mocker):
    mocker.patch('os.path.exists', side_effect=lambda path: path == '/opt/hpvm/bin/hpvminfo')
    hpux_virtual.module.run_command.return_value = (0, 'Running HPVM guest', '')

    virtual_facts = hpux_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HPVM IVM'
    assert 'HPVM IVM' in virtual_facts['virtualization_tech_guest']

def test_get_virtual_facts_hpvminfo_host(hpux_virtual, mocker):
    mocker.patch('os.path.exists', side_effect=lambda path: path == '/opt/hpvm/bin/hpvminfo')
    hpux_virtual.module.run_command.return_value = (0, 'Running HPVM host', '')

    virtual_facts = hpux_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'host'
    assert virtual_facts['virtualization_role'] == 'HPVM'
    assert 'HPVM' in virtual_facts['virtualization_tech_guest']

def test_get_virtual_facts_parstatus(hpux_virtual, mocker):
    mocker.patch('os.path.exists', side_effect=lambda path: path == '/usr/sbin/parstatus')
    hpux_virtual.module.run_command.return_value = (0, '', '')

    virtual_facts = hpux_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'guest'
    assert virtual_facts['virtualization_role'] == 'HP nPar'
    assert 'HP nPar' in virtual_facts['virtualization_tech_guest']
