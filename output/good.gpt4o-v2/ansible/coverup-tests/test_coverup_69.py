# file: lib/ansible/module_utils/facts/virtual/openbsd.py:27-69
# asked: {"lines": [27, 28, 33, 34, 36, 37, 38, 39, 42, 43, 45, 46, 47, 48, 50, 51, 52, 54, 55, 59, 60, 61, 62, 63, 64, 65, 67, 68, 69], "branches": [[54, 55], [54, 59], [60, 61], [60, 67], [62, 60], [62, 63]]}
# gained: {"lines": [27, 28, 33, 34, 36, 37, 38, 39, 42, 43, 45, 46, 47, 48, 50, 51, 52, 54, 55, 59, 60, 61, 62, 63, 64, 65, 67, 68, 69], "branches": [[54, 55], [60, 61], [60, 67], [62, 63]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtual

@pytest.fixture
def openbsd_virtual():
    module = MagicMock()
    return OpenBSDVirtual(module)

def test_get_virtual_facts_no_virtualization(openbsd_virtual):
    with patch('ansible.module_utils.facts.virtual.openbsd.get_file_content', return_value=''):
        with patch.object(openbsd_virtual, 'detect_virt_product', return_value={
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set(),
            'virtualization_type': '',
            'virtualization_role': ''
        }):
            with patch.object(openbsd_virtual, 'detect_virt_vendor', return_value={
                'virtualization_tech_guest': set(),
                'virtualization_tech_host': set(),
                'virtualization_type': '',
                'virtualization_role': ''
            }):
                virtual_facts = openbsd_virtual.get_virtual_facts()
                assert virtual_facts['virtualization_type'] == ''
                assert virtual_facts['virtualization_role'] == ''
                assert virtual_facts['virtualization_tech_guest'] == set()
                assert virtual_facts['virtualization_tech_host'] == set()

def test_get_virtual_facts_with_vmm_host(openbsd_virtual):
    dmesg_content = 'vmm0 at mainbus0: VMX/EPT'
    with patch('ansible.module_utils.facts.virtual.openbsd.get_file_content', return_value=dmesg_content):
        with patch.object(openbsd_virtual, 'detect_virt_product', return_value={
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set(),
            'virtualization_type': '',
            'virtualization_role': ''
        }):
            with patch.object(openbsd_virtual, 'detect_virt_vendor', return_value={
                'virtualization_tech_guest': set(),
                'virtualization_tech_host': set(),
                'virtualization_type': '',
                'virtualization_role': ''
            }):
                virtual_facts = openbsd_virtual.get_virtual_facts()
                assert virtual_facts['virtualization_type'] == 'vmm'
                assert virtual_facts['virtualization_role'] == 'host'
                assert 'vmm' in virtual_facts['virtualization_tech_host']
                assert virtual_facts['virtualization_tech_guest'] == set()

def test_get_virtual_facts_with_guest_tech(openbsd_virtual):
    with patch('ansible.module_utils.facts.virtual.openbsd.get_file_content', return_value=''):
        with patch.object(openbsd_virtual, 'detect_virt_product', return_value={
            'virtualization_tech_guest': {'kvm'},
            'virtualization_tech_host': set(),
            'virtualization_type': '',
            'virtualization_role': ''
        }):
            with patch.object(openbsd_virtual, 'detect_virt_vendor', return_value={
                'virtualization_tech_guest': {'kvm'},
                'virtualization_tech_host': set(),
                'virtualization_type': '',
                'virtualization_role': ''
            }):
                virtual_facts = openbsd_virtual.get_virtual_facts()
                assert virtual_facts['virtualization_type'] == ''
                assert virtual_facts['virtualization_role'] == ''
                assert virtual_facts['virtualization_tech_guest'] == {'kvm'}
                assert virtual_facts['virtualization_tech_host'] == set()
