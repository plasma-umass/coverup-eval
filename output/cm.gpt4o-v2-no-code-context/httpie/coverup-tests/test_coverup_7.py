# file: httpie/cli/argparser.py:117-134
# asked: {"lines": [117, 118, 119, 120, 122, 125, 126, 127, 128, 129, 130, 131, 132, 134], "branches": [[118, 0], [118, 119], [119, 120], [119, 122], [126, 127], [126, 134], [130, 131], [130, 132]]}
# gained: {"lines": [117, 118, 119, 120, 122, 125, 126, 127, 128, 129, 130, 131, 132, 134], "branches": [[118, 0], [118, 119], [119, 120], [119, 122], [126, 127], [126, 134], [130, 131], [130, 132]]}

import pytest
import os
import re
from unittest import mock
from httpie.cli.argparser import HTTPieArgumentParser

URL_SCHEME_RE = re.compile(r'^[a-z][a-z0-9+\-.]*://', re.IGNORECASE)

class MockArgs:
    def __init__(self, url, default_scheme='http'):
        self.url = url
        self.default_scheme = default_scheme

class MockEnv:
    def __init__(self, program_name):
        self.program_name = program_name

@pytest.fixture
def parser():
    return HTTPieArgumentParser()

def test_process_url_no_scheme_http(parser, monkeypatch):
    args = MockArgs(url='example.com')
    env = MockEnv(program_name='http')
    monkeypatch.setattr(parser, 'args', args)
    monkeypatch.setattr(parser, 'env', env)
    
    parser._process_url()
    
    assert parser.args.url == 'http://example.com'

def test_process_url_no_scheme_https(parser, monkeypatch):
    args = MockArgs(url='example.com')
    env = MockEnv(program_name='https')
    monkeypatch.setattr(parser, 'args', args)
    monkeypatch.setattr(parser, 'env', env)
    
    parser._process_url()
    
    assert parser.args.url == 'https://example.com'

def test_process_url_shorthand_localhost_with_port(parser, monkeypatch):
    args = MockArgs(url=':3000/foo')
    env = MockEnv(program_name='http')
    monkeypatch.setattr(parser, 'args', args)
    monkeypatch.setattr(parser, 'env', env)
    
    parser._process_url()
    
    assert parser.args.url == 'http://localhost:3000/foo'

def test_process_url_shorthand_localhost_without_port(parser, monkeypatch):
    args = MockArgs(url=':/foo')
    env = MockEnv(program_name='http')
    monkeypatch.setattr(parser, 'args', args)
    monkeypatch.setattr(parser, 'env', env)
    
    parser._process_url()
    
    assert parser.args.url == 'http://localhost/foo'

def test_process_url_with_scheme(parser, monkeypatch):
    args = MockArgs(url='http://example.com')
    env = MockEnv(program_name='http')
    monkeypatch.setattr(parser, 'args', args)
    monkeypatch.setattr(parser, 'env', env)
    
    parser._process_url()
    
    assert parser.args.url == 'http://example.com'
