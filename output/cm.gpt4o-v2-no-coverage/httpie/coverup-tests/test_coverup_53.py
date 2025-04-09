# file: httpie/context.py:126-128
# asked: {"lines": [126, 127, 128], "branches": []}
# gained: {"lines": [126, 127, 128], "branches": []}

import pytest
from io import StringIO
from httpie.context import Environment

@pytest.fixture
def environment():
    return Environment()

def test_log_error_error_level(environment, monkeypatch):
    stderr = StringIO()
    monkeypatch.setattr(environment, '_orig_stderr', stderr)
    environment.program_name = 'test_program'
    
    environment.log_error('This is an error message', 'error')
    
    assert '\ntest_program: error: This is an error message\n\n' in stderr.getvalue()

def test_log_error_warning_level(environment, monkeypatch):
    stderr = StringIO()
    monkeypatch.setattr(environment, '_orig_stderr', stderr)
    environment.program_name = 'test_program'
    
    environment.log_error('This is a warning message', 'warning')
    
    assert '\ntest_program: warning: This is a warning message\n\n' in stderr.getvalue()

def test_log_error_invalid_level(environment):
    with pytest.raises(AssertionError):
        environment.log_error('This should fail', 'info')
