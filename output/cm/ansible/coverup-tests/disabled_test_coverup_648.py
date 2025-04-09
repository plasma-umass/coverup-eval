# file lib/ansible/playbook/play.py:163-171
# lines [163, 168, 169, 170, 171]
# branches []

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.play import Play
from ansible.playbook.block import Block
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

# Mocking the necessary parts to test the Play class
class MockLoader(DataLoader):
    pass

class MockVariableManager(VariableManager):
    pass

# The test function to cover the missing lines/branches in Play._load_tasks
def test_play_load_tasks_with_malformed_block(mocker):
    # Mock the load_list_of_blocks function to raise an AssertionError
    mocker.patch('ansible.playbook.play.load_list_of_blocks', side_effect=AssertionError("malformed block"))

    # Create instances of the necessary objects
    loader = MockLoader()
    variable_manager = MockVariableManager(loader=loader)

    # Create a Play object with the mocked loader and variable manager
    play = Play()
    play._loader = loader
    play._variable_manager = variable_manager
    play._ds = {'name': 'test'}

    # Define a malformed tasks list
    malformed_tasks = [{'malformed': 'task'}]

    # Test that AnsibleParserError is raised with the correct message
    with pytest.raises(AnsibleParserError) as exc_info:
        play._load_tasks(attr='tasks', ds=malformed_tasks)

    # Verify the exception message
    assert "A malformed block was encountered while loading tasks" in str(exc_info.value)

    # Verify that the original exception is attached
    assert isinstance(exc_info.value.orig_exc, AssertionError)
