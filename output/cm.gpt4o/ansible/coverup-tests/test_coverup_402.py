# file lib/ansible/module_utils/api.py:57-66
# lines [57, 58, 59, 60, 61, 62, 64, 65, 66]
# branches ['64->65', '64->66']

import pytest
from ansible.module_utils.api import basic_auth_argument_spec

def test_basic_auth_argument_spec_no_spec():
    result = basic_auth_argument_spec()
    expected = {
        'api_username': {'type': 'str'},
        'api_password': {'type': 'str', 'no_log': True},
        'api_url': {'type': 'str'},
        'validate_certs': {'type': 'bool', 'default': True}
    }
    assert result == expected

def test_basic_auth_argument_spec_with_spec():
    additional_spec = {
        'custom_param': {'type': 'int', 'default': 42}
    }
    result = basic_auth_argument_spec(additional_spec)
    expected = {
        'api_username': {'type': 'str'},
        'api_password': {'type': 'str', 'no_log': True},
        'api_url': {'type': 'str'},
        'validate_certs': {'type': 'bool', 'default': True},
        'custom_param': {'type': 'int', 'default': 42}
    }
    assert result == expected
