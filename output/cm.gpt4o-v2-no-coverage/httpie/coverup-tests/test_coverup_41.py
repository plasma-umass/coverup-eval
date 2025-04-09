# file: httpie/cli/argparser.py:61-66
# asked: {"lines": [61, 62, 63, 64, 65, 66], "branches": []}
# gained: {"lines": [61, 62, 63, 64, 65, 66], "branches": []}

import pytest
import argparse
from httpie.cli.argparser import HTTPieArgumentParser, HTTPieHelpFormatter

def test_httpie_argument_parser_init(monkeypatch):
    # Mocking the super class __init__ to ensure it is called with correct parameters
    def mock_super_init(self, *args, **kwargs):
        self.called_with = (args, kwargs)
    
    monkeypatch.setattr(argparse.ArgumentParser, '__init__', mock_super_init)
    
    parser = HTTPieArgumentParser()
    
    # Assertions to verify the correct behavior
    assert parser.called_with[1]['formatter_class'] == HTTPieHelpFormatter
    assert parser.called_with[1]['add_help'] is False
    assert parser.env is None
    assert parser.args is None
    assert parser.has_stdin_data is False
