# file: lib/ansible/cli/arguments/option_helpers.py:373-378
# asked: {"lines": [373, 375, 376, 377, 378], "branches": []}
# gained: {"lines": [373, 375, 376, 377, 378], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.cli.arguments.option_helpers import add_subset_options
from ansible import constants as C

def test_add_subset_options(monkeypatch):
    # Mocking the constants
    mock_constants = MagicMock()
    mock_constants.TAGS_RUN = 'mock_tags_run'
    mock_constants.TAGS_SKIP = 'mock_tags_skip'
    
    monkeypatch.setattr(C, 'TAGS_RUN', mock_constants.TAGS_RUN)
    monkeypatch.setattr(C, 'TAGS_SKIP', mock_constants.TAGS_SKIP)
    
    # Mocking the parser
    mock_parser = MagicMock()
    
    add_subset_options(mock_parser)
    
    # Assertions to verify that add_argument was called with the correct parameters
    mock_parser.add_argument.assert_any_call(
        '-t', '--tags', dest='tags', default='mock_tags_run', action='append',
        help='only run plays and tasks tagged with these values'
    )
    mock_parser.add_argument.assert_any_call(
        '--skip-tags', dest='skip_tags', default='mock_tags_skip', action='append',
        help='only run plays and tasks whose tags do not match these values'
    )
