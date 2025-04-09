# file lib/ansible/playbook/playbook_include.py:47-49
# lines [47, 48, 49]
# branches []

import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.playbook_include import PlaybookInclude

@pytest.fixture
def mock_playbook_include(mocker):
    mocker.patch('ansible.playbook.playbook_include.PlaybookInclude.load_data', return_value='mocked_data')
    yield

def test_playbook_include_load(mock_playbook_include):
    data = {'key': 'value'}
    basedir = '/mock/basedir'
    variable_manager = MagicMock()
    loader = MagicMock()

    result = PlaybookInclude.load(data, basedir, variable_manager, loader)

    assert result == 'mocked_data'
    PlaybookInclude.load_data.assert_called_once_with(ds=data, basedir=basedir, variable_manager=variable_manager, loader=loader)
