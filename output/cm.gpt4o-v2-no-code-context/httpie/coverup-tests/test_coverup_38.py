# file: httpie/cli/argparser.py:31-48
# asked: {"lines": [31, 32, 41, 43, 44, 46, 47, 48], "branches": []}
# gained: {"lines": [31, 32, 41, 43, 44, 46, 47, 48], "branches": []}

import pytest
from httpie.cli.argparser import HTTPieHelpFormatter
from textwrap import dedent
import argparse

def test_httpie_help_formatter_init():
    formatter = HTTPieHelpFormatter(prog='test_prog')
    assert formatter._max_help_position == 6

def test_httpie_help_formatter_split_lines():
    formatter = HTTPieHelpFormatter(prog='test_prog')
    text = "    This is a test.\n    This should be dedented."
    expected_output = ["This is a test.", "This should be dedented.", ""]
    assert formatter._split_lines(text, width=80) == expected_output

def test_httpie_help_formatter_with_argparse(monkeypatch):
    parser = argparse.ArgumentParser(prog='test_prog', formatter_class=HTTPieHelpFormatter)
    parser.add_argument('--test', help="    This is a test help.\n    It should be dedented.")
    with monkeypatch.context() as m:
        m.setattr('sys.stdout.write', lambda x: None)
        parser.print_help()
