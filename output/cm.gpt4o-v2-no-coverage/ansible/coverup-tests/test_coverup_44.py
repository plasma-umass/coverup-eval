# file: lib/ansible/module_utils/common/validation.py:173-210
# asked: {"lines": [173, 187, 188, 189, 191, 192, 193, 194, 196, 197, 198, 199, 200, 202, 203, 204, 205, 206, 207, 208, 210], "branches": [[188, 189], [188, 191], [191, 192], [191, 202], [192, 193], [192, 194], [196, 197], [196, 198], [198, 191], [198, 199], [199, 198], [199, 200], [202, 203], [202, 210], [203, 204], [203, 210], [204, 203], [204, 205], [206, 207], [206, 208]]}
# gained: {"lines": [173, 187, 188, 189, 191, 192, 193, 194, 196, 197, 198, 199, 200, 202, 203, 204, 205, 206, 207, 208, 210], "branches": [[188, 189], [188, 191], [191, 192], [191, 202], [192, 193], [192, 194], [196, 197], [196, 198], [198, 191], [198, 199], [199, 198], [199, 200], [202, 203], [202, 210], [203, 204], [203, 210], [204, 203], [204, 205], [206, 207], [206, 208]]}

import pytest
from ansible.module_utils.common.validation import check_required_by
from ansible.module_utils._text import to_native
from ansible.module_utils.six import string_types

def test_check_required_by_no_requirements():
    assert check_required_by(None, {}) == {}

def test_check_required_by_empty_requirements():
    assert check_required_by({}, {}) == {}

def test_check_required_by_no_parameters():
    requirements = {'a': 'b'}
    assert check_required_by(requirements, {}) == {}

def test_check_required_by_parameter_not_none():
    requirements = {'a': 'b'}
    parameters = {'a': 'value', 'b': 'value'}
    assert check_required_by(requirements, parameters) == {'a': []}

def test_check_required_by_single_string():
    requirements = {'a': 'b'}
    parameters = {'a': 'value', 'b': 'value'}
    assert check_required_by(requirements, parameters) == {'a': []}

def test_check_required_by_list_of_values():
    requirements = {'a': ['b', 'c']}
    parameters = {'a': 'value', 'b': 'value', 'c': 'value'}
    assert check_required_by(requirements, parameters) == {'a': []}

def test_check_required_by_missing_parameter():
    requirements = {'a': 'b'}
    parameters = {'a': 'value'}
    with pytest.raises(TypeError, match="missing parameter\\(s\\) required by 'a': b"):
        check_required_by(requirements, parameters)

def test_check_required_by_missing_parameter_with_context():
    requirements = {'a': 'b'}
    parameters = {'a': 'value'}
    options_context = ['context1', 'context2']
    with pytest.raises(TypeError, match="missing parameter\\(s\\) required by 'a': b found in context1 -> context2"):
        check_required_by(requirements, parameters, options_context)

def test_check_required_by_multiple_missing_parameters():
    requirements = {'a': ['b', 'c']}
    parameters = {'a': 'value', 'b': 'value'}
    with pytest.raises(TypeError, match="missing parameter\\(s\\) required by 'a': c"):
        check_required_by(requirements, parameters)

def test_check_required_by_multiple_missing_parameters_with_context():
    requirements = {'a': ['b', 'c']}
    parameters = {'a': 'value', 'b': 'value'}
    options_context = ['context1', 'context2']
    with pytest.raises(TypeError, match="missing parameter\\(s\\) required by 'a': c found in context1 -> context2"):
        check_required_by(requirements, parameters, options_context)
