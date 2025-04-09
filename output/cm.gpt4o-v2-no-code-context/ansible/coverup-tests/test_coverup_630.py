# file: lib/ansible/playbook/playbook_include.py:47-49
# asked: {"lines": [47, 48, 49], "branches": []}
# gained: {"lines": [47, 48, 49], "branches": []}

import pytest
from ansible.playbook.playbook_include import PlaybookInclude

@pytest.fixture
def mock_playbook_include(mocker):
    mocker.patch.object(PlaybookInclude, 'load_data', return_value='mocked_result')
    return PlaybookInclude

def test_playbook_include_load(mock_playbook_include):
    data = {'some': 'data'}
    basedir = '/mock/basedir'
    variable_manager = 'mock_variable_manager'
    loader = 'mock_loader'

    result = mock_playbook_include.load(data, basedir, variable_manager, loader)
    
    assert result == 'mocked_result'
    mock_playbook_include.load_data.assert_called_once_with(ds=data, basedir=basedir, variable_manager=variable_manager, loader=loader)
