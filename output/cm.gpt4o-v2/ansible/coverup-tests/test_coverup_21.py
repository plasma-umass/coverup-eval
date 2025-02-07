# file: lib/ansible/module_utils/common/validation.py:246-335
# asked: {"lines": [246, 294, 295, 296, 298, 299, 300, 301, 302, 303, 304, 306, 310, 311, 312, 314, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 327, 328, 329, 330, 331, 332, 333, 335], "branches": [[295, 296], [295, 298], [298, 299], [298, 327], [303, 304], [303, 306], [310, 311], [310, 314], [316, 317], [316, 321], [317, 318], [317, 321], [319, 317], [319, 320], [321, 298], [321, 322], [327, 328], [327, 335], [328, 329], [328, 335], [331, 332], [331, 333]]}
# gained: {"lines": [246, 294, 295, 296, 298, 299, 300, 301, 302, 303, 304, 306, 310, 311, 312, 314, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 327, 328, 329, 330, 331, 332, 333, 335], "branches": [[295, 296], [295, 298], [298, 299], [298, 327], [303, 304], [303, 306], [310, 311], [310, 314], [316, 317], [317, 318], [317, 321], [319, 317], [319, 320], [321, 298], [321, 322], [327, 328], [327, 335], [328, 329], [331, 332], [331, 333]]}

import pytest
from ansible.module_utils.common.validation import check_required_if

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

def test_check_required_if_any_requirement_missing():
    requirements = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    parameters = {
        'state': 'present',
        'someint': 99,
        'bool_param': True,
    }
    with pytest.raises(TypeError) as excinfo:
        check_required_if(requirements, parameters)
    assert "state is present but any of the following are missing: path" in str(excinfo.value)

def test_check_required_if_no_requirements():
    requirements = None
    parameters = {
        'state': 'present',
        'path': '/some/path',
        'someint': 99,
        'bool_param': True,
        'string_param': 'value'
    }
    assert check_required_if(requirements, parameters) == []

def test_check_required_if_with_options_context():
    requirements = [
        ['state', 'present', ('path',), True],
    ]
    parameters = {
        'state': 'present',
    }
    options_context = ['parent_key']
    with pytest.raises(TypeError) as excinfo:
        check_required_if(requirements, parameters, options_context=options_context)
    assert "state is present but any of the following are missing: path found in parent_key" in str(excinfo.value)

def test_check_required_if_is_one_of():
    requirements = [
        ['state', 'present', ('path', 'other_path'), True],
    ]
    parameters = {
        'state': 'present',
        'other_path': '/some/other/path'
    }
    assert check_required_if(requirements, parameters) == []
