# file: thonny/jedi_utils.py:99-120
# asked: {"lines": [99, 102, 103, 104, 105, 106, 107, 109, 110, 111, 112, 113, 114, 115, 116, 120], "branches": [[103, 104], [103, 120], [106, 107], [106, 109]]}
# gained: {"lines": [99, 102, 103, 104, 105, 106, 107, 109, 110, 111, 112, 113, 114, 115, 116, 120], "branches": [[103, 104], [103, 120], [106, 107], [106, 109]]}

import pytest
from unittest.mock import Mock

# Assuming ThonnyCompletion is defined somewhere in thonny/jedi_utils.py
from thonny.jedi_utils import ThonnyCompletion, _tweak_completions

def test_tweak_completions_with_trailing_equals():
    # Mock completion object with trailing '=' in complete but not in name
    completion = Mock()
    completion.name = "arg"
    completion.complete = "arg="
    completion.type = "param"
    completion.description = "argument"
    completion.parent = None
    completion.full_name = "arg"

    completions = [completion]
    result = _tweak_completions(completions)

    assert len(result) == 1
    assert result[0].name == "arg="
    assert result[0].complete == "arg="
    assert result[0].type == "param"
    assert result[0].description == "argument"
    assert result[0].parent is None
    assert result[0].full_name == "arg"

def test_tweak_completions_without_trailing_equals():
    # Mock completion object without trailing '=' in complete
    completion = Mock()
    completion.name = "arg"
    completion.complete = "arg"
    completion.type = "param"
    completion.description = "argument"
    completion.parent = None
    completion.full_name = "arg"

    completions = [completion]
    result = _tweak_completions(completions)

    assert len(result) == 1
    assert result[0].name == "arg"
    assert result[0].complete == "arg"
    assert result[0].type == "param"
    assert result[0].description == "argument"
    assert result[0].parent is None
    assert result[0].full_name == "arg"

def test_tweak_completions_with_name_equals():
    # Mock completion object with trailing '=' in both name and complete
    completion = Mock()
    completion.name = "arg="
    completion.complete = "arg="
    completion.type = "param"
    completion.description = "argument"
    completion.parent = None
    completion.full_name = "arg"

    completions = [completion]
    result = _tweak_completions(completions)

    assert len(result) == 1
    assert result[0].name == "arg="
    assert result[0].complete == "arg="
    assert result[0].type == "param"
    assert result[0].description == "argument"
    assert result[0].parent is None
    assert result[0].full_name == "arg"
