# file lib/ansible/playbook/playbook_include.py:47-49
# lines [49]
# branches []

import pytest
from ansible.playbook.playbook_include import PlaybookInclude
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

# Mock classes to avoid side effects
class MockPlaybookInclude(PlaybookInclude):
    def load_data(self, ds, basedir, variable_manager, loader):
        # Mock load_data to simply return the data for testing purposes
        return ds

@pytest.fixture
def mock_playbook_include(mocker):
    mocker.patch('ansible.playbook.playbook_include.PlaybookInclude', new=MockPlaybookInclude)

def test_playbook_include_load_executes_line_49(mock_playbook_include):
    # Setup test data and mocks
    data = {'some': 'data'}
    basedir = '/fake/path'
    variable_manager = VariableManager()
    loader = DataLoader()

    # Call the static method load
    result = PlaybookInclude.load(data, basedir, variable_manager, loader)

    # Assert that the result is the same as the data passed in, confirming load_data was called
    assert result == data
