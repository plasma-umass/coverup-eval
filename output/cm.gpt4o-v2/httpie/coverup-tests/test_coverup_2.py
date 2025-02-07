# file: httpie/cli/argparser.py:259-283
# asked: {"lines": [259, 265, 267, 268, 269, 270, 273, 274, 275, 276, 277, 279, 281, 282, 283], "branches": [[267, 268], [267, 281], [268, 269], [268, 273], [274, 275], [274, 279], [275, 274], [275, 276], [281, 0], [281, 282]]}
# gained: {"lines": [259, 265, 267, 268, 269, 270, 273, 274, 275, 276, 277, 281, 282, 283], "branches": [[267, 268], [267, 281], [268, 269], [268, 273], [274, 275], [275, 276], [281, 0], [281, 282]]}

import pytest
from httpie.cli.argparser import HTTPieArgumentParser
import argparse

def test_apply_no_options_valid(monkeypatch):
    parser = HTTPieArgumentParser()
    parser.add_argument('--option', dest='option', default='default_value')
    parser.args = argparse.Namespace(option='non_default_value')
    
    monkeypatch.setattr(parser, 'error', lambda x: None)  # Prevent actual error raising
    
    parser._apply_no_options(['--no-option'])
    
    assert parser.args.option == 'default_value'

def test_apply_no_options_invalid(monkeypatch):
    parser = HTTPieArgumentParser()
    parser.add_argument('--option', dest='option', default='default_value')
    parser.args = argparse.Namespace(option='non_default_value')
    
    errors = []
    monkeypatch.setattr(parser, 'error', lambda x: errors.append(x))  # Capture errors
    
    parser._apply_no_options(['--invalid-option'])
    
    assert errors == ['unrecognized arguments: --invalid-option']

def test_apply_no_options_mixed(monkeypatch):
    parser = HTTPieArgumentParser()
    parser.add_argument('--option', dest='option', default='default_value')
    parser.args = argparse.Namespace(option='non_default_value')
    
    errors = []
    monkeypatch.setattr(parser, 'error', lambda x: errors.append(x))  # Capture errors
    
    parser._apply_no_options(['--no-option', '--invalid-option'])
    
    assert parser.args.option == 'default_value'
    assert errors == ['unrecognized arguments: --invalid-option']
