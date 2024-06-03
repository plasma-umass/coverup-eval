# file httpie/cli/argparser.py:259-283
# lines [259, 265, 267, 268, 269, 270, 273, 274, 275, 276, 277, 279, 281, 282, 283]
# branches ['267->268', '267->281', '268->269', '268->273', '274->275', '274->279', '275->274', '275->276', '281->exit', '281->282']

import pytest
import argparse
from unittest import mock

# Assuming the HTTPieArgumentParser class is defined in httpie.cli.argparser
from httpie.cli.argparser import HTTPieArgumentParser

@pytest.fixture
def parser():
    parser = HTTPieArgumentParser()
    parser.args = argparse.Namespace()
    return parser

def test_apply_no_options_valid(parser):
    parser.add_argument('--option', dest='option', default='default_value')
    parser.args.option = 'some_value'
    
    parser._apply_no_options(['--no-option'])
    
    assert parser.args.option == 'default_value'

def test_apply_no_options_invalid(parser, mocker):
    mocker.patch.object(parser, 'error', side_effect=SystemExit)
    with pytest.raises(SystemExit):
        parser._apply_no_options(['--no-nonexistent'])

def test_apply_no_options_mixed(parser, mocker):
    parser.add_argument('--option', dest='option', default='default_value')
    parser.args.option = 'some_value'
    
    mocker.patch.object(parser, 'error', side_effect=SystemExit)
    with pytest.raises(SystemExit):
        parser._apply_no_options(['--no-option', '--no-nonexistent'])
    
    assert parser.args.option == 'default_value'
