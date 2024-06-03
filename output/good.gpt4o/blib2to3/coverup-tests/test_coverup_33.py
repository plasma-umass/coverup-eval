# file src/blib2to3/pgen2/tokenize.py:216-218
# lines [216, 217, 218]
# branches ['217->exit', '217->218']

import pytest
from blib2to3.pgen2.tokenize import tokenize_loop, generate_tokens
from io import StringIO

def test_tokenize_loop(mocker):
    # Mock the tokeneater function to verify it gets called with the correct arguments
    tokeneater_mock = mocker.Mock()

    # Create a simple input string to tokenize
    input_string = "print('Hello, world!')\n"
    readline = StringIO(input_string).readline

    # Call the tokenize_loop function
    tokenize_loop(readline, tokeneater_mock)

    # Verify that tokeneater was called with the expected tokens
    expected_tokens = list(generate_tokens(StringIO(input_string).readline))
    for call, expected in zip(tokeneater_mock.call_args_list, expected_tokens):
        assert call[0] == expected

    # Clean up: no additional cleanup needed as we used mocker and StringIO
