# file lib/ansible/playbook/play.py:183-191
# lines [188, 189, 190, 191]
# branches []

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.play import Play
from ansible.playbook.block import Block

# Assuming that load_list_of_blocks is a function that needs to be mocked
# and that it raises an AssertionError when a malformed block is encountered.

def test_load_post_tasks_with_malformed_block(mocker):
    # Mock the necessary components
    mock_variable_manager = mocker.MagicMock()
    mock_loader = mocker.MagicMock()
    mock_ds = mocker.MagicMock()
    
    # Create a Play instance with the mocked components
    play = Play()
    play._variable_manager = mock_variable_manager
    play._loader = mock_loader
    play._ds = mock_ds
    
    # Mock the load_list_of_blocks function to raise an AssertionError
    mocker.patch('ansible.playbook.play.load_list_of_blocks', side_effect=AssertionError("Malformed block"))
    
    # Test that AnsibleParserError is raised with the correct message
    with pytest.raises(AnsibleParserError) as excinfo:
        play._load_post_tasks(attr=None, ds=mock_ds)
    
    assert "A malformed block was encountered while loading post_tasks" in str(excinfo.value)
    assert excinfo.value.obj == mock_ds
    assert isinstance(excinfo.value.orig_exc, AssertionError)
