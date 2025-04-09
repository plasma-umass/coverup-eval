# file tornado/options.py:663-664
# lines [663, 664]
# branches []

import pytest
from unittest import mock
from tornado.options import _Option

def test__parse_string():
    with mock.patch.object(_Option, '__init__', lambda self, name: None):
        option = _Option("test_option")
        test_value = "test_string"
        
        with mock.patch('tornado.options._unicode', return_value=test_value) as mock_unicode:
            result = option._parse_string(test_value)
            mock_unicode.assert_called_once_with(test_value)
            assert result == test_value
