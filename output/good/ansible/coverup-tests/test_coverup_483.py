# file lib/ansible/module_utils/api.py:46-54
# lines [46, 48, 49, 50, 52, 53, 54]
# branches ['52->53', '52->54']

import pytest
from ansible.module_utils.api import retry_argument_spec

# Test function to check if the retry_argument_spec function works correctly
def test_retry_argument_spec():
    # Define a custom spec to update the default one
    custom_spec = {
        'custom_arg': dict(type='str')
    }

    # Call the function with the custom spec
    result_spec = retry_argument_spec(spec=custom_spec)

    # Assertions to check if the result spec is as expected
    assert 'retries' in result_spec, "The 'retries' key should be in the result spec"
    assert 'retry_pause' in result_spec, "The 'retry_pause' key should be in the result spec"
    assert 'custom_arg' in result_spec, "The 'custom_arg' key should be in the result spec"
    assert result_spec['retries'] == dict(type='int'), "The 'retries' key should be of type 'int'"
    assert result_spec['retry_pause'] == dict(type='float', default=1), "The 'retry_pause' key should be of type 'float' with default 1"
    assert result_spec['custom_arg'] == dict(type='str'), "The 'custom_arg' key should be of type 'str'"

    # Call the function without the custom spec
    default_spec = retry_argument_spec()

    # Assertions to check if the default spec is as expected
    assert 'retries' in default_spec, "The 'retries' key should be in the default spec"
    assert 'retry_pause' in default_spec, "The 'retry_pause' key should be in the default spec"
    assert default_spec['retries'] == dict(type='int'), "The 'retries' key should be of type 'int' in the default spec"
    assert default_spec['retry_pause'] == dict(type='float', default=1), "The 'retry_pause' key should be of type 'float' with default 1 in the default spec"
