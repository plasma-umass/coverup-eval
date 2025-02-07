# file: lib/ansible/module_utils/api.py:57-66
# asked: {"lines": [57, 58, 59, 60, 61, 62, 64, 65, 66], "branches": [[64, 65], [64, 66]]}
# gained: {"lines": [57, 58, 59, 60, 61, 62, 64, 65, 66], "branches": [[64, 65], [64, 66]]}

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
    custom_spec = {
        'custom_field': {'type': 'str', 'default': 'custom_value'}
    }
    result = basic_auth_argument_spec(custom_spec)
    expected = {
        'api_username': {'type': 'str'},
        'api_password': {'type': 'str', 'no_log': True},
        'api_url': {'type': 'str'},
        'validate_certs': {'type': 'bool', 'default': True},
        'custom_field': {'type': 'str', 'default': 'custom_value'}
    }
    assert result == expected
