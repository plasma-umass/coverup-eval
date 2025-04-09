# file thonny/jedi_utils.py:99-120
# lines [99, 102, 103, 104, 105, 106, 107, 109, 110, 111, 112, 113, 114, 115, 116, 120]
# branches ['103->104', '103->120', '106->107', '106->109']

import pytest
from unittest.mock import MagicMock

# Assuming ThonnyCompletion is defined somewhere in thonny.jedi_utils
# If not, we need to create a mock or a simple class for it
from thonny.jedi_utils import ThonnyCompletion, _tweak_completions

@pytest.fixture
def completion_mock(mocker):
    completion = mocker.MagicMock()
    completion.name = "arg"
    completion.complete = "arg="
    completion.type = "param"
    completion.description = "argument"
    completion.parent = "parent"
    completion.full_name = "full_name.arg"
    return completion

def test_tweak_completions(completion_mock):
    completions = [completion_mock]
    tweaked_completions = _tweak_completions(completions)
    
    assert len(tweaked_completions) == 1
    tweaked_completion = tweaked_completions[0]
    
    assert tweaked_completion.name == "arg="
    assert tweaked_completion.complete == "arg="
    assert tweaked_completion.type == "param"
    assert tweaked_completion.description == "argument"
    assert tweaked_completion.parent == "parent"
    assert tweaked_completion.full_name == "full_name.arg"
