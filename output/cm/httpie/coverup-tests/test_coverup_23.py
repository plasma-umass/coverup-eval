# file httpie/core.py:221-231
# lines [221, 222, 223, 224, 225, 226, 227, 229, 230, 231]
# branches []

import pytest
import platform
from httpie.core import Environment, print_debug_info
from unittest.mock import MagicMock

@pytest.fixture
def mock_environment():
    env = Environment()
    env.stderr = MagicMock()
    return env

def test_print_debug_info(mock_environment):
    print_debug_info(mock_environment)

    assert mock_environment.stderr.writelines.called
    assert mock_environment.stderr.write.called

    calls = mock_environment.stderr.writelines.call_args[0][0]
    assert any('HTTPie' in call for call in calls)
    assert any('Requests' in call for call in calls)
    assert any('Pygments' in call for call in calls)
    assert any('Python' in call for call in calls)
    assert any(call for call in calls if call.startswith(platform.system()))

    repr_call = mock_environment.stderr.write.call_args_list[-2][0][0]
    assert repr_call == repr(mock_environment)
