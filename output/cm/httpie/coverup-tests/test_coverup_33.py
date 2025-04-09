# file httpie/cli/argparser.py:108-115
# lines [108, 109, 110, 111, 112, 113, 114]
# branches []

import argparse
import pytest
from httpie.cli.argparser import HTTPieArgumentParser
from httpie.cli.constants import RequestType

# Mock class to hold arguments
class Args:
    pass

@pytest.fixture
def parser(mocker):
    mocker.patch.object(HTTPieArgumentParser, '__init__', lambda self: None)
    parser = HTTPieArgumentParser()
    parser.args = Args()
    return parser

def test_process_request_type_json(parser):
    parser.args.request_type = RequestType.JSON
    parser._process_request_type()
    assert parser.args.json is True
    assert parser.args.multipart is False
    assert parser.args.form is False

def test_process_request_type_multipart(parser):
    parser.args.request_type = RequestType.MULTIPART
    parser._process_request_type()
    assert parser.args.json is False
    assert parser.args.multipart is True
    assert parser.args.form is True

def test_process_request_type_form(parser):
    parser.args.request_type = RequestType.FORM
    parser._process_request_type()
    assert parser.args.json is False
    assert parser.args.multipart is False
    assert parser.args.form is True

def test_process_request_type_none(parser):
    parser.args.request_type = None
    parser._process_request_type()
    assert parser.args.json is False
    assert parser.args.multipart is False
    assert parser.args.form is False
