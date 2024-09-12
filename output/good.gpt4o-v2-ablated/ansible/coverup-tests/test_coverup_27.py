# file: lib/ansible/module_utils/common/validation.py:137-170
# asked: {"lines": [137, 153, 154, 155, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 170], "branches": [[154, 155], [154, 157], [157, 158], [157, 163], [160, 157], [160, 161], [161, 157], [161, 162], [163, 164], [163, 170], [164, 165], [164, 170], [166, 167], [166, 168]]}
# gained: {"lines": [137, 153, 154, 155, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 170], "branches": [[154, 155], [154, 157], [157, 158], [157, 163], [160, 157], [160, 161], [161, 157], [161, 162], [163, 164], [163, 170], [164, 165], [166, 167], [166, 168]]}

import pytest
from ansible.module_utils.common.validation import check_required_together

def count_terms(field, parameters):
    """Mock function to replace the actual count_terms function."""
    return parameters.get(field, 0)

def to_native(msg):
    """Mock function to replace the actual to_native function."""
    return msg

@pytest.fixture
def mock_functions(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.validation.count_terms', count_terms)
    monkeypatch.setattr('ansible.module_utils.common.validation.to_native', to_native)

def test_check_required_together_none_terms(mock_functions):
    assert check_required_together(None, {}) == []

def test_check_required_together_empty_terms(mock_functions):
    assert check_required_together([], {}) == []

def test_check_required_together_no_parameters(mock_functions):
    terms = [['param1', 'param2'], ['param3', 'param4']]
    assert check_required_together(terms, {}) == []

def test_check_required_together_all_present(mock_functions):
    terms = [['param1', 'param2'], ['param3', 'param4']]
    parameters = {'param1': 1, 'param2': 1, 'param3': 1, 'param4': 1}
    assert check_required_together(terms, parameters) == []

def test_check_required_together_some_missing(mock_functions):
    terms = [['param1', 'param2'], ['param3', 'param4']]
    parameters = {'param1': 1, 'param3': 1}
    with pytest.raises(TypeError, match="parameters are required together: param1, param2"):
        check_required_together(terms, parameters)

def test_check_required_together_with_options_context(mock_functions):
    terms = [['param1', 'param2'], ['param3', 'param4']]
    parameters = {'param1': 1, 'param3': 1}
    options_context = ['context1', 'context2']
    with pytest.raises(TypeError, match="parameters are required together: param1, param2 found in context1 -> context2"):
        check_required_together(terms, parameters, options_context)
