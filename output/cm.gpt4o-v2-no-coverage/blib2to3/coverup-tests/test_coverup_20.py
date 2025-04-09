# file: src/blib2to3/pytree.py:528-533
# asked: {"lines": [528, 529, 530, 531, 532, 533], "branches": [[531, 532], [531, 533]]}
# gained: {"lines": [528, 529, 530, 531, 532, 533], "branches": [[531, 532], [531, 533]]}

import pytest
from blib2to3.pytree import BasePattern, type_repr

class MockedBasePattern(BasePattern):
    def __init__(self, type, content=None, name=None):
        self.type = type
        self.content = content
        self.name = name

@pytest.fixture
def setup_base_pattern():
    # Setup a BasePattern instance with mock data
    pattern = MockedBasePattern(type=1, content="content", name="name")
    yield pattern
    # Teardown if necessary (none needed here)

def test_repr_with_all_fields(setup_base_pattern, mocker):
    pattern = setup_base_pattern
    mocker.patch('blib2to3.pytree.type_repr', return_value="MOCKED_TYPE")
    result = repr(pattern)
    assert result == "MockedBasePattern('MOCKED_TYPE', 'content', 'name')"

def test_repr_with_missing_name(setup_base_pattern, mocker):
    pattern = setup_base_pattern
    pattern.name = None
    mocker.patch('blib2to3.pytree.type_repr', return_value="MOCKED_TYPE")
    result = repr(pattern)
    assert result == "MockedBasePattern('MOCKED_TYPE', 'content')"

def test_repr_with_missing_content_and_name(setup_base_pattern, mocker):
    pattern = setup_base_pattern
    pattern.content = None
    pattern.name = None
    mocker.patch('blib2to3.pytree.type_repr', return_value="MOCKED_TYPE")
    result = repr(pattern)
    assert result == "MockedBasePattern('MOCKED_TYPE')"

def test_repr_with_only_type(setup_base_pattern, mocker):
    pattern = setup_base_pattern
    pattern.content = None
    pattern.name = None
    mocker.patch('blib2to3.pytree.type_repr', return_value="MOCKED_TYPE")
    result = repr(pattern)
    assert result == "MockedBasePattern('MOCKED_TYPE')"

def test_repr_with_none_type():
    pattern = MockedBasePattern(type=None)
    with pytest.raises(AssertionError):
        repr(pattern)
