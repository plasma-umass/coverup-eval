# file lib/ansible/playbook/play.py:133-138
# lines [135, 136, 137, 138]
# branches ['136->137', '136->138']

import pytest
from ansible.playbook.play import Play
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader

# Assuming the existence of a test file named test_play.py

# New test function to cover lines 135-138
def test_play_load_with_vars(mocker):
    # Mocking the necessary components
    variable_manager = mocker.MagicMock(spec=VariableManager)
    loader = mocker.MagicMock(spec=DataLoader)
    data = {'name': 'test_play'}
    vars_to_copy = {'some_var': 'some_value'}

    # Call the static method with vars to trigger lines 135-138
    play = Play.load(data, variable_manager=variable_manager, loader=loader, vars=vars_to_copy)

    # Assertions to verify postconditions
    assert isinstance(play, Play)
    assert play.vars == vars_to_copy  # Ensure vars were copied correctly

    # Clean up is not necessary as we are using mocks and not modifying any global state
