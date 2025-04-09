# file: lib/ansible/playbook/playbook_include.py:47-49
# asked: {"lines": [47, 48, 49], "branches": []}
# gained: {"lines": [47, 48, 49], "branches": []}

import pytest
from ansible.playbook.playbook_include import PlaybookInclude

def test_playbook_include_load(mocker):
    mock_load_data = mocker.patch.object(PlaybookInclude, 'load_data', return_value="mocked_result")
    
    data = {"key": "value"}
    basedir = "/mock/basedir"
    variable_manager = mocker.Mock()
    loader = mocker.Mock()
    
    result = PlaybookInclude.load(data, basedir, variable_manager, loader)
    
    mock_load_data.assert_called_once_with(ds=data, basedir=basedir, variable_manager=variable_manager, loader=loader)
    assert result == "mocked_result"
