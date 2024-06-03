# file lib/ansible/module_utils/common/parameters.py:802-824
# lines [802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 814, 815, 816, 817, 818, 820, 821, 822, 824]
# branches ['804->805', '804->824', '809->804', '809->810', '810->811', '810->815', '811->812', '811->814', '820->821', '820->822']

import pytest
from unittest.mock import Mock

# Assuming AnsibleFallbackNotFound is defined somewhere in the module
class AnsibleFallbackNotFound(Exception):
    pass

# Import the function to be tested
from ansible.module_utils.common.parameters import set_fallbacks

def test_set_fallbacks(mocker):
    # Mocking the fallback strategy function
    mock_fallback_strategy = Mock(return_value='fallback_value')
    
    # Argument specification with fallback strategy
    argument_spec = {
        'param1': {
            'fallback': (mock_fallback_strategy, ['arg1'], {'kwarg1': 'value1'}),
            'no_log': True
        },
        'param2': {
            'fallback': (mock_fallback_strategy,),
            'no_log': False
        },
        'param3': {
            'fallback': (None,),
            'no_log': False
        }
    }
    
    # Parameters dictionary without the parameters that have fallbacks
    parameters = {}
    
    # Call the function
    no_log_values = set_fallbacks(argument_spec, parameters)
    
    # Assertions to verify the postconditions
    assert parameters['param1'] == 'fallback_value'
    assert parameters['param2'] == 'fallback_value'
    assert 'param3' not in parameters
    assert 'fallback_value' in no_log_values
    assert mock_fallback_strategy.call_count == 2
    mock_fallback_strategy.assert_any_call('arg1', kwarg1='value1')
    mock_fallback_strategy.assert_any_call()

    # Clean up
    mock_fallback_strategy.reset_mock()
