# file src/blib2to3/pytree.py:528-533
# lines [528, 529, 530, 531, 532, 533]
# branches ['531->532', '531->533']

import pytest
from blib2to3.pytree import BasePattern
from unittest.mock import patch

class TestBasePattern(BasePattern):
    def __init__(self, type=None, content=None, name=None):
        self.type = type
        self.content = content
        self.name = name

@patch('blib2to3.pytree.type_repr', return_value='type_repr_mock')
def test_basepattern_repr(mock_type_repr):
    # Test case where type is not None and all attributes are set
    pattern = TestBasePattern(type='type', content='content', name='name')
    repr_str = repr(pattern)
    assert repr_str == "TestBasePattern('type_repr_mock', 'content', 'name')"

    # Test case where name is None
    pattern = TestBasePattern(type='type', content='content', name=None)
    repr_str = repr(pattern)
    assert repr_str == "TestBasePattern('type_repr_mock', 'content')"

    # Test case where content and name are None
    pattern = TestBasePattern(type='type', content=None, name=None)
    repr_str = repr(pattern)
    assert repr_str == "TestBasePattern('type_repr_mock')"

    # Test case where type is None (should raise AssertionError)
    pattern = TestBasePattern(type=None, content='content', name='name')
    with pytest.raises(AssertionError):
        repr(pattern)
