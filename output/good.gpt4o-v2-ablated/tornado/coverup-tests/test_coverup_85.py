# file: tornado/options.py:145-146
# asked: {"lines": [145, 146], "branches": []}
# gained: {"lines": [145, 146], "branches": []}

import pytest
from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    return OptionParser()

def test_normalize_name_with_underscore(option_parser):
    normalized_name = option_parser._normalize_name("test_name")
    assert normalized_name == "test-name"

def test_normalize_name_without_underscore(option_parser):
    normalized_name = option_parser._normalize_name("testname")
    assert normalized_name == "testname"

def test_normalize_name_with_multiple_underscores(option_parser):
    normalized_name = option_parser._normalize_name("test_name_with_underscores")
    assert normalized_name == "test-name-with-underscores"
