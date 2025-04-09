# file: httpie/core.py:221-231
# asked: {"lines": [222, 223, 224, 225, 226, 227, 229, 230, 231], "branches": []}
# gained: {"lines": [222, 223, 224, 225, 226, 227, 229, 230, 231], "branches": []}

import pytest
from io import StringIO
from httpie.core import print_debug_info
from httpie.context import Environment

def test_print_debug_info(monkeypatch):
    # Create a mock environment
    mock_stderr = StringIO()
    env = Environment(stderr=mock_stderr)

    # Mock versions and platform information
    monkeypatch.setattr('httpie.core.httpie_version', '1.0.0')
    monkeypatch.setattr('httpie.core.requests_version', '2.25.1')
    monkeypatch.setattr('httpie.core.pygments_version', '2.7.4')
    monkeypatch.setattr('sys.version', '3.8.5 (default, Jul 20 2020, 12:11:08) \n[GCC 9.3.0]')
    monkeypatch.setattr('sys.executable', '/usr/bin/python3')
    monkeypatch.setattr('platform.system', lambda: 'Linux')
    monkeypatch.setattr('platform.release', lambda: '5.4.0-42-generic')

    # Call the function
    print_debug_info(env)

    # Verify the output
    output = mock_stderr.getvalue()
    assert 'HTTPie 1.0.0\n' in output
    assert 'Requests 2.25.1\n' in output
    assert 'Pygments 2.7.4\n' in output
    assert 'Python 3.8.5 (default, Jul 20 2020, 12:11:08) \n[GCC 9.3.0]\n' in output
    assert '/usr/bin/python3\n' in output
    assert 'Linux 5.4.0-42-generic' in output
    assert '\n\n' in output
    assert repr(env) in output
    assert output.endswith('\n')
