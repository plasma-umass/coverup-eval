# file: lib/ansible/module_utils/common/validation.py:338-361
# asked: {"lines": [338, 349, 350, 351, 353, 354, 355, 357, 358, 359, 361], "branches": [[350, 351], [350, 353], [353, 354], [353, 357], [354, 353], [354, 355], [357, 358], [357, 361]]}
# gained: {"lines": [338, 349, 350, 351, 353, 354, 355, 357, 358, 359, 361], "branches": [[350, 351], [350, 353], [353, 354], [353, 357], [354, 353], [354, 355], [357, 358], [357, 361]]}

import pytest
from ansible.module_utils.common.validation import check_missing_parameters

def test_check_missing_parameters_no_required():
    parameters = {'param1': 'value1', 'param2': 'value2'}
    required_parameters = None
    result = check_missing_parameters(parameters, required_parameters)
    assert result == []

def test_check_missing_parameters_all_present():
    parameters = {'param1': 'value1', 'param2': 'value2'}
    required_parameters = ['param1', 'param2']
    result = check_missing_parameters(parameters, required_parameters)
    assert result == []

def test_check_missing_parameters_some_missing():
    parameters = {'param1': 'value1'}
    required_parameters = ['param1', 'param2']
    with pytest.raises(TypeError, match="missing required arguments: param2"):
        check_missing_parameters(parameters, required_parameters)

def test_check_missing_parameters_all_missing():
    parameters = {}
    required_parameters = ['param1', 'param2']
    with pytest.raises(TypeError, match="missing required arguments: param1, param2"):
        check_missing_parameters(parameters, required_parameters)
