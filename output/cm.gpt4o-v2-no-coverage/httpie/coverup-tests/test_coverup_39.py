# file: httpie/cli/argparser.py:31-48
# asked: {"lines": [31, 32, 41, 43, 44, 46, 47, 48], "branches": []}
# gained: {"lines": [31, 32, 41, 43, 44, 46, 47, 48], "branches": []}

import pytest
from httpie.cli.argparser import HTTPieHelpFormatter
from argparse import ArgumentParser, HelpFormatter

def test_httpie_help_formatter_init():
    class CustomArgumentParser(ArgumentParser):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.formatter_class = HTTPieHelpFormatter

    parser = CustomArgumentParser(prog='test')
    formatter = parser.formatter_class(prog='test')
    assert isinstance(formatter, HTTPieHelpFormatter)
    assert formatter._max_help_position == 6

def test_httpie_help_formatter_split_lines():
    formatter = HTTPieHelpFormatter(prog='test')
    text = "    This is a test.\n    This should be dedented."
    expected_output = ["This is a test.", "This should be dedented.", ""]
    assert formatter._split_lines(text, width=80) == expected_output
