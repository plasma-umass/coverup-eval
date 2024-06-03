# file thefuck/rules/scm_correction.py:22-27
# lines [24, 25, 27]
# branches []

import pytest
from thefuck.rules.scm_correction import match
from thefuck.rules.scm_correction import wrong_scm_patterns

class Command:
    def __init__(self, script_parts, output):
        self.script_parts = script_parts
        self.output = output

@pytest.fixture
def mock_get_actual_scm(mocker):
    return mocker.patch('thefuck.rules.scm_correction._get_actual_scm', return_value=True)

def test_match_scm_correction(mock_get_actual_scm):
    for scm, pattern in wrong_scm_patterns.items():
        command = Command([scm], pattern)
        assert match(command)

    # Test with a command that should not match
    command = Command(['git'], 'some other error')
    assert not match(command)
