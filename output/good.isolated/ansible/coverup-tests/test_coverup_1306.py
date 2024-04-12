# file lib/ansible/module_utils/common/validation.py:42-67
# lines [46, 47, 48]
# branches ['44->46', '46->47', '46->48']

import pytest
from ansible.module_utils.common.validation import safe_eval

def test_safe_eval_non_string_include_exceptions(mocker):
    # Mock isinstance to force the branch where value is not a string
    mocker.patch('ansible.module_utils.common.validation.isinstance', return_value=False)
    # Test with include_exceptions=True
    result = safe_eval(value={}, include_exceptions=True)
    assert result == ({}, None), "safe_eval should return the value and None when include_exceptions is True"

def test_safe_eval_non_string_exclude_exceptions(mocker):
    # Mock isinstance to force the branch where value is not a string
    mocker.patch('ansible.module_utils.common.validation.isinstance', return_value=False)
    # Test with include_exceptions=False
    result = safe_eval(value={}, include_exceptions=False)
    assert result == {}, "safe_eval should return the value when include_exceptions is False"
