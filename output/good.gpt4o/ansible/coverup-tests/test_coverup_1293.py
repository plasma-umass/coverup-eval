# file lib/ansible/module_utils/common/validation.py:137-170
# lines []
# branches ['160->157', '164->170']

import pytest
from ansible.module_utils.common.validation import check_required_together

def test_check_required_together_missing_branches():
    # Test case to cover branch 160->157
    terms = [['param1', 'param2'], ['param3', 'param4']]
    parameters = {'param1': 'value1'}
    with pytest.raises(TypeError) as excinfo:
        check_required_together(terms, parameters)
    assert "parameters are required together: param1, param2" in str(excinfo.value)

    # Test case to cover branch 164->170
    terms = [['param1', 'param2'], ['param3', 'param4']]
    parameters = {'param1': 'value1', 'param3': 'value3'}
    with pytest.raises(TypeError) as excinfo:
        check_required_together(terms, parameters)
    assert "parameters are required together: param1, param2" in str(excinfo.value) or \
           "parameters are required together: param3, param4" in str(excinfo.value)

    # Test case to cover branch 164->170 with options_context
    terms = [['param1', 'param2']]
    parameters = {'param1': 'value1'}
    options_context = ['context1', 'context2']
    with pytest.raises(TypeError) as excinfo:
        check_required_together(terms, parameters, options_context)
    assert "parameters are required together: param1, param2 found in context1 -> context2" in str(excinfo.value)
