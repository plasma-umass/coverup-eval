# file lib/ansible/module_utils/facts/virtual/freebsd.py:25-74
# lines [25, 26, 31, 33, 34, 35, 36, 39, 40, 42, 43, 44, 45, 47, 48, 49, 51, 52, 53, 55, 56, 57, 59, 60, 63, 65, 66, 67, 69, 70, 72, 73, 74]
# branches ['42->43', '42->47', '59->60', '59->65', '69->70', '69->72']

import os
import pytest
from unittest.mock import patch, MagicMock

# Assuming the FreeBSDVirtual class is imported from ansible.module_utils.facts.virtual.freebsd
from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual

@pytest.fixture
def mock_sysctl_detection_mixin():
    with patch('ansible.module_utils.facts.virtual.freebsd.VirtualSysctlDetectionMixin') as mock:
        yield mock

@pytest.fixture
def mock_virtual(mock_sysctl_detection_mixin):
    module = MagicMock()
    module.run_command = MagicMock(return_value=(0, '', ''))
    return FreeBSDVirtual(module)

def test_get_virtual_facts_xen(mock_virtual):
    with patch('os.path.exists', return_value=True):
        facts = mock_virtual.get_virtual_facts()
        assert facts['virtualization_type'] == 'xen'
        assert facts['virtualization_role'] == 'guest'
        assert 'xen' in facts['virtualization_tech_guest']

def test_get_virtual_facts_no_xen(mock_virtual):
    with patch('os.path.exists', return_value=False):
        with patch.object(mock_virtual, 'detect_virt_product', side_effect=[
            {'virtualization_tech_guest': {'vmware'}, 'virtualization_tech_host': set()},
            {'virtualization_tech_guest': set(), 'virtualization_tech_host': {'bhyve'}},
            {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}
        ]):
            with patch.object(mock_virtual, 'detect_virt_vendor', return_value={
                'virtualization_tech_guest': set(),
                'virtualization_tech_host': set()
            }):
                facts = mock_virtual.get_virtual_facts()
                assert facts['virtualization_type'] == ''
                assert facts['virtualization_role'] == ''
                assert 'vmware' in facts['virtualization_tech_guest']
                assert 'bhyve' in facts['virtualization_tech_host']

def test_get_virtual_facts_with_vendor(mock_virtual):
    with patch('os.path.exists', return_value=False):
        with patch.object(mock_virtual, 'detect_virt_product', side_effect=[
            {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()},
            {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()},
            {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}
        ]):
            with patch.object(mock_virtual, 'detect_virt_vendor', return_value={
                'virtualization_tech_guest': {'kvm'},
                'virtualization_tech_host': set()
            }):
                facts = mock_virtual.get_virtual_facts()
                assert facts['virtualization_type'] == ''
                assert facts['virtualization_role'] == ''
                assert 'kvm' in facts['virtualization_tech_guest']
