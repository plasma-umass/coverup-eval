# file: tornado/options.py:145-146
# asked: {"lines": [145, 146], "branches": []}
# gained: {"lines": [145, 146], "branches": []}

import pytest
from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    return OptionParser()

def test_normalize_name_with_underscore(option_parser):
    result = option_parser._normalize_name("test_name")
    assert result == "test-name"

def test_normalize_name_without_underscore(option_parser):
    result = option_parser._normalize_name("testname")
    assert result == "testname"
