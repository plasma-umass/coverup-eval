# file lib/ansible/module_utils/api.py:57-66
# lines [57, 58, 59, 60, 61, 62, 64, 65, 66]
# branches ['64->65', '64->66']

import pytest
from ansible.module_utils.api import basic_auth_argument_spec

def test_basic_auth_argument_spec_with_spec():
    # Define a spec to be updated
    additional_spec = {
        'extra_param': dict(type='str')
    }

    # Call the function with the additional spec
    result = basic_auth_argument_spec(spec=additional_spec)

    # Assert that the result contains both the basic auth keys and the additional spec keys
    expected_keys = {'api_username', 'api_password', 'api_url', 'validate_certs', 'extra_param'}
    assert set(result.keys()) == expected_keys

    # Assert that the additional spec was updated correctly
    assert result['extra_param'] == dict(type='str')

    # Assert that the original keys are still present with correct values
    assert result['api_username'] == dict(type='str')
    assert result['api_password'] == dict(type='str', no_log=True)
    assert result['api_url'] == dict(type='str')
    assert result['validate_certs'] == dict(type='bool', default=True)

def test_basic_auth_argument_spec_without_spec():
    # Call the function without additional spec
    result = basic_auth_argument_spec()

    # Assert that the result contains only the basic auth keys
    expected_keys = {'api_username', 'api_password', 'api_url', 'validate_certs'}
    assert set(result.keys()) == expected_keys

    # Assert that the keys have correct values
    assert result['api_username'] == dict(type='str')
    assert result['api_password'] == dict(type='str', no_log=True)
    assert result['api_url'] == dict(type='str')
    assert result['validate_certs'] == dict(type='bool', default=True)
