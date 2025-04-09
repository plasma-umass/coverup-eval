# file: httpie/cli/argparser.py:108-115
# asked: {"lines": [108, 109, 110, 111, 112, 113, 114], "branches": []}
# gained: {"lines": [108, 109, 110, 111, 112, 113, 114], "branches": []}

import pytest
from httpie.cli.argparser import HTTPieArgumentParser, RequestType
import argparse

@pytest.fixture
def parser():
    return HTTPieArgumentParser()

def test_process_request_type_json(parser, monkeypatch):
    class Args:
        request_type = RequestType.JSON

    monkeypatch.setattr(parser, 'args', Args())
    parser._process_request_type()
    assert parser.args.json is True
    assert parser.args.multipart is False
    assert parser.args.form is False

def test_process_request_type_multipart(parser, monkeypatch):
    class Args:
        request_type = RequestType.MULTIPART

    monkeypatch.setattr(parser, 'args', Args())
    parser._process_request_type()
    assert parser.args.json is False
    assert parser.args.multipart is True
    assert parser.args.form is True

def test_process_request_type_form(parser, monkeypatch):
    class Args:
        request_type = RequestType.FORM

    monkeypatch.setattr(parser, 'args', Args())
    parser._process_request_type()
    assert parser.args.json is False
    assert parser.args.multipart is False
    assert parser.args.form is True
