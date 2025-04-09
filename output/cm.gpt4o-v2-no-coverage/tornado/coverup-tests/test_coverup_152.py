# file: tornado/options.py:663-664
# asked: {"lines": [663, 664], "branches": []}
# gained: {"lines": [663, 664], "branches": []}

import pytest
from tornado.options import _Option
from tornado.escape import to_unicode

class TestOption:
    def test_parse_string(self):
        option = _Option(name="test_option", type=str)
        input_value = "test"
        expected_output = to_unicode(input_value)
        
        assert option._parse_string(input_value) == expected_output

    def test_parse_string_non_ascii(self):
        option = _Option(name="test_option", type=str)
        input_value = "tést"
        expected_output = to_unicode(input_value)
        
        assert option._parse_string(input_value) == expected_output
