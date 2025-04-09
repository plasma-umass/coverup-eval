# file: lib/ansible/module_utils/facts/system/distribution.py:510-511
# asked: {"lines": [510, 511], "branches": []}
# gained: {"lines": [510, 511], "branches": []}

import pytest
from ansible.module_utils.facts.system.distribution import Distribution

def test_distribution_init(monkeypatch):
    class MockModule:
        pass

    mock_module = MockModule()
    dist = Distribution(mock_module)
    
    assert dist.module is mock_module
