# file lib/ansible/module_utils/facts/virtual/netbsd.py:25-68
# lines [29, 30, 31, 34, 35, 37, 38, 39, 40, 42, 43, 44, 46, 47, 52, 53, 54, 56, 57, 59, 60, 62, 63, 64, 66, 67, 68]
# branches ['46->47', '46->52', '56->57', '56->59', '59->60', '59->66', '62->63', '62->66']

import os
import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual

@pytest.fixture
def mock_detect_virt_product(mocker):
    return mocker.patch.object(NetBSDVirtual, 'detect_virt_product', return_value={
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    })

@pytest.fixture
def mock_detect_virt_vendor(mocker):
    return mocker.patch.object(NetBSDVirtual, 'detect_virt_vendor', return_value={
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    })

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists', return_value=True)

def test_get_virtual_facts(mock_detect_virt_product, mock_detect_virt_vendor, mock_os_path_exists):
    module = MagicMock()
    netbsd_virtual = NetBSDVirtual(module)
    virtual_facts = netbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'xen' in virtual_facts['virtualization_tech_guest']
    mock_detect_virt_product.assert_called_once_with('machdep.dmi.system-product')
    mock_detect_virt_vendor.assert_called_with('machdep.hypervisor')
    mock_os_path_exists.assert_called_once_with('/dev/xencons')
