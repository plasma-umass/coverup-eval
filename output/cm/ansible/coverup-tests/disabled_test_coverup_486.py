# file lib/ansible/playbook/play.py:133-138
# lines [133, 134, 135, 136, 137, 138]
# branches ['136->137', '136->138']

import pytest
from ansible.playbook.play import Play
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader

# Mock classes to avoid side effects
class MockVariableManager(VariableManager):
    def __init__(self):
        pass

class MockDataLoader(DataLoader):
    def __init__(self):
        pass

@pytest.fixture
def mock_variable_manager(mocker):
    mocker.patch('ansible.vars.manager.VariableManager', MockVariableManager)

@pytest.fixture
def mock_loader(mocker):
    mocker.patch('ansible.parsing.dataloader.DataLoader', MockDataLoader)

def test_play_load_with_vars(mock_variable_manager, mock_loader):
    # Setup
    data = {'name': 'test_play'}
    vars = {'some_var': 'value'}
    
    # Execute
    play = Play.load(data, vars=vars)
    
    # Assert
    assert play.vars == vars, "The vars should be copied to the play's vars attribute"
    
    # Cleanup is handled by the pytest fixtures and mock patches
