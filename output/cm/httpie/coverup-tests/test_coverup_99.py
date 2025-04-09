# file httpie/cli/argparser.py:259-283
# lines [265, 267, 268, 269, 270, 273, 274, 275, 276, 277, 279, 281, 282, 283]
# branches ['267->268', '267->281', '268->269', '268->273', '274->275', '274->279', '275->274', '275->276', '281->exit', '281->282']

import argparse
import pytest
from httpie.cli.argparser import HTTPieArgumentParser

class TestHTTPieArgumentParser:

    @pytest.fixture
    def parser(self, mocker):
        parser = HTTPieArgumentParser()
        parser.args = argparse.Namespace()
        mocker.patch.object(parser, 'error')
        return parser

    def test_apply_no_options_with_invalid_options(self, parser):
        parser._apply_no_options(['--no-invalid', '--another-invalid'])
        parser.error.assert_called_once_with('unrecognized arguments: --no-invalid --another-invalid')

    def test_apply_no_options_with_mixed_options(self, parser, mocker):
        # Mock actions to simulate existing --option
        action = argparse.Action(
            option_strings=['--option'],
            dest='option',
            nargs=None,
            const=None,
            default=None,
            type=None,
            choices=None,
            required=False,
            help=None,
            metavar=None
        )
        mocker.patch.object(parser, '_actions', [action])
        parser.args.option = None

        # Apply no-options with one valid and one invalid
        parser._apply_no_options(['--no-option', '--no-invalid'])

        # Check that the valid option was reset to its default
        assert parser.args.option is None
        # Check that the invalid option triggered an error
        parser.error.assert_called_once_with('unrecognized arguments: --no-invalid')

    def test_apply_no_options_with_valid_options(self, parser, mocker):
        # Mock actions to simulate existing --option
        action = argparse.Action(
            option_strings=['--option'],
            dest='option',
            nargs=None,
            const=None,
            default='default_value',
            type=None,
            choices=None,
            required=False,
            help=None,
            metavar=None
        )
        mocker.patch.object(parser, '_actions', [action])
        parser.args.option = 'changed_value'

        # Apply no-options with a valid option
        parser._apply_no_options(['--no-option'])

        # Check that the option was reset to its default
        assert parser.args.option == 'default_value'
        # Check that no error was called
        parser.error.assert_not_called()
