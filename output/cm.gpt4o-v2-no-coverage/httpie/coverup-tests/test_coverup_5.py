# file: httpie/cli/argparser.py:117-134
# asked: {"lines": [117, 118, 119, 120, 122, 125, 126, 127, 128, 129, 130, 131, 132, 134], "branches": [[118, 0], [118, 119], [119, 120], [119, 122], [126, 127], [126, 134], [130, 131], [130, 132]]}
# gained: {"lines": [117, 118, 119, 120, 122, 125, 126, 127, 128, 129, 130, 131, 132, 134], "branches": [[118, 0], [118, 119], [119, 120], [119, 122], [126, 127], [126, 134], [130, 131], [130, 132]]}

import pytest
import argparse
import os
import re
from unittest.mock import Mock, patch
from httpie.cli.argparser import HTTPieArgumentParser
from httpie.cli.constants import URL_SCHEME_RE

@pytest.fixture
def parser():
    parser = HTTPieArgumentParser()
    parser.args = Mock()
    parser.env = Mock()
    return parser

def test_process_url_with_https_program_name(parser):
    parser.args.url = "example.com"
    parser.args.default_scheme = "http"
    parser.env.program_name = "https"
    
    parser._process_url()
    
    assert parser.args.url == "https://example.com"

def test_process_url_with_default_scheme(parser):
    parser.args.url = "example.com"
    parser.args.default_scheme = "http"
    parser.env.program_name = "httpie"
    
    parser._process_url()
    
    assert parser.args.url == "http://example.com"

def test_process_url_with_shorthand_localhost(parser):
    parser.args.url = ":3000/foo"
    parser.args.default_scheme = "http"
    parser.env.program_name = "httpie"
    
    parser._process_url()
    
    assert parser.args.url == "http://localhost:3000/foo"

def test_process_url_with_shorthand_localhost_no_port(parser):
    parser.args.url = ":/foo"
    parser.args.default_scheme = "http"
    parser.env.program_name = "httpie"
    
    parser._process_url()
    
    assert parser.args.url == "http://localhost/foo"

def test_process_url_with_full_url(parser):
    parser.args.url = "http://example.com"
    parser.args.default_scheme = "http"
    parser.env.program_name = "httpie"
    
    parser._process_url()
    
    assert parser.args.url == "http://example.com"
