# file: lib/ansible/playbook/base.py:83-119
# asked: {"lines": [84, 85, 86, 87, 91, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119], "branches": [[96, 97], [96, 99], [99, 100], [99, 117], [100, 101], [100, 102], [102, 103], [102, 105], [106, 107], [106, 108], [109, 110], [109, 115], [110, 111], [110, 112], [113, 109], [113, 114], [115, 116], [115, 117], [117, 0], [117, 118]]}
# gained: {"lines": [84, 85, 86, 87, 91, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119], "branches": [[96, 97], [96, 99], [99, 100], [99, 117], [100, 101], [100, 102], [102, 103], [102, 105], [106, 107], [106, 108], [109, 110], [109, 115], [110, 111], [110, 112], [113, 114], [115, 116], [115, 117], [117, 0], [117, 118]]}

import pytest
from ansible.playbook.base import _validate_action_group_metadata
from ansible import constants as C
from unittest.mock import patch

@pytest.fixture
def mock_display_warning():
    with patch('ansible.playbook.base.display.warning') as mock_warning:
        yield mock_warning

def test_validate_action_group_metadata_no_validate(mock_display_warning):
    C.VALIDATE_ACTION_GROUP_METADATA = False
    action = {'some_key': 'some_value'}
    found_group_metadata = False
    fq_group_name = 'test_group'
    
    _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    mock_display_warning.assert_not_called()

def test_validate_action_group_metadata_metadata_only(mock_display_warning):
    C.VALIDATE_ACTION_GROUP_METADATA = True
    action = {'metadata': {}}
    found_group_metadata = False
    fq_group_name = 'test_group'
    
    _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    mock_display_warning.assert_not_called()

def test_validate_action_group_metadata_unexpected_keys(mock_display_warning):
    C.VALIDATE_ACTION_GROUP_METADATA = True
    action = {'metadata': {'unexpected_key': 'value'}}
    found_group_metadata = False
    fq_group_name = 'test_group'
    
    _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    mock_display_warning.assert_called_once()
    assert "unexpected keys" in mock_display_warning.call_args[0][0]

def test_validate_action_group_metadata_unexpected_types(mock_display_warning):
    C.VALIDATE_ACTION_GROUP_METADATA = True
    action = {'metadata': {'extend_group': 123}}
    found_group_metadata = False
    fq_group_name = 'test_group'
    
    _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    mock_display_warning.assert_called_once()
    assert "unexpected key types" in mock_display_warning.call_args[0][0]

def test_validate_action_group_metadata_multiple_metadata_entries(mock_display_warning):
    C.VALIDATE_ACTION_GROUP_METADATA = True
    action = {'metadata': {}}
    found_group_metadata = True
    fq_group_name = 'test_group'
    
    _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    mock_display_warning.assert_called_once()
    assert "multiple metadata entries" in mock_display_warning.call_args[0][0]

def test_validate_action_group_metadata_metadata_not_dict(mock_display_warning):
    C.VALIDATE_ACTION_GROUP_METADATA = True
    action = {'metadata': 'not_a_dict'}
    found_group_metadata = False
    fq_group_name = 'test_group'
    
    _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    mock_display_warning.assert_called_once()
    assert "metadata is not a dictionary" in mock_display_warning.call_args[0][0]

def test_validate_action_group_metadata_invalid_metadata(mock_display_warning):
    C.VALIDATE_ACTION_GROUP_METADATA = True
    action = {'some_key': 'some_value'}
    found_group_metadata = False
    fq_group_name = 'test_group'
    
    _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    
    mock_display_warning.assert_called_once()
    assert "Invalid metadata was found" in mock_display_warning.call_args[0][0]
