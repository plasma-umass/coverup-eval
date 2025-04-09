# file lib/ansible/module_utils/api.py:46-54
# lines [46, 48, 49, 50, 52, 53, 54]
# branches ['52->53', '52->54']

import pytest
from ansible.module_utils.api import retry_argument_spec

def test_retry_argument_spec_no_spec():
    result = retry_argument_spec()
    expected = {
        'retries': {'type': 'int'},
        'retry_pause': {'type': 'float', 'default': 1},
    }
    assert result == expected

def test_retry_argument_spec_with_spec():
    additional_spec = {
        'timeout': {'type': 'int', 'default': 30},
        'backoff': {'type': 'float', 'default': 2.0},
    }
    result = retry_argument_spec(additional_spec)
    expected = {
        'retries': {'type': 'int'},
        'retry_pause': {'type': 'float', 'default': 1},
        'timeout': {'type': 'int', 'default': 30},
        'backoff': {'type': 'float', 'default': 2.0},
    }
    assert result == expected
