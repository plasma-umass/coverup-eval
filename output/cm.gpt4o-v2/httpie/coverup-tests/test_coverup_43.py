# file: httpie/core.py:221-231
# asked: {"lines": [221, 222, 223, 224, 225, 226, 227, 229, 230, 231], "branches": []}
# gained: {"lines": [221, 222, 223, 224, 225, 226, 227, 229, 230, 231], "branches": []}

import pytest
import platform
import sys
from io import StringIO
from httpie.context import Environment
from httpie.core import print_debug_info
from httpie import __version__ as httpie_version
from requests import __version__ as requests_version
from pygments import __version__ as pygments_version

def test_print_debug_info(monkeypatch):
    # Create a mock environment with a StringIO object to capture stderr
    mock_stderr = StringIO()
    env = Environment(stderr=mock_stderr)

    # Call the function
    print_debug_info(env)

    # Get the output
    output = mock_stderr.getvalue()

    # Assertions to verify the output contains expected debug information
    assert f'HTTPie {httpie_version}\n' in output
    assert f'Requests {requests_version}\n' in output
    assert f'Pygments {pygments_version}\n' in output
    assert f'Python {sys.version}\n{sys.executable}\n' in output
    assert f'{platform.system()} {platform.release()}' in output
    assert repr(env) in output

    # Clean up
    mock_stderr.close()
