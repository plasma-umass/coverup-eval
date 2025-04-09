# file: httpie/core.py:221-231
# asked: {"lines": [222, 223, 224, 225, 226, 227, 229, 230, 231], "branches": []}
# gained: {"lines": [222, 223, 224, 225, 226, 227, 229, 230, 231], "branches": []}

import pytest
from io import StringIO
from httpie.context import Environment
from httpie.core import print_debug_info

@pytest.fixture
def mock_env():
    class MockStderr:
        def __init__(self):
            self.output = StringIO()

        def writelines(self, lines):
            for line in lines:
                self.output.write(line)

        def write(self, message):
            self.output.write(message)

        def get_output(self):
            return self.output.getvalue()

    env = Environment()
    env.stderr = MockStderr()
    return env

def test_print_debug_info(mock_env):
    print_debug_info(mock_env)
    output = mock_env.stderr.get_output()
    
    assert 'HTTPie' in output
    assert 'Requests' in output
    assert 'Pygments' in output
    assert 'Python' in output
    assert repr(mock_env) in output
