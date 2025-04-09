# file src/blib2to3/pytree.py:528-533
# lines [528, 529, 530, 531, 532, 533]
# branches ['531->532', '531->533']

import pytest
from blib2to3.pytree import BasePattern

class TestBasePattern(BasePattern):
    def __init__(self, type=None, content=None, name=None):
        self.type = type
        self.content = content
        self.name = name

    def __repr__(self):
        args = [repr(self.type), repr(self.content), repr(self.name)]
        while args and args[-1] == repr(None):
            del args[-1]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(args))

@pytest.fixture
def base_pattern_cleanup(mocker):
    # Cleanup code if necessary
    yield
    # No cleanup needed for this test

def test_base_pattern_repr(base_pattern_cleanup):
    # Test with all attributes set
    pattern = TestBasePattern(type='type', content='content', name='name')
    assert repr(pattern) == "TestBasePattern('type', 'content', 'name')"

    # Test with name as None
    pattern = TestBasePattern(type='type', content='content', name=None)
    assert repr(pattern) == "TestBasePattern('type', 'content')"

    # Test with content and name as None
    pattern = TestBasePattern(type='type', content=None, name=None)
    assert repr(pattern) == "TestBasePattern('type')"

    # Test with type, content, and name as None
    pattern = TestBasePattern(type=None, content=None, name=None)
    assert repr(pattern) == "TestBasePattern()"
