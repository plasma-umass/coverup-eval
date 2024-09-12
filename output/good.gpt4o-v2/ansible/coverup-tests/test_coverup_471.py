# file: lib/ansible/module_utils/api.py:46-54
# asked: {"lines": [46, 48, 49, 50, 52, 53, 54], "branches": [[52, 53], [52, 54]]}
# gained: {"lines": [46, 48, 49, 50, 52, 53, 54], "branches": [[52, 53], [52, 54]]}

import pytest
from ansible.module_utils.api import retry_argument_spec

def test_retry_argument_spec_no_spec():
    result = retry_argument_spec()
    expected = {
        'retries': {'type': 'int'},
        'retry_pause': {'type': 'float', 'default': 1}
    }
    assert result == expected

def test_retry_argument_spec_with_spec():
    custom_spec = {
        'max_retries': {'type': 'int', 'default': 5},
        'retry_delay': {'type': 'float', 'default': 2}
    }
    result = retry_argument_spec(custom_spec)
    expected = {
        'retries': {'type': 'int'},
        'retry_pause': {'type': 'float', 'default': 1},
        'max_retries': {'type': 'int', 'default': 5},
        'retry_delay': {'type': 'float', 'default': 2}
    }
    assert result == expected
