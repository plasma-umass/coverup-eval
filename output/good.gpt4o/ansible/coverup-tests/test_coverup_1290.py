# file lib/ansible/module_utils/common/parameters.py:802-824
# lines [817, 818]
# branches []

import pytest
from unittest.mock import Mock

# Assuming AnsibleFallbackNotFound is defined somewhere in the module
from ansible.module_utils.common.parameters import set_fallbacks, AnsibleFallbackNotFound

def test_set_fallbacks_ansible_fallback_not_found(mocker):
    # Mocking the fallback strategy to raise AnsibleFallbackNotFound
    mock_fallback_strategy = Mock(side_effect=AnsibleFallbackNotFound)
    
    argument_spec = {
        'param1': {
            'fallback': (mock_fallback_strategy,)
        }
    }
    parameters = {}

    no_log_values = set_fallbacks(argument_spec, parameters)

    # Assertions to verify the postconditions
    assert 'param1' not in parameters
    assert no_log_values == set()
    mock_fallback_strategy.assert_called_once()

