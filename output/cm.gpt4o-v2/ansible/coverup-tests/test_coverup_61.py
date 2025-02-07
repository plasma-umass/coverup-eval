# file: lib/ansible/module_utils/facts/virtual/netbsd.py:25-68
# asked: {"lines": [25, 26, 28, 29, 30, 31, 34, 35, 37, 38, 39, 40, 42, 43, 44, 46, 47, 52, 53, 54, 56, 57, 59, 60, 62, 63, 64, 66, 67, 68], "branches": [[46, 47], [46, 52], [56, 57], [56, 59], [59, 60], [59, 66], [62, 63], [62, 66]]}
# gained: {"lines": [25, 26, 28, 29, 30, 31, 34, 35, 37, 38, 39, 40, 42, 43, 44, 46, 47, 52, 53, 54, 56, 57, 59, 60, 62, 63, 64, 66, 67, 68], "branches": [[46, 47], [46, 52], [56, 57], [56, 59], [59, 60], [59, 66], [62, 63]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual

@pytest.fixture
def netbsd_virtual(mocker):
    module_mock = mocker.Mock()
    return NetBSDVirtual(module_mock)

def test_get_virtual_facts_machdep_dmi_system_product(netbsd_virtual, mocker):
    mocker.patch.object(netbsd_virtual, 'detect_virt_product', return_value={
        'virtualization_tech_guest': {'tech_guest_1'},
        'virtualization_tech_host': {'tech_host_1'},
        'virtualization_type': 'type1',
        'virtualization_role': 'role1'
    })
    mocker.patch.object(netbsd_virtual, 'detect_virt_vendor', return_value={
        'virtualization_tech_guest': {'tech_guest_2'},
        'virtualization_tech_host': {'tech_host_2'}
    })
    mocker.patch('os.path.exists', return_value=False)

    virtual_facts = netbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'type1'
    assert virtual_facts['virtualization_role'] == 'role1'
    assert virtual_facts['virtualization_tech_guest'] == {'tech_guest_1', 'tech_guest_2'}
    assert virtual_facts['virtualization_tech_host'] == {'tech_host_1', 'tech_host_2'}

def test_get_virtual_facts_machdep_hypervisor(netbsd_virtual, mocker):
    mocker.patch.object(netbsd_virtual, 'detect_virt_product', return_value={
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
        'virtualization_type': '',
        'virtualization_role': ''
    })
    mocker.patch.object(netbsd_virtual, 'detect_virt_vendor', side_effect=[
        {
            'virtualization_tech_guest': {'tech_guest_1'},
            'virtualization_tech_host': {'tech_host_1'}
        },
        {
            'virtualization_tech_guest': {'tech_guest_2'},
            'virtualization_tech_host': {'tech_host_2'}
        }
    ])
    mocker.patch('os.path.exists', return_value=False)

    virtual_facts = netbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_guest'] == {'tech_guest_1', 'tech_guest_2'}
    assert virtual_facts['virtualization_tech_host'] == {'tech_host_1', 'tech_host_2'}

def test_get_virtual_facts_xen_guest(netbsd_virtual, mocker):
    mocker.patch.object(netbsd_virtual, 'detect_virt_product', return_value={
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
        'virtualization_type': '',
        'virtualization_role': ''
    })
    mocker.patch.object(netbsd_virtual, 'detect_virt_vendor', return_value={
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    })
    mocker.patch('os.path.exists', return_value=True)

    virtual_facts = netbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_tech_guest'] == {'xen'}
    assert virtual_facts['virtualization_tech_host'] == set()
