# file lib/ansible/module_utils/common/validation.py:137-170
# lines [137, 153, 154, 155, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 170]
# branches ['154->155', '154->157', '157->158', '157->163', '160->157', '160->161', '161->157', '161->162', '163->164', '163->170', '164->165', '164->170', '166->167', '166->168']

import pytest
from ansible.module_utils.common.validation import check_required_together
from ansible.module_utils._text import to_native

def count_terms(field, parameters):
    # Mock function to simulate count_terms behavior
    return parameters.get(field, 0)

@pytest.fixture
def mock_count_terms(mocker):
    mocker.patch('ansible.module_utils.common.validation.count_terms', side_effect=count_terms)

def test_check_required_together_with_missing_parameters(mock_count_terms):
    terms = [['param1', 'param2'], ['param3', 'param4']]
    parameters = {'param1': 1, 'param3': 1}
    options_context = ['context1', 'context2']

    with pytest.raises(TypeError) as excinfo:
        check_required_together(terms, parameters, options_context)

    assert "parameters are required together: param1, param2 found in context1 -> context2" in str(excinfo.value)

def test_check_required_together_without_missing_parameters(mock_count_terms):
    terms = [['param1', 'param2'], ['param3', 'param4']]
    parameters = {'param1': 1, 'param2': 1, 'param3': 1, 'param4': 1}

    result = check_required_together(terms, parameters)
    assert result == []

def test_check_required_together_with_empty_terms(mock_count_terms):
    terms = []
    parameters = {'param1': 1, 'param2': 1}

    result = check_required_together(terms, parameters)
    assert result == []

def test_check_required_together_with_none_terms(mock_count_terms):
    terms = None
    parameters = {'param1': 1, 'param2': 1}

    result = check_required_together(terms, parameters)
    assert result == []

def test_check_required_together_with_no_missing_parameters_and_context(mock_count_terms):
    terms = [['param1', 'param2']]
    parameters = {'param1': 1, 'param2': 1}
    options_context = ['context1']

    result = check_required_together(terms, parameters, options_context)
    assert result == []
