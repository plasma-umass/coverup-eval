# file: lib/ansible/module_utils/facts/virtual/openbsd.py:27-69
# asked: {"lines": [27, 28, 33, 34, 36, 37, 38, 39, 42, 43, 45, 46, 47, 48, 50, 51, 52, 54, 55, 59, 60, 61, 62, 63, 64, 65, 67, 68, 69], "branches": [[54, 55], [54, 59], [60, 61], [60, 67], [62, 60], [62, 63]]}
# gained: {"lines": [27, 28, 33, 34, 36, 37, 38, 39, 42, 43, 45, 46, 47, 48, 50, 51, 52, 54, 55, 59, 60, 61, 62, 63, 64, 65, 67, 68, 69], "branches": [[54, 55], [54, 59], [60, 61], [60, 67], [62, 63]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtual
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def openbsd_virtual():
    module = MagicMock(spec=AnsibleModule)
    return OpenBSDVirtual(module)

def test_get_virtual_facts_no_dmesg_boot(monkeypatch, openbsd_virtual):
    def mock_get_file_content(path):
        return ""

    def mock_detect_virt_product(key):
        return {
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set(),
            'virtualization_type': '',
            'virtualization_role': ''
        }

    def mock_detect_virt_vendor(key):
        return {
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set(),
            'virtualization_type': '',
            'virtualization_role': ''
        }

    monkeypatch.setattr('ansible.module_utils.facts.virtual.openbsd.get_file_content', mock_get_file_content)
    monkeypatch.setattr(openbsd_virtual, 'detect_virt_product', mock_detect_virt_product)
    monkeypatch.setattr(openbsd_virtual, 'detect_virt_vendor', mock_detect_virt_vendor)

    virtual_facts = openbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

def test_get_virtual_facts_with_dmesg_boot(monkeypatch, openbsd_virtual):
    def mock_get_file_content(path):
        return "vmm0 at mainbus0: VMX/EPT"

    def mock_detect_virt_product(key):
        return {
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set(),
            'virtualization_type': '',
            'virtualization_role': ''
        }

    def mock_detect_virt_vendor(key):
        return {
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set(),
            'virtualization_type': '',
            'virtualization_role': ''
        }

    monkeypatch.setattr('ansible.module_utils.facts.virtual.openbsd.get_file_content', mock_get_file_content)
    monkeypatch.setattr(openbsd_virtual, 'detect_virt_product', mock_detect_virt_product)
    monkeypatch.setattr(openbsd_virtual, 'detect_virt_vendor', mock_detect_virt_vendor)

    virtual_facts = openbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'
    assert 'vmm' in virtual_facts['virtualization_tech_host']
    assert virtual_facts['virtualization_tech_guest'] == set()

def test_get_virtual_facts_with_detect_virt_product(monkeypatch, openbsd_virtual):
    def mock_get_file_content(path):
        return ""

    def mock_detect_virt_product(key):
        return {
            'virtualization_tech_guest': {'kvm'},
            'virtualization_tech_host': set(),
            'virtualization_type': 'kvm',
            'virtualization_role': 'guest'
        }

    def mock_detect_virt_vendor(key):
        return {
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set(),
            'virtualization_type': '',
            'virtualization_role': ''
        }

    monkeypatch.setattr('ansible.module_utils.facts.virtual.openbsd.get_file_content', mock_get_file_content)
    monkeypatch.setattr(openbsd_virtual, 'detect_virt_product', mock_detect_virt_product)
    monkeypatch.setattr(openbsd_virtual, 'detect_virt_vendor', mock_detect_virt_vendor)

    virtual_facts = openbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'kvm'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'kvm' in virtual_facts['virtualization_tech_guest']
    assert virtual_facts['virtualization_tech_host'] == set()

def test_get_virtual_facts_with_detect_virt_vendor(monkeypatch, openbsd_virtual):
    def mock_get_file_content(path):
        return ""

    def mock_detect_virt_product(key):
        return {
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set(),
            'virtualization_type': '',
            'virtualization_role': ''
        }

    def mock_detect_virt_vendor(key):
        return {
            'virtualization_tech_guest': {'vmm'},
            'virtualization_tech_host': set(),
            'virtualization_type': 'vmm',
            'virtualization_role': 'guest'
        }

    monkeypatch.setattr('ansible.module_utils.facts.virtual.openbsd.get_file_content', mock_get_file_content)
    monkeypatch.setattr(openbsd_virtual, 'detect_virt_product', mock_detect_virt_product)
    monkeypatch.setattr(openbsd_virtual, 'detect_virt_vendor', mock_detect_virt_vendor)

    virtual_facts = openbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'vmm' in virtual_facts['virtualization_tech_guest']
    assert virtual_facts['virtualization_tech_host'] == set()
