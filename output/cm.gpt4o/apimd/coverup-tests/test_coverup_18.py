# file apimd/parser.py:36-43
# lines [36, 38, 39, 40, 41, 42, 43]
# branches ['39->40', '39->43', '41->39', '41->42']

import pytest
from unittest.mock import Mock

# Assuming the function _attr is imported from apimd.parser
from apimd.parser import _attr

class TestAttrFunction:
    def test_attr_function(self):
        # Create a mock object with nested attributes
        mock_obj = Mock()
        mock_obj.a = Mock()
        mock_obj.a.b = Mock()
        mock_obj.a.b.c = 'value'

        # Test nested attribute access
        assert _attr(mock_obj, 'a.b.c') == 'value'

        # Test non-existent attribute access
        mock_obj.a.b.configure_mock(d=None)
        assert _attr(mock_obj, 'a.b.d') is None

        # Test attribute access with None in the middle
        mock_obj.a.b = None
        assert _attr(mock_obj, 'a.b.c') is None

        # Test top-level non-existent attribute
        mock_obj.configure_mock(x=None)
        assert _attr(mock_obj, 'x.y.z') is None
