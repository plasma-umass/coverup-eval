# file thonny/jedi_utils.py:99-120
# lines []
# branches ['106->109']

import pytest

# Assuming ThonnyCompletion is defined somewhere in thonny.jedi_utils
from thonny.jedi_utils import ThonnyCompletion, _tweak_completions

class MockCompletion:
    def __init__(self, name, complete, type, description, parent, full_name):
        self.name = name
        self.complete = complete
        self.type = type
        self.description = description
        self.parent = parent
        self.full_name = full_name

@pytest.fixture
def mock_completion():
    return MockCompletion(
        name="arg",
        complete="arg",
        type="param",
        description="argument",
        parent=None,
        full_name="func.arg"
    )

def test_tweak_completions_without_equal_sign(mock_completion):
    completions = [mock_completion]
    tweaked_completions = _tweak_completions(completions)
    assert len(tweaked_completions) == 1
    assert tweaked_completions[0].name == "arg"
    assert tweaked_completions[0].complete == "arg"
    assert tweaked_completions[0].type == "param"
    assert tweaked_completions[0].description == "argument"
    assert tweaked_completions[0].parent is None
    assert tweaked_completions[0].full_name == "func.arg"
