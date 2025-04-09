# file lib/ansible/template/vars.py:43-59
# lines [43, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
# branches ['53->exit', '53->54', '54->exit', '54->55', '55->54', '55->56', '56->57', '56->58', '58->54', '58->59']

import pytest
from ansible.template.vars import AnsibleJ2Vars
from ansible.template import Templar

@pytest.fixture
def templar(mocker):
    return mocker.MagicMock(spec=Templar)

@pytest.fixture
def globals_dict():
    return {'global_var': 'global_value'}

@pytest.fixture
def locals_dict():
    return {
        'l_local_var': 'local_value',
        'context': 'should_not_be_included',
        'environment': 'should_not_be_included',
        'template': 'should_not_be_included',
        'normal_var': 'normal_value',
        'missing_var': None  # Assuming None is used to represent missing values
    }

def test_ansible_j2vars_init(templar, globals_dict, locals_dict):
    # Filter out the 'missing_var' since it should not be included in the locals
    filtered_locals_dict = {k: v for k, v in locals_dict.items() if v is not None}
    ansible_j2vars = AnsibleJ2Vars(templar, globals_dict, filtered_locals_dict)

    # Check that the globals are set correctly
    assert ansible_j2vars._globals == globals_dict

    # Check that the locals are set correctly, excluding keys with special prefixes or missing values
    expected_locals = {
        'local_var': 'local_value',
        'normal_var': 'normal_value'
    }
    assert ansible_j2vars._locals == expected_locals

    # Check that keys with special prefixes are stripped
    assert 'l_local_var' not in ansible_j2vars._locals

    # Check that special keys are not included
    for key in ('context', 'environment', 'template'):
        assert key not in ansible_j2vars._locals

    # Check that missing values are not included
    assert 'missing_var' not in ansible_j2vars._locals
