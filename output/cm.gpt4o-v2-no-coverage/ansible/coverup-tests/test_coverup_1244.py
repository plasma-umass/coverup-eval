# file: lib/ansible/module_utils/facts/virtual/openbsd.py:27-69
# asked: {"lines": [], "branches": [[62, 60]]}
# gained: {"lines": [], "branches": [[62, 60]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtual

@pytest.fixture
def openbsd_virtual():
    module = MagicMock()
    return OpenBSDVirtual(module)

def test_get_virtual_facts_no_dmesg_match(openbsd_virtual, monkeypatch):
    def mock_get_file_content(path):
        return "some unrelated content\nanother line"

    monkeypatch.setattr('ansible.module_utils.facts.virtual.openbsd.get_file_content', mock_get_file_content)
    monkeypatch.setattr(openbsd_virtual, 'detect_virt_product', lambda x: {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()})
    monkeypatch.setattr(openbsd_virtual, 'detect_virt_vendor', lambda x: {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()})

    virtual_facts = openbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

def test_get_virtual_facts_with_dmesg_match(openbsd_virtual, monkeypatch):
    def mock_get_file_content(path):
        return "vmm0 at mainbus0: VMX/EPT\nanother line"

    monkeypatch.setattr('ansible.module_utils.facts.virtual.openbsd.get_file_content', mock_get_file_content)
    monkeypatch.setattr(openbsd_virtual, 'detect_virt_product', lambda x: {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()})
    monkeypatch.setattr(openbsd_virtual, 'detect_virt_vendor', lambda x: {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()})

    virtual_facts = openbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == {'vmm'}
