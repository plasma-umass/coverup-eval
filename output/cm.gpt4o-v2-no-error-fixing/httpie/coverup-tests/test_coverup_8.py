# file: httpie/cli/argparser.py:117-134
# asked: {"lines": [117, 118, 119, 120, 122, 125, 126, 127, 128, 129, 130, 131, 132, 134], "branches": [[118, 0], [118, 119], [119, 120], [119, 122], [126, 127], [126, 134], [130, 131], [130, 132]]}
# gained: {"lines": [117, 118, 119, 120, 122, 125, 126, 127, 128, 129, 130, 131, 132, 134], "branches": [[118, 119], [119, 120], [119, 122], [126, 127], [126, 134], [130, 131], [130, 132]]}

import pytest
import argparse
import os
from unittest import mock
from httpie.cli.argparser import HTTPieArgumentParser
from httpie.cli.constants import URL_SCHEME_RE

@pytest.fixture
def parser():
    parser = HTTPieArgumentParser()
    parser.args = argparse.Namespace()
    parser.env = argparse.Namespace()
    return parser

def test_process_url_no_scheme_https(parser, monkeypatch):
    parser.args.url = "example.com"
    parser.args.default_scheme = "http"
    parser.env.program_name = "https"

    with mock.patch("os.path.basename", return_value="https"):
        parser._process_url()

    assert parser.args.url == "https://example.com"

def test_process_url_no_scheme_default(parser, monkeypatch):
    parser.args.url = "example.com"
    parser.args.default_scheme = "http"
    parser.env.program_name = "httpie"

    with mock.patch("os.path.basename", return_value="httpie"):
        parser._process_url()

    assert parser.args.url == "http://example.com"

def test_process_url_shorthand_localhost_with_port(parser, monkeypatch):
    parser.args.url = ":3000/foo"
    parser.args.default_scheme = "http"
    parser.env.program_name = "httpie"

    with mock.patch("os.path.basename", return_value="httpie"):
        parser._process_url()

    assert parser.args.url == "http://localhost:3000/foo"

def test_process_url_shorthand_localhost_no_port(parser, monkeypatch):
    parser.args.url = ":/foo"
    parser.args.default_scheme = "http"
    parser.env.program_name = "httpie"

    with mock.patch("os.path.basename", return_value="httpie"):
        parser._process_url()

    assert parser.args.url == "http://localhost/foo"
