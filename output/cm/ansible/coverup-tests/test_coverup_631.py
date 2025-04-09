# file lib/ansible/cli/arguments/option_helpers.py:216-221
# lines [216, 218, 219, 220, 221]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.constants import DEFAULT_POLL_INTERVAL
from ansible.cli.arguments.option_helpers import add_async_options

class MockParser:
    def add_argument(self, *args, **kwargs):
        pass

@pytest.fixture
def mock_parser(mocker):
    parser = MockParser()
    mocker.patch.object(parser, 'add_argument')
    return parser

def test_add_async_options(mock_parser):
    add_async_options(mock_parser)
    
    # Verify that add_argument was called with the expected arguments for '--poll'
    mock_parser.add_argument.assert_any_call(
        '-P', '--poll', default=DEFAULT_POLL_INTERVAL, type=int, dest='poll_interval',
        help="set the poll interval if using -B (default=%s)" % DEFAULT_POLL_INTERVAL
    )
    
    # Verify that add_argument was called with the expected arguments for '--background'
    mock_parser.add_argument.assert_any_call(
        '-B', '--background', dest='seconds', type=int, default=0,
        help='run asynchronously, failing after X seconds (default=N/A)'
    )
    
    # Verify that add_argument was called exactly two times
    assert mock_parser.add_argument.call_count == 2
