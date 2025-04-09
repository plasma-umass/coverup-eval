# file lib/ansible/module_utils/facts/virtual/sysctl.py:93-112
# lines [102, 103, 104, 106, 107, 108]
# branches ['98->110', '100->110', '101->102', '105->106']

import pytest
from unittest.mock import Mock, patch

# Assuming the class is imported from the module
from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def virtual_sysctl_detection_mixin(mock_module):
    mixin = VirtualSysctlDetectionMixin()
    mixin.module = mock_module
    mixin.sysctl_path = "/sbin/sysctl"
    return mixin

def test_detect_virt_vendor_kvm(virtual_sysctl_detection_mixin, mock_module):
    key = "hw.vendor"
    mock_module.run_command.return_value = (0, "QEMU\n", "")
    
    result = virtual_sysctl_detection_mixin.detect_virt_vendor(key)
    
    assert result['virtualization_type'] == 'kvm'
    assert result['virtualization_role'] == 'guest'
    assert 'kvm' in result['virtualization_tech_guest']
    assert 'virtualization_tech_host' in result

def test_detect_virt_vendor_vmm(virtual_sysctl_detection_mixin, mock_module):
    key = "hw.vendor"
    mock_module.run_command.return_value = (0, "OpenBSD\n", "")
    
    result = virtual_sysctl_detection_mixin.detect_virt_vendor(key)
    
    assert result['virtualization_type'] == 'vmm'
    assert result['virtualization_role'] == 'guest'
    assert 'vmm' in result['virtualization_tech_guest']
    assert 'virtualization_tech_host' in result

def test_detect_virt_vendor_no_sysctl_path(virtual_sysctl_detection_mixin, mock_module):
    virtual_sysctl_detection_mixin.sysctl_path = None
    key = "hw.vendor"
    
    with patch.object(virtual_sysctl_detection_mixin, 'detect_sysctl', return_value=None):
        result = virtual_sysctl_detection_mixin.detect_virt_vendor(key)
    
    assert 'virtualization_type' not in result
    assert 'virtualization_role' not in result
    assert 'virtualization_tech_guest' in result
    assert 'virtualization_tech_host' in result
