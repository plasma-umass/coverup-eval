# file lib/ansible/module_utils/facts/virtual/netbsd.py:25-68
# lines []
# branches ['46->52', '56->59', '59->66', '62->66']

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual

@pytest.fixture
def netbsd_virtual(mocker):
    module_mock = MagicMock()
    return NetBSDVirtual(module=module_mock)

@pytest.fixture
def mock_detect_virt_product():
    return {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

@pytest.fixture
def mock_detect_virt_vendor():
    return {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

def test_get_virtual_facts_with_xen(netbsd_virtual, mock_detect_virt_product, mock_detect_virt_vendor):
    with patch.object(netbsd_virtual, 'detect_virt_product', return_value=mock_detect_virt_product), \
         patch.object(netbsd_virtual, 'detect_virt_vendor', return_value=mock_detect_virt_vendor), \
         patch('os.path.exists', return_value=True):
        virtual_facts = netbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'xen' in virtual_facts['virtualization_tech_guest']
    assert virtual_facts['virtualization_tech_host'] == set()

def test_get_virtual_facts_without_xen(netbsd_virtual, mock_detect_virt_product, mock_detect_virt_vendor):
    with patch.object(netbsd_virtual, 'detect_virt_product', return_value=mock_detect_virt_product), \
         patch.object(netbsd_virtual, 'detect_virt_vendor', side_effect=[mock_detect_virt_vendor, {'virtualization_type': 'test_type', 'virtualization_role': 'test_role', 'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}]), \
         patch('os.path.exists', return_value=False):
        virtual_facts = netbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'test_type'
    assert virtual_facts['virtualization_role'] == 'test_role'
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()
