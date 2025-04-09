# file lib/ansible/module_utils/facts/system/distribution.py:510-511
# lines [510, 511]
# branches []

import pytest
from unittest.mock import Mock

# Assuming the Distribution class is imported from the correct module
from ansible.module_utils.facts.system.distribution import Distribution

def test_distribution_init():
    # Create a mock module
    mock_module = Mock()
    
    # Instantiate the Distribution class with the mock module
    distribution = Distribution(mock_module)
    
    # Assert that the module attribute is set correctly
    assert distribution.module == mock_module
