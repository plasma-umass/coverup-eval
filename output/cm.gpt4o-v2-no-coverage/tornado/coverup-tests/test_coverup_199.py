# file: tornado/options.py:163-165
# asked: {"lines": [164, 165], "branches": []}
# gained: {"lines": [164, 165], "branches": []}

import pytest
from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    parser = OptionParser()
    parser.__dict__['_options'] = {'test-option': True}
    return parser

def test_contains_with_normalized_name(option_parser):
    assert 'test_option' in option_parser

def test_contains_with_non_normalized_name(option_parser):
    assert 'test-option' in option_parser

def test_contains_with_missing_option(option_parser):
    assert 'missing_option' not in option_parser
