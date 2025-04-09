# file lib/ansible/playbook/play.py:193-205
# lines [198, 199, 200, 201, 202, 204, 205]
# branches []

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.play import Play
from ansible.playbook.block import Block

# Assuming that the `load_list_of_blocks` function is imported from the correct module
# If not, please adjust the import statement accordingly
from ansible.playbook.helpers import load_list_of_blocks

# Mock for the load_list_of_blocks function to raise an AssertionError
def mock_load_list_of_blocks(ds, play, use_handlers, variable_manager, loader):
    raise AssertionError("Mocked assertion error for testing")

# Test function to cover lines 198-205
def test_play_load_handlers_assertion_error(mocker):
    # Mock the load_list_of_blocks to raise AssertionError
    mocker.patch('ansible.playbook.play.load_list_of_blocks', side_effect=mock_load_list_of_blocks)
    
    # Create a minimal Play object with necessary attributes
    play = Play()
    play.handlers = []
    play._variable_manager = mocker.MagicMock()
    play._loader = mocker.MagicMock()
    play._ds = {'name': 'test'}

    # Assert that AnsibleParserError is raised with the correct message
    with pytest.raises(AnsibleParserError) as exc_info:
        play._load_handlers(attr=None, ds=[{'block': 'test'}])

    assert "A malformed block was encountered while loading handlers" in str(exc_info.value)
    assert exc_info.value.orig_exc is not None
    assert isinstance(exc_info.value.orig_exc, AssertionError)
