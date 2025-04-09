# file: lib/ansible/cli/console.py:115-119
# asked: {"lines": [116, 117, 118, 119], "branches": []}
# gained: {"lines": [116, 117, 118, 119], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def mock_display():
    with patch('ansible.cli.console.display', new_callable=Display) as mock_display:
        yield mock_display

@pytest.fixture
def mock_cli():
    class MockCLI(ConsoleCLI):
        def __init__(self):
            self.parser = MagicMock()
            self.args = []
            self.SKIP_INVENTORY_DEFAULTS = False

        def validate_conflicts(self, options, runas_opts=False, fork_opts=False):
            return super(MockCLI, self).validate_conflicts(options, runas_opts, fork_opts)

    return MockCLI()

def test_post_process_args(mock_cli, mock_display):
    options = MagicMock()
    options.verbosity = 3
    options.forks = 1

    with patch.object(mock_cli, 'validate_conflicts', wraps=mock_cli.validate_conflicts) as mock_validate_conflicts:
        processed_options = mock_cli.post_process_args(options)

        assert processed_options == options
        assert mock_display.verbosity == 3
        mock_validate_conflicts.assert_called_once_with(options, runas_opts=True, fork_opts=True)
