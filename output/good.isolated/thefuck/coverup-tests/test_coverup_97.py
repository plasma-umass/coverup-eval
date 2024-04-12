# file thefuck/types.py:202-204
# lines [202, 203]
# branches []

import pytest
from thefuck.types import CorrectedCommand

def test_corrected_command_initialization():
    corrected_command = CorrectedCommand(script='ls', side_effect=None, priority=0)
    assert isinstance(corrected_command, CorrectedCommand)
