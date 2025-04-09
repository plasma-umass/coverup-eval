# file: lib/ansible/module_utils/facts/virtual/netbsd.py:25-68
# asked: {"lines": [25, 26, 28, 29, 30, 31, 34, 35, 37, 38, 39, 40, 42, 43, 44, 46, 47, 52, 53, 54, 56, 57, 59, 60, 62, 63, 64, 66, 67, 68], "branches": [[46, 47], [46, 52], [56, 57], [56, 59], [59, 60], [59, 66], [62, 63], [62, 66]]}
# gained: {"lines": [25, 26, 28, 29, 30, 31, 34, 35, 37, 38, 39, 40, 42, 43, 44, 46, 47, 52, 53, 54, 56, 57, 59, 60, 62, 63, 64, 66, 67, 68], "branches": [[46, 47], [46, 52], [56, 57], [56, 59], [59, 60], [59, 66], [62, 63]]}

import pytest
import os
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual

@pytest.fixture
def netbsd_virtual():
    module = MagicMock()
    return NetBSDVirtual(module)

def test_get_virtual_facts_default(monkeypatch, netbsd_virtual):
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

    monkeypatch.setattr(netbsd_virtual, 'detect_virt_product', mock_detect_virt_product)
    monkeypatch.setattr(netbsd_virtual, 'detect_virt_vendor', mock_detect_virt_vendor)
    monkeypatch.setattr(os.path, 'exists', lambda x: False)

    virtual_facts = netbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

def test_get_virtual_facts_xen_guest(monkeypatch, netbsd_virtual):
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

    monkeypatch.setattr(netbsd_virtual, 'detect_virt_product', mock_detect_virt_product)
    monkeypatch.setattr(netbsd_virtual, 'detect_virt_vendor', mock_detect_virt_vendor)
    monkeypatch.setattr(os.path, 'exists', lambda x: x == '/dev/xencons')

    virtual_facts = netbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'xen' in virtual_facts['virtualization_tech_guest']
    assert virtual_facts['virtualization_tech_host'] == set()

def test_get_virtual_facts_with_product_facts(monkeypatch, netbsd_virtual):
    def mock_detect_virt_product(key):
        return {
            'virtualization_tech_guest': {'tech1'},
            'virtualization_tech_host': {'tech2'},
            'virtualization_type': 'product_type',
            'virtualization_role': 'product_role'
        }

    def mock_detect_virt_vendor(key):
        return {
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set(),
            'virtualization_type': '',
            'virtualization_role': ''
        }

    monkeypatch.setattr(netbsd_virtual, 'detect_virt_product', mock_detect_virt_product)
    monkeypatch.setattr(netbsd_virtual, 'detect_virt_vendor', mock_detect_virt_vendor)
    monkeypatch.setattr(os.path, 'exists', lambda x: False)

    virtual_facts = netbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'product_type'
    assert virtual_facts['virtualization_role'] == 'product_role'
    assert 'tech1' in virtual_facts['virtualization_tech_guest']
    assert 'tech2' in virtual_facts['virtualization_tech_host']

def test_get_virtual_facts_with_vendor_facts(monkeypatch, netbsd_virtual):
    def mock_detect_virt_product(key):
        return {
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set(),
            'virtualization_type': '',
            'virtualization_role': ''
        }

    def mock_detect_virt_vendor(key):
        return {
            'virtualization_tech_guest': {'tech3'},
            'virtualization_tech_host': {'tech4'},
            'virtualization_type': 'vendor_type',
            'virtualization_role': 'vendor_role'
        }

    monkeypatch.setattr(netbsd_virtual, 'detect_virt_product', mock_detect_virt_product)
    monkeypatch.setattr(netbsd_virtual, 'detect_virt_vendor', mock_detect_virt_vendor)
    monkeypatch.setattr(os.path, 'exists', lambda x: False)

    virtual_facts = netbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'vendor_type'
    assert virtual_facts['virtualization_role'] == 'vendor_role'
    assert 'tech3' in virtual_facts['virtualization_tech_guest']
    assert 'tech4' in virtual_facts['virtualization_tech_host']
