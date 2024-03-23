# file lib/ansible/module_utils/facts/virtual/sysctl.py:93-112
# lines [93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112]
# branches ['98->99', '98->110', '100->101', '100->110', '101->102', '101->105', '105->106', '105->110']

import pytest
from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin

class MockModule(object):
    def run_command(self, command):
        if 'machdep.cpu.brand_string' in command:
            return 0, 'QEMU', ''
        elif 'hw.vendor' in command:
            return 0, 'OpenBSD', ''
        else:
            return 1, '', 'An error occurred'
    def get_bin_path(self, bin_name):
        return '/sbin/' + bin_name

@pytest.fixture
def sysctl_mixin(mocker):
    mixin = VirtualSysctlDetectionMixin()
    mixin.module = MockModule()
    mixin.sysctl_path = '/sbin/sysctl'
    return mixin

def test_detect_virt_vendor_qemu(sysctl_mixin):
    facts = sysctl_mixin.detect_virt_vendor('machdep.cpu.brand_string')
    assert facts.get('virtualization_type') == 'kvm'
    assert facts.get('virtualization_role') == 'guest'
    assert 'kvm' in facts.get('virtualization_tech_guest', set())
    assert not facts.get('virtualization_tech_host', set())

def test_detect_virt_vendor_openbsd(sysctl_mixin):
    facts = sysctl_mixin.detect_virt_vendor('hw.vendor')
    assert facts.get('virtualization_type') == 'vmm'
    assert facts.get('virtualization_role') == 'guest'
    assert 'vmm' in facts.get('virtualization_tech_guest', set())
    assert not facts.get('virtualization_tech_host', set())

def test_detect_virt_vendor_no_match(sysctl_mixin):
    sysctl_mixin.module.run_command = lambda command: (1, '', 'An error occurred')
    facts = sysctl_mixin.detect_virt_vendor('nonexistent.key')
    assert 'virtualization_type' not in facts
    assert 'virtualization_role' not in facts
    assert not facts.get('virtualization_tech_guest', set())
    assert not facts.get('virtualization_tech_host', set())
