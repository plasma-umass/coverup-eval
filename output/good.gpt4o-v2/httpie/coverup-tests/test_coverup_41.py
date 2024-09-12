# file: httpie/cli/argparser.py:440-444
# asked: {"lines": [440, 441, 442, 443, 444], "branches": [[442, 443], [442, 444]]}
# gained: {"lines": [440, 441, 442, 443, 444], "branches": [[442, 443], [442, 444]]}

import pytest
from unittest.mock import MagicMock
from httpie.cli.argparser import HTTPieArgumentParser
from httpie.cli.argtypes import PARSED_DEFAULT_FORMAT_OPTIONS, parse_format_options

def test_process_format_options_with_defaults(monkeypatch):
    parser = HTTPieArgumentParser()
    parser.args = MagicMock()
    parser.args.format_options = None

    parser._process_format_options()

    assert parser.args.format_options == PARSED_DEFAULT_FORMAT_OPTIONS

def test_process_format_options_with_custom_options(monkeypatch):
    parser = HTTPieArgumentParser()
    parser.args = MagicMock()
    custom_options = 'json.indent:2,json.sort_keys:false'
    parser.args.format_options = [custom_options]

    parser._process_format_options()

    expected_options = parse_format_options(custom_options, defaults=PARSED_DEFAULT_FORMAT_OPTIONS)
    assert parser.args.format_options == expected_options
