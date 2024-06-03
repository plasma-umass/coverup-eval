# file httpie/cli/argparser.py:108-115
# lines [109, 110, 111, 112, 113, 114]
# branches []

import pytest
from unittest import mock
import argparse
from httpie.cli.argparser import HTTPieArgumentParser, RequestType

def test_process_request_type(mocker):
    parser = HTTPieArgumentParser()
    args = argparse.Namespace()
    
    # Mock the args to cover all branches
    args.request_type = RequestType.JSON
    parser.args = args
    parser._process_request_type()
    assert parser.args.json is True
    assert parser.args.multipart is False
    assert parser.args.form is False

    args.request_type = RequestType.MULTIPART
    parser.args = args
    parser._process_request_type()
    assert parser.args.json is False
    assert parser.args.multipart is True
    assert parser.args.form is True

    args.request_type = RequestType.FORM
    parser.args = args
    parser._process_request_type()
    assert parser.args.json is False
    assert parser.args.multipart is False
    assert parser.args.form is True

    args.request_type = None
    parser.args = args
    parser._process_request_type()
    assert parser.args.json is False
    assert parser.args.multipart is False
    assert parser.args.form is False
