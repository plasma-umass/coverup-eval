# file lib/ansible/module_utils/common/validation.py:70-100
# lines [88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 100]
# branches ['85->88', '88->89', '88->93', '90->88', '90->91', '93->94', '93->100', '96->97', '96->98']

import pytest
from ansible.module_utils.common.validation import check_mutually_exclusive

def test_check_mutually_exclusive():
    # Test case where terms is None
    assert check_mutually_exclusive(None, {}) == []

    # Test case where no mutually exclusive terms are found
    terms = [['param1', 'param2'], ['param3', 'param4']]
    parameters = {'param1': 'value1', 'param3': 'value3'}
    assert check_mutually_exclusive(terms, parameters) == []

    # Test case where mutually exclusive terms are found
    terms = [['param1', 'param2'], ['param3', 'param4']]
    parameters = {'param1': 'value1', 'param2': 'value2', 'param3': 'value3'}
    with pytest.raises(TypeError, match="parameters are mutually exclusive: param1|param2"):
        check_mutually_exclusive(terms, parameters)

    # Test case where mutually exclusive terms are found with options_context
    terms = [['param1', 'param2'], ['param3', 'param4']]
    parameters = {'param1': 'value1', 'param2': 'value2', 'param3': 'value3'}
    options_context = ['context1', 'context2']
    with pytest.raises(TypeError, match="parameters are mutually exclusive: param1|param2 found in context1 -> context2"):
        check_mutually_exclusive(terms, parameters, options_context)
