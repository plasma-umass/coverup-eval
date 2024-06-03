# file lib/ansible/module_utils/common/validation.py:103-134
# lines [103, 118, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 134]
# branches ['119->120', '119->122', '122->123', '122->127', '124->122', '124->125', '127->128', '127->134', '128->129', '128->134', '130->131', '130->132']

import pytest
from ansible.module_utils.common.validation import check_required_one_of

def count_terms(term, parameters):
    """Mock function to simulate the count_terms behavior."""
    return sum(1 for t in term if t in parameters and parameters[t] is not None)

@pytest.fixture
def mock_count_terms(mocker):
    """Fixture to mock the count_terms function."""
    return mocker.patch('ansible.module_utils.common.validation.count_terms', side_effect=count_terms)

def test_check_required_one_of_no_terms(mock_count_terms):
    parameters = {'param1': 'value1', 'param2': 'value2'}
    terms = None
    result = check_required_one_of(terms, parameters)
    assert result == []

def test_check_required_one_of_all_terms_present(mock_count_terms):
    parameters = {'param1': 'value1', 'param2': 'value2'}
    terms = [['param1', 'param2']]
    result = check_required_one_of(terms, parameters)
    assert result == []

def test_check_required_one_of_some_terms_missing(mock_count_terms):
    parameters = {'param1': 'value1'}
    terms = [['param2']]
    with pytest.raises(TypeError) as excinfo:
        check_required_one_of(terms, parameters)
    assert "one of the following is required: param2" in str(excinfo.value)

def test_check_required_one_of_with_options_context(mock_count_terms):
    parameters = {'param1': 'value1'}
    terms = [['param2']]
    options_context = ['parent']
    with pytest.raises(TypeError) as excinfo:
        check_required_one_of(terms, parameters, options_context)
    assert "one of the following is required: param2 found in parent" in str(excinfo.value)
