# file src/blib2to3/pgen2/tokenize.py:216-218
# lines [216, 217, 218]
# branches ['217->exit', '217->218']

import pytest
from blib2to3.pgen2.tokenize import tokenize_loop, generate_tokens
from io import StringIO

# Mock tokeneater function to capture the tokens
def mock_tokeneater(type, token, start, end, line):
    mock_tokeneater.calls.append((type, token, start, end, line))

mock_tokeneater.calls = []

@pytest.fixture
def mock_readline():
    # Create a mock readline function
    lines = iter(["print('Hello, world!')\n", ""])
    def _mock_readline():
        return next(lines)
    return _mock_readline

def test_tokenize_loop_executes_missing_lines(mock_readline):
    # Use the mock readline and tokeneater to test tokenize_loop
    tokenize_loop(mock_readline, mock_tokeneater)

    # Check if the mock tokeneater was called with the expected tokens
    assert len(mock_tokeneater.calls) > 0
    assert any(token == 'print' for _, token, _, _, _ in mock_tokeneater.calls)
    assert any(token == '(' for _, token, _, _, _ in mock_tokeneater.calls)
    assert any(token == "'Hello, world!'" for _, token, _, _, _ in mock_tokeneater.calls)
    assert any(token == ')' for _, token, _, _, _ in mock_tokeneater.calls)

    # Clean up after the test
    mock_tokeneater.calls = []
