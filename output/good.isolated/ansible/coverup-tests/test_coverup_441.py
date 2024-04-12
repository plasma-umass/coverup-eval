# file lib/ansible/plugins/lookup/config.py:107-115
# lines [107, 108, 109, 110, 111, 112, 113, 115]
# branches ['110->111', '110->115']

import pytest
from ansible.errors import AnsibleLookupError
from ansible.module_utils._text import to_native

# Assuming the 'C' object is part of the Ansible configuration global settings
# and 'config' is a string representing the configuration key to look up.

# Mock the 'C' object for testing purposes
class MockConfig:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# Define the test function
def test_get_global_config(mocker):
    # Mock the 'C' object with a known attribute
    mock_config = MockConfig(test_attribute='test_value')
    mocker.patch('ansible.plugins.lookup.config.C', new=mock_config)

    # Import the function to be tested
    from ansible.plugins.lookup.config import _get_global_config

    # Test for a valid configuration key
    result = _get_global_config('test_attribute')
    assert result == 'test_value', "The result should be the value of the test_attribute"

    # Test for a callable configuration key
    mock_config.test_callable = lambda: 'callable_result'
    with pytest.raises(AnsibleLookupError) as excinfo:
        _get_global_config('test_callable')
    assert 'Invalid setting "test_callable" attempted' in str(excinfo.value), "Should raise an AnsibleLookupError for callable settings"

    # Test for a non-existent configuration key
    # Assuming MissingSetting is defined in the same module as _get_global_config
    from ansible.plugins.lookup.config import MissingSetting
    with pytest.raises(MissingSetting) as excinfo:
        _get_global_config('non_existent_attribute')
    assert 'non_existent_attribute' in str(excinfo.value), "Should raise a MissingSetting for non-existent settings"
