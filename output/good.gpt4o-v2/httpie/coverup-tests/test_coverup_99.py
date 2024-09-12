# file: httpie/cli/argparser.py:117-134
# asked: {"lines": [], "branches": [[118, 0]]}
# gained: {"lines": [], "branches": [[118, 0]]}

import pytest
import argparse
import os
import re
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

    monkeypatch.setattr(os.path, "basename", lambda x: "https")
    parser._process_url()
    assert parser.args.url == "https://example.com"

def test_process_url_no_scheme_default(parser, monkeypatch):
    parser.args.url = "example.com"
    parser.args.default_scheme = "http"
    parser.env.program_name = "httpie"

    monkeypatch.setattr(os.path, "basename", lambda x: "httpie")
    parser._process_url()
    assert parser.args.url == "http://example.com"

def test_process_url_shorthand_localhost_with_port(parser, monkeypatch):
    parser.args.url = ":3000/foo"
    parser.args.default_scheme = "http"
    parser.env.program_name = "httpie"

    monkeypatch.setattr(os.path, "basename", lambda x: "httpie")
    parser._process_url()
    assert parser.args.url == "http://localhost:3000/foo"

def test_process_url_shorthand_localhost_no_port(parser, monkeypatch):
    parser.args.url = ":/foo"
    parser.args.default_scheme = "http"
    parser.env.program_name = "httpie"

    monkeypatch.setattr(os.path, "basename", lambda x: "httpie")
    parser._process_url()
    assert parser.args.url == "http://localhost/foo"

def test_process_url_with_scheme(parser):
    parser.args.url = "http://example.com"
    parser._process_url()
    assert parser.args.url == "http://example.com"
