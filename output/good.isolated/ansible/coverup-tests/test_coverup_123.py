# file lib/ansible/module_utils/common/validation.py:70-100
# lines [70, 84, 85, 86, 88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 100]
# branches ['85->86', '85->88', '88->89', '88->93', '90->88', '90->91', '93->94', '93->100', '96->97', '96->98']

import pytest
from ansible.module_utils.common.validation import check_mutually_exclusive
from ansible.module_utils._text import to_native

def test_check_mutually_exclusive_raises_type_error(mocker):
    parameters = {'param1': 'value1', 'param2': 'value2'}
    terms = [['param1', 'param2']]
    options_context = ['parent', 'child']

    with pytest.raises(TypeError) as excinfo:
        check_mutually_exclusive(terms, parameters, options_context)

    assert "parameters are mutually exclusive: param1|param2 found in parent -> child" in str(excinfo.value)

def test_check_mutually_exclusive_returns_empty_list():
    parameters = {'param1': 'value1'}
    terms = [['param1', 'param2']]

    result = check_mutually_exclusive(terms, parameters)
    assert result == []

def test_check_mutually_exclusive_with_none_terms():
    parameters = {'param1': 'value1'}
    terms = None

    result = check_mutually_exclusive(terms, parameters)
    assert result == []
