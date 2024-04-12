# file lib/ansible/module_utils/common/validation.py:338-361
# lines [338, 349, 350, 351, 353, 354, 355, 357, 358, 359, 361]
# branches ['350->351', '350->353', '353->354', '353->357', '354->353', '354->355', '357->358', '357->361']

import pytest
from ansible.module_utils.common.validation import check_missing_parameters
from ansible.module_utils._text import to_native

def test_check_missing_parameters_with_missing_params():
    parameters = {'name': 'test', 'state': 'present'}
    required_parameters = ['name', 'state', 'path']
    
    with pytest.raises(TypeError) as excinfo:
        check_missing_parameters(parameters, required_parameters)
    
    assert to_native("missing required arguments: path") in str(excinfo.value)

def test_check_missing_parameters_with_no_missing_params():
    parameters = {'name': 'test', 'state': 'present', 'path': '/some/path'}
    required_parameters = ['name', 'state', 'path']
    
    result = check_missing_parameters(parameters, required_parameters)
    
    assert result == []

def test_check_missing_parameters_with_no_required_params():
    parameters = {'name': 'test', 'state': 'present'}
    required_parameters = None
    
    result = check_missing_parameters(parameters, required_parameters)
    
    assert result == []
