# file: tornado/options.py:663-664
# asked: {"lines": [663, 664], "branches": []}
# gained: {"lines": [663, 664], "branches": []}

import pytest
from tornado.escape import _unicode
from tornado.options import _Option

class TestOption:
    def test_parse_string(self):
        option = _Option(name="test_option", type=str)
        test_value = "test string"
        expected_value = _unicode(test_value)
        
        result = option._parse_string(test_value)
        
        assert result == expected_value
