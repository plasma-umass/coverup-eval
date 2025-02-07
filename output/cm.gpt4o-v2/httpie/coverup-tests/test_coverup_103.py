# file: httpie/cli/argparser.py:259-283
# asked: {"lines": [279], "branches": [[274, 279], [275, 274]]}
# gained: {"lines": [279], "branches": [[274, 279], [275, 274]]}

import pytest
from httpie.cli.argparser import HTTPieArgumentParser
import argparse

def test_apply_no_options_valid(monkeypatch):
    parser = HTTPieArgumentParser()
    parser.add_argument('--option', dest='option', default='default_value')
    parser.args = argparse.Namespace(option='non_default_value')

    monkeypatch.setattr(parser, 'error', lambda msg: None)

    parser._apply_no_options(['--no-option'])

    assert parser.args.option == 'default_value'

def test_apply_no_options_invalid(monkeypatch):
    parser = HTTPieArgumentParser()
    parser.add_argument('--option', dest='option', default='default_value')
    parser.args = argparse.Namespace(option='non_default_value')

    error_called = []

    def mock_error(msg):
        error_called.append(msg)

    monkeypatch.setattr(parser, 'error', mock_error)

    parser._apply_no_options(['--invalid-option'])

    assert error_called
    assert 'unrecognized arguments: --invalid-option' in error_called[0]

def test_apply_no_options_mixed(monkeypatch):
    parser = HTTPieArgumentParser()
    parser.add_argument('--option', dest='option', default='default_value')
    parser.add_argument('--another-option', dest='another_option', default='another_default_value')
    parser.args = argparse.Namespace(option='non_default_value', another_option='another_non_default_value')

    error_called = []

    def mock_error(msg):
        error_called.append(msg)

    monkeypatch.setattr(parser, 'error', mock_error)

    parser._apply_no_options(['--no-option', '--no-invalid-option'])

    assert parser.args.option == 'default_value'
    assert parser.args.another_option == 'another_non_default_value'
    assert error_called
    assert 'unrecognized arguments: --no-invalid-option' in error_called[0]
