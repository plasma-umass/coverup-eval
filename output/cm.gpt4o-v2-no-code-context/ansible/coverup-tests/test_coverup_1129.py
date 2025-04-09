# file: lib/ansible/module_utils/common/validation.py:173-210
# asked: {"lines": [191, 192, 193, 194, 196, 197, 198, 199, 200, 202, 203, 204, 205, 206, 207, 208, 210], "branches": [[188, 191], [191, 192], [191, 202], [192, 193], [192, 194], [196, 197], [196, 198], [198, 191], [198, 199], [199, 198], [199, 200], [202, 203], [202, 210], [203, 204], [203, 210], [204, 203], [204, 205], [206, 207], [206, 208]]}
# gained: {"lines": [191, 192, 193, 194, 196, 197, 198, 199, 200, 202, 203, 204, 205, 206, 207, 208, 210], "branches": [[188, 191], [191, 192], [191, 202], [192, 193], [192, 194], [196, 197], [196, 198], [198, 191], [198, 199], [199, 198], [199, 200], [202, 203], [202, 210], [203, 204], [203, 210], [204, 203], [204, 205], [206, 207], [206, 208]]}

import pytest
from ansible.module_utils.common.validation import check_required_by

def test_check_required_by_no_requirements():
    assert check_required_by(None, {}) == {}

def test_check_required_by_empty_requirements():
    assert check_required_by({}, {}) == {}

def test_check_required_by_missing_parameters():
    requirements = {'key1': 'required1'}
    parameters = {}
    assert check_required_by(requirements, parameters) == {}

def test_check_required_by_parameters_none():
    requirements = {'key1': 'required1'}
    parameters = {'key1': None}
    assert check_required_by(requirements, parameters) == {}

def test_check_required_by_single_string():
    requirements = {'key1': 'required1'}
    parameters = {'key1': 'value1', 'required1': None}
    with pytest.raises(TypeError, match="missing parameter\(s\) required by 'key1': required1"):
        check_required_by(requirements, parameters)

def test_check_required_by_list_of_values():
    requirements = {'key1': ['required1', 'required2']}
    parameters = {'key1': 'value1', 'required1': None, 'required2': None}
    with pytest.raises(TypeError, match="missing parameter\(s\) required by 'key1': required1, required2"):
        check_required_by(requirements, parameters)

def test_check_required_by_with_options_context():
    requirements = {'key1': 'required1'}
    parameters = {'key1': 'value1', 'required1': None}
    options_context = ['parent1', 'parent2']
    with pytest.raises(TypeError, match="missing parameter\(s\) required by 'key1': required1 found in parent1 -> parent2"):
        check_required_by(requirements, parameters, options_context)

def test_check_required_by_all_parameters_present():
    requirements = {'key1': 'required1'}
    parameters = {'key1': 'value1', 'required1': 'value2'}
    assert check_required_by(requirements, parameters) == {'key1': []}
