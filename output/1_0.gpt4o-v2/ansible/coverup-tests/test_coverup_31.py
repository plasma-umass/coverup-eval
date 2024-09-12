# file: lib/ansible/module_utils/facts/virtual/base.py:25-55
# asked: {"lines": [25, 26, 36, 39, 40, 43, 44, 46, 48, 49, 50, 51, 52, 53, 55], "branches": []}
# gained: {"lines": [25, 26, 36, 39, 40, 43, 44, 46, 48, 49, 50, 51, 52, 53, 55], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.base import Virtual

class MockModule:
    pass

@pytest.fixture
def mock_module():
    return MockModule()

def test_virtual_init(mock_module):
    virtual = Virtual(mock_module)
    assert virtual.module == mock_module

def test_virtual_populate(mock_module):
    virtual = Virtual(mock_module)
    facts = virtual.populate()
    assert facts == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }

def test_virtual_get_virtual_facts(mock_module):
    virtual = Virtual(mock_module)
    facts = virtual.get_virtual_facts()
    assert facts == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }
