# file lib/ansible/playbook/play.py:133-138
# lines [135, 136, 137, 138]
# branches ['136->137', '136->138']

import pytest
from ansible.playbook.play import Play
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader

# Assuming the Play class is part of a larger module, we need to mock dependencies
# that are not relevant to the test.

@pytest.fixture
def variable_manager(mocker):
    return mocker.MagicMock(spec=VariableManager)

@pytest.fixture
def loader(mocker):
    return mocker.MagicMock(spec=DataLoader)

def test_play_load_with_vars(variable_manager, loader):
    # Setup test data
    data = {'name': 'test_play'}
    test_vars = {'var1': 'value1', 'var2': 'value2'}

    # Call the method we're testing
    play = Play.load(data, variable_manager=variable_manager, loader=loader, vars=test_vars)

    # Assertions to check postconditions
    assert play.vars == test_vars
    variable_manager.assert_not_called()  # Assuming we don't want to interact with variable_manager in this test
    loader.assert_not_called()  # Assuming we don't want to interact with loader in this test
