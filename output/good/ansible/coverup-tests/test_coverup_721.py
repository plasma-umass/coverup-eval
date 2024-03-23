# file lib/ansible/cli/arguments/option_helpers.py:277-280
# lines [277, 279, 280]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.cli.arguments.option_helpers import add_fork_options

class MockParser:
    def add_argument(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

@pytest.fixture
def mock_parser():
    return MockParser()

def test_add_fork_options(mock_parser):
    add_fork_options(mock_parser)
    assert mock_parser.args == ('-f', '--forks')
    assert mock_parser.kwargs['dest'] == 'forks'
    assert mock_parser.kwargs['default'] == 5  # Assuming C.DEFAULT_FORKS is 5
    assert mock_parser.kwargs['type'] == int
    assert "specify number of parallel processes to use (default=5)" in mock_parser.kwargs['help']
