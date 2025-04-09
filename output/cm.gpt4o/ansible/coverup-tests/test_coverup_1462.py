# file lib/ansible/playbook/base.py:83-119
# lines []
# branches ['99->117', '113->109', '117->exit']

import pytest
from unittest import mock
from ansible.playbook.base import _validate_action_group_metadata

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch('ansible.playbook.base.display.warning')

def test_validate_action_group_metadata_case_99_to_117(mock_display_warning):
    action = {'metadata': 'not_a_dict'}
    found_group_metadata = True
    fq_group_name = 'test_group'
    
    with mock.patch('ansible.playbook.base.C.VALIDATE_ACTION_GROUP_METADATA', True):
        _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    assert mock_display_warning.called
    assert "Invalid metadata was found for action_group test_group while loading module_defaults." in mock_display_warning.call_args[0][0]
    assert "The group contains multiple metadata entries." in mock_display_warning.call_args[0][0]
    assert "The metadata is not a dictionary. Got not_a_dict" in mock_display_warning.call_args[0][0]

def test_validate_action_group_metadata_case_113_to_109(mock_display_warning):
    action = {'metadata': {'extend_group': 123}}
    found_group_metadata = False
    fq_group_name = 'test_group'
    
    with mock.patch('ansible.playbook.base.C.VALIDATE_ACTION_GROUP_METADATA', True):
        _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    assert mock_display_warning.called
    assert "Invalid metadata was found for action_group test_group while loading module_defaults." in mock_display_warning.call_args[0][0]
    assert "The metadata contains unexpected key types: extend_group is 123 (expected type list)" in mock_display_warning.call_args[0][0]

def test_validate_action_group_metadata_case_117_exit(mock_display_warning):
    action = {'metadata': {'unexpected_key': 'value'}}
    found_group_metadata = False
    fq_group_name = 'test_group'
    
    with mock.patch('ansible.playbook.base.C.VALIDATE_ACTION_GROUP_METADATA', True):
        _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    assert mock_display_warning.called
    assert "Invalid metadata was found for action_group test_group while loading module_defaults." in mock_display_warning.call_args[0][0]
    assert "The metadata contains unexpected keys: unexpected_key" in mock_display_warning.call_args[0][0]

def test_validate_action_group_metadata_all_branches(mock_display_warning):
    action = {'metadata': {'extend_group': ['valid_list'], 'unexpected_key': 'value'}}
    found_group_metadata = True
    fq_group_name = 'test_group'
    
    with mock.patch('ansible.playbook.base.C.VALIDATE_ACTION_GROUP_METADATA', True):
        _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    assert mock_display_warning.called
    assert "Invalid metadata was found for action_group test_group while loading module_defaults." in mock_display_warning.call_args[0][0]
    assert "The group contains multiple metadata entries." in mock_display_warning.call_args[0][0]
    assert "The metadata contains unexpected keys: unexpected_key" in mock_display_warning.call_args[0][0]
