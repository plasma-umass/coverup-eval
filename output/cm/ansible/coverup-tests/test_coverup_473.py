# file lib/ansible/module_utils/api.py:35-43
# lines [35, 37, 38, 39, 41, 42, 43]
# branches ['41->42', '41->43']

import pytest
from ansible.module_utils.api import rate_limit_argument_spec

def test_rate_limit_argument_spec_with_spec():
    # Prepare a spec to update the default rate_limit_argument_spec
    additional_spec = {'extra_option': {'type': 'str', 'default': 'extra_value'}}

    # Call the function with the additional spec
    result = rate_limit_argument_spec(spec=additional_spec)

    # Assert that the result contains both the default and the additional spec
    assert 'rate' in result
    assert 'rate_limit' in result
    assert 'extra_option' in result
    assert result['extra_option'] == {'type': 'str', 'default': 'extra_value'}

def test_rate_limit_argument_spec_without_spec():
    # Call the function without providing an additional spec
    result = rate_limit_argument_spec()

    # Assert that the result contains only the default spec
    assert 'rate' in result
    assert 'rate_limit' in result
    assert len(result) == 2
