# file lib/ansible/playbook/play.py:193-205
# lines [193, 198, 199, 200, 201, 202, 204, 205]
# branches []

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.play import Play
from ansible.playbook.block import Block
from ansible.template import Templar
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader

# Mock classes and functions
class MockLoader(DataLoader):
    pass

class MockVariableManager(VariableManager):
    def __init__(self):
        pass

def mock_load_list_of_blocks(ds, play, use_handlers, variable_manager, loader):
    if ds == "raise_assertion":
        raise AssertionError("test assertion")
    return [Block()]

# Test function
def test_play_load_handlers_with_assertion_error(mocker):
    # Setup
    mocker.patch('ansible.playbook.play.load_list_of_blocks', side_effect=mock_load_list_of_blocks)
    play = Play()
    play._variable_manager = MockVariableManager()
    play._loader = MockLoader()
    play.handlers = []
    play._ds = {}  # Set the _ds attribute to avoid AttributeError

    # Test with ds that raises an assertion error
    with pytest.raises(AnsibleParserError) as excinfo:
        play._load_handlers(attr=None, ds="raise_assertion")

    # Assertions
    assert "A malformed block was encountered while loading handlers" in str(excinfo.value)

    # Cleanup is handled by pytest's fixture scope
