# file lib/ansible/playbook/playbook_include.py:47-49
# lines [49]
# branches []

import pytest
from ansible.playbook.playbook_include import PlaybookInclude
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

# Assuming the existence of the PlaybookInclude class with the load method as provided

class TestPlaybookInclude:
    def test_playbook_include_load(self, mocker):
        # Mock the load_data method to ensure it is called with correct parameters
        mocker.patch.object(PlaybookInclude, 'load_data', return_value='mocked_load_data')

        # Create necessary objects for the test
        data = {'some': 'data'}
        basedir = '/fake/path'
        variable_manager = VariableManager()
        loader = DataLoader()

        # Call the static load method
        result = PlaybookInclude.load(data, basedir, variable_manager, loader)

        # Assert that load_data was called with the correct parameters
        PlaybookInclude.load_data.assert_called_once_with(ds=data, basedir=basedir, variable_manager=variable_manager, loader=loader)

        # Assert that the result is what load_data returned
        assert result == 'mocked_load_data'
