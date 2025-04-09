# file: lib/ansible/module_utils/facts/virtual/netbsd.py:25-68
# asked: {"lines": [29, 30, 31, 34, 35, 37, 38, 39, 40, 42, 43, 44, 46, 47, 52, 53, 54, 56, 57, 59, 60, 62, 63, 64, 66, 67, 68], "branches": [[46, 47], [46, 52], [56, 57], [56, 59], [59, 60], [59, 66], [62, 63], [62, 66]]}
# gained: {"lines": [29, 30, 31, 34, 35, 37, 38, 39, 40, 42, 43, 44, 46, 47, 52, 53, 54, 56, 57, 59, 60, 62, 63, 64, 66, 67, 68], "branches": [[46, 47], [46, 52], [56, 57], [56, 59], [59, 60], [59, 66], [62, 63]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual

@pytest.fixture
def netbsd_virtual():
    return NetBSDVirtual(module=MagicMock())

def test_get_virtual_facts_default(netbsd_virtual):
    with patch('os.path.exists', return_value=False):
        netbsd_virtual.detect_virt_product = MagicMock(return_value={
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set()
        })
        netbsd_virtual.detect_virt_vendor = MagicMock(return_value={
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set()
        })
        facts = netbsd_virtual.get_virtual_facts()
        assert facts['virtualization_type'] == ''
        assert facts['virtualization_role'] == ''
        assert facts['virtualization_tech_guest'] == set()
        assert facts['virtualization_tech_host'] == set()

def test_get_virtual_facts_with_xen(netbsd_virtual):
    with patch('os.path.exists', return_value=True):
        netbsd_virtual.detect_virt_product = MagicMock(return_value={
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set()
        })
        netbsd_virtual.detect_virt_vendor = MagicMock(return_value={
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set()
        })
        facts = netbsd_virtual.get_virtual_facts()
        assert facts['virtualization_type'] == 'xen'
        assert facts['virtualization_role'] == 'guest'
        assert 'xen' in facts['virtualization_tech_guest']

def test_get_virtual_facts_detect_virt_product(netbsd_virtual):
    with patch('os.path.exists', return_value=False):
        netbsd_virtual.detect_virt_product = MagicMock(return_value={
            'virtualization_type': 'kvm',
            'virtualization_role': 'guest',
            'virtualization_tech_guest': {'kvm'},
            'virtualization_tech_host': set()
        })
        netbsd_virtual.detect_virt_vendor = MagicMock(return_value={
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set()
        })
        facts = netbsd_virtual.get_virtual_facts()
        assert facts['virtualization_type'] == 'kvm'
        assert facts['virtualization_role'] == 'guest'
        assert 'kvm' in facts['virtualization_tech_guest']

def test_get_virtual_facts_detect_virt_vendor(netbsd_virtual):
    with patch('os.path.exists', return_value=False):
        netbsd_virtual.detect_virt_product = MagicMock(return_value={
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set()
        })
        netbsd_virtual.detect_virt_vendor = MagicMock(side_effect=[
            {
                'virtualization_tech_guest': set(),
                'virtualization_tech_host': set()
            },
            {
                'virtualization_type': 'vmm',
                'virtualization_role': 'guest',
                'virtualization_tech_guest': {'vmm'},
                'virtualization_tech_host': set()
            }
        ])
        facts = netbsd_virtual.get_virtual_facts()
        assert facts['virtualization_type'] == 'vmm'
        assert facts['virtualization_role'] == 'guest'
        assert 'vmm' in facts['virtualization_tech_guest']
