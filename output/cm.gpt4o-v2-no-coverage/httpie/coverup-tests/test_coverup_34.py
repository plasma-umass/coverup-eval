# file: httpie/cli/argparser.py:108-115
# asked: {"lines": [108, 109, 110, 111, 112, 113, 114], "branches": []}
# gained: {"lines": [108, 109, 110, 111, 112, 113, 114], "branches": []}

import pytest
from httpie.cli.argparser import HTTPieArgumentParser
from httpie.cli.constants import RequestType
import argparse

class MockArgs:
    def __init__(self, request_type):
        self.request_type = request_type
        self.json = None
        self.multipart = None
        self.form = None

@pytest.fixture
def parser():
    return HTTPieArgumentParser()

@pytest.mark.parametrize("request_type, expected_json, expected_multipart, expected_form", [
    (RequestType.JSON, True, False, False),
    (RequestType.MULTIPART, False, True, True),
    (RequestType.FORM, False, False, True),
])
def test_process_request_type(parser, request_type, expected_json, expected_multipart, expected_form):
    parser.args = MockArgs(request_type)
    parser._process_request_type()
    assert parser.args.json == expected_json
    assert parser.args.multipart == expected_multipart
    assert parser.args.form == expected_form
