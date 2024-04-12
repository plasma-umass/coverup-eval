# file httpie/context.py:126-128
# lines [126, 127, 128]
# branches []

import pytest
from httpie.context import Environment
from io import StringIO

@pytest.fixture
def mock_environment(mocker):
    env = Environment()
    env.program_name = 'test_program'
    env._orig_stderr = StringIO()
    return env

def test_log_error_with_error_level(mock_environment):
    mock_environment.log_error('Test error message')
    assert '\ntest_program: error: Test error message\n\n' == mock_environment._orig_stderr.getvalue()

def test_log_error_with_warning_level(mock_environment):
    mock_environment.log_error('Test warning message', level='warning')
    assert '\ntest_program: warning: Test warning message\n\n' == mock_environment._orig_stderr.getvalue()

def test_log_error_with_invalid_level(mock_environment):
    with pytest.raises(AssertionError):
        mock_environment.log_error('Test invalid level message', level='invalid')
