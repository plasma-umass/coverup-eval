# file httpie/cli/argparser.py:31-48
# lines [31, 32, 41, 43, 44, 46, 47, 48]
# branches []

import pytest
from httpie.cli.argparser import HTTPieHelpFormatter
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from textwrap import dedent

def test_httpie_help_formatter(mocker):
    parser = ArgumentParser(formatter_class=HTTPieHelpFormatter)
    parser.add_argument('--example', help="This is an example\nargument with multiple\nlines of help text.")
    
    # Mock the print_help method to capture the output
    mocker.patch('argparse.ArgumentParser.print_help')
    
    # Call print_help to trigger the formatter
    parser.print_help()
    
    # Verify that the formatter is used and the help text is formatted correctly
    expected_help_text = dedent("This is an example\nargument with multiple\nlines of help text.\n\n").splitlines()
    formatter = parser._get_formatter()
    help_text = formatter._split_lines(parser._actions[1].help, 80)  # Assuming a default width of 80
    
    assert help_text == expected_help_text
