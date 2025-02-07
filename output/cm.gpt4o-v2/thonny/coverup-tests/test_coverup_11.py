# file: thonny/jedi_utils.py:99-120
# asked: {"lines": [99, 102, 103, 104, 105, 106, 107, 109, 110, 111, 112, 113, 114, 115, 116, 120], "branches": [[103, 104], [103, 120], [106, 107], [106, 109]]}
# gained: {"lines": [99, 102, 103, 104, 105, 106, 107, 109, 110, 111, 112, 113, 114, 115, 116, 120], "branches": [[103, 104], [103, 120], [106, 107], [106, 109]]}

import pytest
from thonny.jedi_utils import _tweak_completions, ThonnyCompletion

class MockCompletion:
    def __init__(self, name, complete, type, description, parent, full_name):
        self.name = name
        self.complete = complete
        self.type = type
        self.description = description
        self.parent = parent
        self.full_name = full_name

def test_tweak_completions_no_trailing_equals():
    completions = [
        MockCompletion(name="test", complete="test", type="type", description="desc", parent="parent", full_name="full_name")
    ]
    result = _tweak_completions(completions)
    assert len(result) == 1
    assert result[0].name == "test"
    assert result[0].complete == "test"

def test_tweak_completions_with_trailing_equals():
    completions = [
        MockCompletion(name="test", complete="test=", type="type", description="desc", parent="parent", full_name="full_name")
    ]
    result = _tweak_completions(completions)
    assert len(result) == 1
    assert result[0].name == "test="
    assert result[0].complete == "test="

def test_tweak_completions_mixed():
    completions = [
        MockCompletion(name="test1", complete="test1", type="type", description="desc", parent="parent", full_name="full_name"),
        MockCompletion(name="test2", complete="test2=", type="type", description="desc", parent="parent", full_name="full_name")
    ]
    result = _tweak_completions(completions)
    assert len(result) == 2
    assert result[0].name == "test1"
    assert result[0].complete == "test1"
    assert result[1].name == "test2="
    assert result[1].complete == "test2="
