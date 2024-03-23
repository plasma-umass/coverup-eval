# file lib/ansible/module_utils/facts/virtual/base.py:25-55
# lines [25, 26, 36, 39, 40, 43, 44, 46, 48, 49, 50, 51, 52, 53, 55]
# branches []

import pytest
from ansible.module_utils.facts.virtual.base import Virtual

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    return mock_module

def test_virtual_populate(mock_module):
    virtual = Virtual(module=mock_module)
    facts = virtual.populate()
    assert isinstance(facts, dict)
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''
    assert isinstance(facts['virtualization_tech_guest'], set)
    assert isinstance(facts['virtualization_tech_host'], set)
