# file: lib/ansible/module_utils/common/validation.py:246-335
# asked: {"lines": [], "branches": [[316, 321], [328, 335]]}
# gained: {"lines": [], "branches": [[316, 321]]}

import pytest
from ansible.module_utils.common.validation import check_required_if
from ansible.module_utils._text import to_native

def test_check_required_if_no_requirements():
    assert check_required_if(None, {}) == []

def test_check_required_if_empty_requirements():
    assert check_required_if([], {}) == []

def test_check_required_if_all_requirements_met():
    requirements = [['state', 'present', ('path',), True]]
    parameters = {'state': 'present', 'path': '/some/path'}
    assert check_required_if(requirements, parameters) == []

def test_check_required_if_any_requirement_missing():
    requirements = [['state', 'present', ('path',), True]]
    parameters = {'state': 'present'}
    with pytest.raises(TypeError) as excinfo:
        check_required_if(requirements, parameters)
    assert "state is present but any of the following are missing: path" in str(excinfo.value)

def test_check_required_if_all_requirements_missing():
    requirements = [['state', 'present', ('path', 'name')]]
    parameters = {'state': 'present'}
    with pytest.raises(TypeError) as excinfo:
        check_required_if(requirements, parameters)
    assert "state is present but all of the following are missing: path, name" in str(excinfo.value)

def test_check_required_if_with_options_context():
    requirements = [['state', 'present', ('path',), True]]
    parameters = {'state': 'present'}
    options_context = ['parent']
    with pytest.raises(TypeError) as excinfo:
        check_required_if(requirements, parameters, options_context)
    assert "state is present but any of the following are missing: path found in parent" in str(excinfo.value)

def test_check_required_if_no_parameters():
    requirements = [['state', 'present', ('path',), True]]
    parameters = {}
    assert check_required_if(requirements, parameters) == []

def test_check_required_if_partial_requirements_met():
    requirements = [['state', 'present', ('path', 'name')]]
    parameters = {'state': 'present', 'path': '/some/path'}
    with pytest.raises(TypeError) as excinfo:
        check_required_if(requirements, parameters)
    assert "state is present but all of the following are missing: name" in str(excinfo.value)
