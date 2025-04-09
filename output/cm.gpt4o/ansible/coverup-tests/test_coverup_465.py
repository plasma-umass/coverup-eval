# file lib/ansible/module_utils/api.py:35-43
# lines [35, 37, 38, 39, 41, 42, 43]
# branches ['41->42', '41->43']

import pytest
from ansible.module_utils.api import rate_limit_argument_spec

def test_rate_limit_argument_spec_no_spec():
    result = rate_limit_argument_spec()
    expected = {
        'rate': {'type': 'int'},
        'rate_limit': {'type': 'int'}
    }
    assert result == expected

def test_rate_limit_argument_spec_with_spec():
    additional_spec = {
        'timeout': {'type': 'int'},
        'retries': {'type': 'int'}
    }
    result = rate_limit_argument_spec(additional_spec)
    expected = {
        'rate': {'type': 'int'},
        'rate_limit': {'type': 'int'},
        'timeout': {'type': 'int'},
        'retries': {'type': 'int'}
    }
    assert result == expected
