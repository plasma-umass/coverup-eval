# file lib/ansible/cli/arguments/option_helpers.py:373-378
# lines [373, 375, 376, 377, 378]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the module structure and class names based on the provided code snippet
# Since the import for ansible.constants.DEFAULTS failed, we'll mock the constants
C = MagicMock()
C.TAGS_RUN = []
C.TAGS_SKIP = []

from ansible.cli.arguments.option_helpers import add_subset_options

class TestOptionHelpers:

    @pytest.fixture
    def parser(self, mocker):
        # Mock the parser to avoid side effects
        parser = mocker.MagicMock()
        parser.add_argument = MagicMock()
        return parser

    def test_add_subset_options(self, parser):
        # Call the function to test
        add_subset_options(parser)

        # Assert that add_argument was called with the expected arguments for '--tags'
        parser.add_argument.assert_any_call(
            '-t', '--tags', dest='tags', default=C.TAGS_RUN, action='append',
            help="only run plays and tasks tagged with these values"
        )

        # Assert that add_argument was called with the expected arguments for '--skip-tags'
        parser.add_argument.assert_any_call(
            '--skip-tags', dest='skip_tags', default=C.TAGS_SKIP, action='append',
            help="only run plays and tasks whose tags do not match these values"
        )

        # Assert that add_argument was called exactly two times
        assert parser.add_argument.call_count == 2
