# file: lib/ansible/module_utils/facts/virtual/freebsd.py:25-74
# asked: {"lines": [34, 35, 36, 39, 40, 42, 43, 44, 45, 47, 48, 49, 51, 52, 53, 55, 56, 57, 59, 60, 63, 65, 66, 67, 69, 70, 72, 73, 74], "branches": [[42, 43], [42, 47], [59, 60], [59, 65], [69, 70], [69, 72]]}
# gained: {"lines": [34, 35, 36, 39, 40, 42, 43, 44, 45, 47, 48, 49, 51, 52, 53, 55, 56, 57, 59, 60, 63, 65, 66, 67, 69, 70, 72, 73, 74], "branches": [[42, 43], [42, 47], [59, 60], [59, 65], [69, 70], [69, 72]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual

@pytest.fixture
def freebsd_virtual():
    module = MagicMock()
    module.run_command = MagicMock(return_value=(0, '', ''))
    return FreeBSDVirtual(module)

def test_get_virtual_facts_xen(freebsd_virtual):
    with patch('os.path.exists', return_value=True):
        with patch.object(freebsd_virtual, 'detect_virt_product', return_value={'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}):
            virtual_facts = freebsd_virtual.get_virtual_facts()
            assert virtual_facts['virtualization_type'] == 'xen'
            assert virtual_facts['virtualization_role'] == 'guest'
            assert 'xen' in virtual_facts['virtualization_tech_guest']

def test_get_virtual_facts_no_xen(freebsd_virtual):
    with patch('os.path.exists', return_value=False):
        with patch.object(freebsd_virtual, 'detect_virt_product', side_effect=[
            {'virtualization_tech_guest': {'vm_guest'}, 'virtualization_tech_host': set()},
            {'virtualization_tech_guest': set(), 'virtualization_tech_host': {'hv_vendor'}},
            {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}
        ]):
            with patch.object(freebsd_virtual, 'detect_virt_vendor', return_value={'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}):
                virtual_facts = freebsd_virtual.get_virtual_facts()
                assert virtual_facts['virtualization_type'] == ''
                assert virtual_facts['virtualization_role'] == ''
                assert 'vm_guest' in virtual_facts['virtualization_tech_guest']
                assert 'hv_vendor' in virtual_facts['virtualization_tech_host']

def test_get_virtual_facts_update_sysctl(freebsd_virtual):
    with patch('os.path.exists', return_value=False):
        with patch.object(freebsd_virtual, 'detect_virt_product', side_effect=[
            {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()},
            {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()},
            {'virtualization_tech_guest': {'jail'}, 'virtualization_tech_host': set()}
        ]):
            with patch.object(freebsd_virtual, 'detect_virt_vendor', return_value={'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}):
                virtual_facts = freebsd_virtual.get_virtual_facts()
                assert virtual_facts['virtualization_type'] == ''
                assert virtual_facts['virtualization_role'] == ''
                assert 'jail' in virtual_facts['virtualization_tech_guest']
