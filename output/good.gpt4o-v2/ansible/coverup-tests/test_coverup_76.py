# file: lib/ansible/module_utils/common/validation.py:137-170
# asked: {"lines": [137, 153, 154, 155, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 170], "branches": [[154, 155], [154, 157], [157, 158], [157, 163], [160, 157], [160, 161], [161, 157], [161, 162], [163, 164], [163, 170], [164, 165], [164, 170], [166, 167], [166, 168]]}
# gained: {"lines": [137, 153, 154, 155, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 170], "branches": [[154, 155], [154, 157], [157, 158], [157, 163], [160, 157], [160, 161], [161, 157], [161, 162], [163, 164], [163, 170], [164, 165], [166, 167], [166, 168]]}

import pytest
from ansible.module_utils.common.validation import check_required_together
from ansible.module_utils._text import to_native

def test_check_required_together_no_terms():
    assert check_required_together(None, {}) == []

def test_check_required_together_empty_terms():
    assert check_required_together([], {}) == []

def test_check_required_together_no_parameters():
    terms = [['param1', 'param2'], ['param3', 'param4']]
    assert check_required_together(terms, {}) == []

def test_check_required_together_all_present():
    terms = [['param1', 'param2'], ['param3', 'param4']]
    parameters = {'param1': 'value1', 'param2': 'value2', 'param3': 'value3', 'param4': 'value4'}
    assert check_required_together(terms, parameters) == []

def test_check_required_together_some_missing():
    terms = [['param1', 'param2'], ['param3', 'param4']]
    parameters = {'param1': 'value1', 'param3': 'value3'}
    with pytest.raises(TypeError, match="parameters are required together: param1, param2"):
        check_required_together(terms, parameters)

def test_check_required_together_with_options_context():
    terms = [['param1', 'param2'], ['param3', 'param4']]
    parameters = {'param1': 'value1', 'param3': 'value3'}
    options_context = ['context1', 'context2']
    with pytest.raises(TypeError, match="parameters are required together: param1, param2 found in context1 -> context2"):
        check_required_together(terms, parameters, options_context)
