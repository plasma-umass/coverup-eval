# file: lib/ansible/module_utils/common/validation.py:246-335
# asked: {"lines": [298, 299, 300, 301, 302, 303, 304, 306, 310, 311, 312, 314, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 327, 328, 329, 330, 331, 332, 333, 335], "branches": [[295, 298], [298, 299], [298, 327], [303, 304], [303, 306], [310, 311], [310, 314], [316, 317], [316, 321], [317, 318], [317, 321], [319, 317], [319, 320], [321, 298], [321, 322], [327, 328], [327, 335], [328, 329], [328, 335], [331, 332], [331, 333]]}
# gained: {"lines": [298, 299, 300, 301, 302, 303, 304, 306, 310, 311, 312, 314, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 327, 328, 329, 330, 331, 332, 333, 335], "branches": [[295, 298], [298, 299], [298, 327], [303, 304], [303, 306], [310, 311], [310, 314], [316, 317], [317, 318], [317, 321], [319, 317], [319, 320], [321, 298], [321, 322], [327, 328], [327, 335], [328, 329], [331, 332], [331, 333]]}

import pytest
from ansible.module_utils.common.validation import check_required_if
from ansible.module_utils._text import to_native

def test_check_required_if_no_requirements():
    assert check_required_if(None, {}) == []

def test_check_required_if_empty_requirements():
    assert check_required_if([], {}) == []

def test_check_required_if_all_requirements_met():
    requirements = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    parameters = {
        'state': 'present',
        'path': '/some/path',
        'someint': 99,
        'bool_param': True,
        'string_param': 'value'
    }
    assert check_required_if(requirements, parameters) == []

def test_check_required_if_missing_all_requirements():
    requirements = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    parameters = {
        'state': 'present',
        'someint': 99,
    }
    with pytest.raises(TypeError) as excinfo:
        check_required_if(requirements, parameters)
    assert "state is present but any of the following are missing: path" in str(excinfo.value)

def test_check_required_if_missing_some_requirements():
    requirements = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    parameters = {
        'state': 'present',
        'path': '/some/path',
        'someint': 99,
        'bool_param': True,
    }
    with pytest.raises(TypeError) as excinfo:
        check_required_if(requirements, parameters)
    assert "someint is 99 but all of the following are missing: string_param" in str(excinfo.value)

def test_check_required_if_with_options_context():
    requirements = [
        ['state', 'present', ('path',), True],
    ]
    parameters = {
        'state': 'present',
    }
    options_context = ['parent']
    with pytest.raises(TypeError) as excinfo:
        check_required_if(requirements, parameters, options_context)
    assert "state is present but any of the following are missing: path found in parent" in str(excinfo.value)
