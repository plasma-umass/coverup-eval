# file lib/ansible/module_utils/facts/system/distribution.py:510-511
# lines [510, 511]
# branches []

import pytest
from ansible.module_utils.facts.system.distribution import Distribution

# Mocking the module object that would be passed to Distribution
class MockModule:
    pass

@pytest.fixture
def mock_module(mocker):
    return mocker.Mock(spec=MockModule)

def test_distribution_init(mock_module):
    # Instantiate the Distribution class with the mock module
    distribution = Distribution(mock_module)
    
    # Assert that the module attribute is set correctly
    assert distribution.module is mock_module
