# file: tornado/options.py:163-165
# asked: {"lines": [163, 164, 165], "branches": []}
# gained: {"lines": [163, 164, 165], "branches": []}

import pytest
from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    return OptionParser()

def test_contains_method(option_parser):
    option_parser.define('test_option', default=42)
    assert 'test_option' in option_parser

    # Clean up
    del option_parser._options[option_parser._normalize_name('test_option')]
