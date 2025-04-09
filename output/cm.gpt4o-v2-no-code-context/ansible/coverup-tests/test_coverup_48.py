# file: lib/ansible/module_utils/facts/virtual/freebsd.py:25-74
# asked: {"lines": [25, 26, 31, 33, 34, 35, 36, 39, 40, 42, 43, 44, 45, 47, 48, 49, 51, 52, 53, 55, 56, 57, 59, 60, 63, 65, 66, 67, 69, 70, 72, 73, 74], "branches": [[42, 43], [42, 47], [59, 60], [59, 65], [69, 70], [69, 72]]}
# gained: {"lines": [25, 26, 31, 33, 34, 35, 36, 39, 40, 42, 43, 44, 45, 47, 48, 49, 51, 52, 53, 55, 56, 57, 59, 60, 63, 65, 66, 67, 69, 70, 72, 73, 74], "branches": [[42, 43], [42, 47], [59, 60], [59, 65], [69, 70], [69, 72]]}

import pytest
import os
from unittest.mock import patch, MagicMock

# Assuming the FreeBSDVirtual class is imported from the module
from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual

@pytest.fixture
def freebsd_virtual():
    module = MagicMock()
    return FreeBSDVirtual(module)

def test_get_virtual_facts_xen_guest(freebsd_virtual, monkeypatch):
    def mock_exists(path):
        return path == '/dev/xen/xenstore'

    def mock_detect_virt_product(key):
        return {
            'kern.vm_guest': {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()},
            'hw.hv_vendor': {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()},
            'security.jail.jailed': {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}
        }.get(key, {})

    def mock_detect_virt_vendor(key):
        return {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(freebsd_virtual, 'detect_virt_product', mock_detect_virt_product)
    monkeypatch.setattr(freebsd_virtual, 'detect_virt_vendor', mock_detect_virt_vendor)

    virtual_facts = freebsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'xen' in virtual_facts['virtualization_tech_guest']
    assert 'xen' not in virtual_facts['virtualization_tech_host']

def test_get_virtual_facts_no_xen(freebsd_virtual, monkeypatch):
    def mock_exists(path):
        return False

    def mock_detect_virt_product(key):
        return {
            'kern.vm_guest': {'virtualization_tech_guest': {'vmware'}, 'virtualization_tech_host': set()},
            'hw.hv_vendor': {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()},
            'security.jail.jailed': {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}
        }.get(key, {})

    def mock_detect_virt_vendor(key):
        return {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(freebsd_virtual, 'detect_virt_product', mock_detect_virt_product)
    monkeypatch.setattr(freebsd_virtual, 'detect_virt_vendor', mock_detect_virt_vendor)

    virtual_facts = freebsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert 'vmware' in virtual_facts['virtualization_tech_guest']
    assert 'vmware' not in virtual_facts['virtualization_tech_host']

def test_get_virtual_facts_with_vendor(freebsd_virtual, monkeypatch):
    def mock_exists(path):
        return False

    def mock_detect_virt_product(key):
        return {
            'kern.vm_guest': {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()},
            'hw.hv_vendor': {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()},
            'security.jail.jailed': {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}
        }.get(key, {})

    def mock_detect_virt_vendor(key):
        return {'virtualization_tech_guest': {'bhyve'}, 'virtualization_tech_host': set()}

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(freebsd_virtual, 'detect_virt_product', mock_detect_virt_product)
    monkeypatch.setattr(freebsd_virtual, 'detect_virt_vendor', mock_detect_virt_vendor)

    virtual_facts = freebsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert 'bhyve' in virtual_facts['virtualization_tech_guest']
    assert 'bhyve' not in virtual_facts['virtualization_tech_host']
