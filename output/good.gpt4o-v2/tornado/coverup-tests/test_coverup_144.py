# file: tornado/options.py:145-146
# asked: {"lines": [145, 146], "branches": []}
# gained: {"lines": [145, 146], "branches": []}

import pytest
from tornado.options import OptionParser

def test_normalize_name():
    parser = OptionParser()
    assert parser._normalize_name("test_name") == "test-name"
    assert parser._normalize_name("another_test_name") == "another-test-name"
    assert parser._normalize_name("no_underscores") == "no-underscores"
    assert parser._normalize_name("already-normalized") == "already-normalized"
