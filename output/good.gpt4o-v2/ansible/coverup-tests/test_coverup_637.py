# file: lib/ansible/cli/arguments/option_helpers.py:373-378
# asked: {"lines": [373, 375, 376, 377, 378], "branches": []}
# gained: {"lines": [373, 375, 376, 377, 378], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.cli.arguments.option_helpers import add_subset_options
from ansible import constants as C

def test_add_subset_options():
    parser = MagicMock()
    add_subset_options(parser)
    
    parser.add_argument.assert_any_call(
        '-t', '--tags', dest='tags', default=C.TAGS_RUN, action='append',
        help='only run plays and tasks tagged with these values'
    )
    parser.add_argument.assert_any_call(
        '--skip-tags', dest='skip_tags', default=C.TAGS_SKIP, action='append',
        help='only run plays and tasks whose tags do not match these values'
    )
