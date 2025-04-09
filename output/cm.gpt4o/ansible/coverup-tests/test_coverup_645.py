# file lib/ansible/cli/arguments/option_helpers.py:155-158
# lines [155, 156, 157, 158]
# branches []

import os
import pytest
from unittest import mock
from ansible.cli.arguments.option_helpers import _gitinfo

@pytest.fixture
def mock_os_path(mocker):
    mocker.patch('os.path.normpath', return_value='/mocked/path')
    mocker.patch('os.path.join', side_effect=lambda *args: '/'.join(args))
    mocker.patch('os.path.dirname', return_value='/mocked/dirname')
    return mocker

def test_gitinfo(mock_os_path):
    with mock.patch('ansible.cli.arguments.option_helpers._git_repo_info', return_value={'mocked': 'info'}) as mock_git_repo_info:
        result = _gitinfo()
        assert result == {'mocked': 'info'}
        mock_git_repo_info.assert_called_once_with('/mocked/path/.git')
