# file: src/blib2to3/pytree.py:528-533
# asked: {"lines": [529, 530, 531, 532, 533], "branches": [[531, 532], [531, 533]]}
# gained: {"lines": [529, 530, 531, 532, 533], "branches": [[531, 532], [531, 533]]}

import pytest
from blib2to3.pytree import BasePattern

class MockType:
    def __repr__(self):
        return "MockType"

class MockBasePattern(BasePattern):
    def __init__(self, type, content=None, name=None):
        self.type = type
        self.content = content
        self.name = name

def mock_type_repr(type_num):
    return "MockType"

@pytest.fixture
def monkeypatch_type_repr(monkeypatch):
    monkeypatch.setattr("blib2to3.pytree.type_repr", mock_type_repr)

def test_basepattern_repr_with_all_attributes(monkeypatch_type_repr):
    pattern = MockBasePattern("MockType", "content", "name")
    result = repr(pattern)
    assert result == "MockBasePattern('MockType', 'content', 'name')"

def test_basepattern_repr_with_missing_name(monkeypatch_type_repr):
    pattern = MockBasePattern("MockType", "content")
    result = repr(pattern)
    assert result == "MockBasePattern('MockType', 'content')"

def test_basepattern_repr_with_missing_content_and_name(monkeypatch_type_repr):
    pattern = MockBasePattern("MockType")
    result = repr(pattern)
    assert result == "MockBasePattern('MockType')"
