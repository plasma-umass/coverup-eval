# file: lib/ansible/playbook/base.py:83-119
# asked: {"lines": [84, 85, 86, 87, 91, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119], "branches": [[96, 97], [96, 99], [99, 100], [99, 117], [100, 101], [100, 102], [102, 103], [102, 105], [106, 107], [106, 108], [109, 110], [109, 115], [110, 111], [110, 112], [113, 109], [113, 114], [115, 116], [115, 117], [117, 0], [117, 118]]}
# gained: {"lines": [84, 85, 86, 87, 91, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119], "branches": [[96, 97], [96, 99], [99, 100], [100, 101], [100, 102], [102, 103], [102, 105], [106, 107], [106, 108], [109, 110], [109, 115], [110, 111], [110, 112], [113, 109], [113, 114], [115, 116], [115, 117], [117, 0], [117, 118]]}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the function is imported from ansible.playbook.base
from ansible.playbook.base import _validate_action_group_metadata

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch('ansible.playbook.base.display.warning')

@pytest.fixture
def mock_validate_action_group_metadata(mocker):
    return mocker.patch('ansible.playbook.base.C.VALIDATE_ACTION_GROUP_METADATA', True)

def test_validate_action_group_metadata_no_metadata_key(mock_display_warning, mock_validate_action_group_metadata):
    action = {'some_key': 'some_value'}
    found_group_metadata = False
    fq_group_name = 'test_group'
    
    _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    mock_display_warning.assert_called_once()
    assert "The only expected key is metadata, but got keys: some_key" in mock_display_warning.call_args[0][0]

def test_validate_action_group_metadata_multiple_metadata_entries(mock_display_warning, mock_validate_action_group_metadata):
    action = {'metadata': {}}
    found_group_metadata = True
    fq_group_name = 'test_group'
    
    _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    mock_display_warning.assert_called_once()
    assert "The group contains multiple metadata entries." in mock_display_warning.call_args[0][0]

def test_validate_action_group_metadata_metadata_not_dict(mock_display_warning, mock_validate_action_group_metadata):
    action = {'metadata': 'not_a_dict'}
    found_group_metadata = False
    fq_group_name = 'test_group'
    
    _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    mock_display_warning.assert_called_once()
    assert "The metadata is not a dictionary. Got not_a_dict" in mock_display_warning.call_args[0][0]

def test_validate_action_group_metadata_unexpected_keys(mock_display_warning, mock_validate_action_group_metadata):
    action = {'metadata': {'unexpected_key': 'value'}}
    found_group_metadata = False
    fq_group_name = 'test_group'
    
    _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    mock_display_warning.assert_called_once()
    assert "The metadata contains unexpected keys: unexpected_key" in mock_display_warning.call_args[0][0]

def test_validate_action_group_metadata_unexpected_key_types(mock_display_warning, mock_validate_action_group_metadata):
    action = {'metadata': {'extend_group': 123}}
    found_group_metadata = False
    fq_group_name = 'test_group'
    
    _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    mock_display_warning.assert_called_once()
    assert "The metadata contains unexpected key types: extend_group is 123 (expected type list)" in mock_display_warning.call_args[0][0]

def test_validate_action_group_metadata_valid_metadata(mock_display_warning, mock_validate_action_group_metadata):
    action = {'metadata': {'extend_group': []}}
    found_group_metadata = False
    fq_group_name = 'test_group'
    
    _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    mock_display_warning.assert_not_called()
