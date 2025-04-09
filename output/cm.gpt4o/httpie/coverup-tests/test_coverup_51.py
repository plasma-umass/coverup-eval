# file httpie/cli/argparser.py:440-444
# lines [440, 441, 442, 443, 444]
# branches ['442->443', '442->444']

import pytest
from unittest import mock
import argparse
from httpie.cli.argparser import HTTPieArgumentParser, PARSED_DEFAULT_FORMAT_OPTIONS

def parse_format_options(options_group, defaults):
    # Mock implementation of parse_format_options
    return {**defaults, **options_group}

@pytest.fixture
def mock_parse_format_options(mocker):
    return mocker.patch('httpie.cli.argparser.parse_format_options', side_effect=parse_format_options)

def test_process_format_options(mock_parse_format_options):
    parser = HTTPieArgumentParser()
    parser.args = argparse.Namespace(format_options=[{'new': 'option'}])
    
    parser._process_format_options()
    
    expected_options = {**PARSED_DEFAULT_FORMAT_OPTIONS, 'new': 'option'}
    assert parser.args.format_options == expected_options
    mock_parse_format_options.assert_called_once_with({'new': 'option'}, defaults=PARSED_DEFAULT_FORMAT_OPTIONS)

def test_process_format_options_no_format_options(mock_parse_format_options):
    parser = HTTPieArgumentParser()
    parser.args = argparse.Namespace(format_options=None)
    
    parser._process_format_options()
    
    assert parser.args.format_options == PARSED_DEFAULT_FORMAT_OPTIONS
    mock_parse_format_options.assert_not_called()
