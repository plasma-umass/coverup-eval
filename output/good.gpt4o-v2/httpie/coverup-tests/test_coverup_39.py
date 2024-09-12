# file: httpie/cli/argparser.py:108-115
# asked: {"lines": [108, 109, 110, 111, 112, 113, 114], "branches": []}
# gained: {"lines": [108, 109, 110, 111, 112, 113, 114], "branches": []}

import pytest
from httpie.cli.argparser import HTTPieArgumentParser
from httpie.cli.constants import RequestType

class MockArgs:
    def __init__(self, request_type):
        self.request_type = request_type
        self.json = None
        self.multipart = None
        self.form = None

@pytest.fixture
def parser():
    return HTTPieArgumentParser()

def test_process_request_type_json(parser):
    parser.args = MockArgs(RequestType.JSON)
    parser._process_request_type()
    assert parser.args.json is True
    assert parser.args.multipart is False
    assert parser.args.form is False

def test_process_request_type_multipart(parser):
    parser.args = MockArgs(RequestType.MULTIPART)
    parser._process_request_type()
    assert parser.args.json is False
    assert parser.args.multipart is True
    assert parser.args.form is True

def test_process_request_type_form(parser):
    parser.args = MockArgs(RequestType.FORM)
    parser._process_request_type()
    assert parser.args.json is False
    assert parser.args.multipart is False
    assert parser.args.form is True
