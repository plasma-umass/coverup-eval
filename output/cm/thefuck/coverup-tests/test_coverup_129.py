# file thefuck/shells/generic.py:56-71
# lines [65]
# branches ['59->exit', '64->65', '70->67']

import os
import pytest
from thefuck.shells.generic import Generic
from thefuck.conf import settings

class TestGenericShellHistory:

    @pytest.fixture
    def generic_shell(self, mocker):
        mocker.patch('thefuck.shells.generic.Generic._get_history_file_name', return_value='history_test_file')
        mocker.patch('thefuck.shells.generic.Generic._script_from_history', side_effect=lambda x: x.strip())
        return Generic()

    @pytest.fixture
    def history_file(self, tmpdir):
        file = tmpdir.join('history_test_file')
        file.write('command1\ncommand2\ncommand3\n')
        return str(file)

    def test_get_history_lines_with_limit(self, mocker, generic_shell, history_file):
        mocker.patch('os.path.isfile', return_value=True)
        mocker.patch('io.open', mocker.mock_open(read_data='command1\ncommand2\ncommand3\n'))
        settings.history_limit = 2

        history_lines = list(generic_shell._get_history_lines())

        assert history_lines == ['command2', 'command3']
        assert len(history_lines) == settings.history_limit

    def test_get_history_lines_without_limit(self, mocker, generic_shell, history_file):
        mocker.patch('os.path.isfile', return_value=True)
        mocker.patch('io.open', mocker.mock_open(read_data='command1\ncommand2\ncommand3\n'))
        settings.history_limit = None

        history_lines = list(generic_shell._get_history_lines())

        assert history_lines == ['command1', 'command2', 'command3']

    def test_get_history_lines_with_empty_lines(self, mocker, generic_shell, history_file):
        mocker.patch('os.path.isfile', return_value=True)
        mocker.patch('io.open', mocker.mock_open(read_data='\n\ncommand1\n\ncommand2\ncommand3\n\n'))
        settings.history_limit = None

        history_lines = list(generic_shell._get_history_lines())

        assert history_lines == ['command1', 'command2', 'command3']

    def test_get_history_lines_file_not_exist(self, mocker, generic_shell):
        mocker.patch('os.path.isfile', return_value=False)

        history_lines = list(generic_shell._get_history_lines())

        assert history_lines == []

@pytest.fixture(autouse=True)
def reset_settings():
    original_history_limit = settings.history_limit
    yield
    settings.history_limit = original_history_limit
