# file tornado/util.py:160-167
# lines [160, 161, 163, 166, 167]
# branches ['163->166', '163->167']

import pytest
from tornado.util import exec_in

def test_exec_in_executes_string_code():
    # Define the globals dictionary
    mock_globals = {}

    # Define the code to be executed
    code_string = "result = 42"

    # Execute the code string
    exec_in(code_string, mock_globals)

    # Assert that the code was executed and the result is in mock_globals
    assert 'result' in mock_globals
    assert mock_globals['result'] == 42

def test_exec_in_executes_code_object():
    # Define the globals dictionary
    mock_globals = {}

    # Define the code to be executed as a code object
    code_object = compile("result = 42", "<string>", "exec")

    # Execute the code object
    exec_in(code_object, mock_globals)

    # Assert that the code was executed and the result is in mock_globals
    assert 'result' in mock_globals
    assert mock_globals['result'] == 42

def test_exec_in_executes_with_locals():
    # Define the globals dictionary
    mock_globals = {}

    # Define the locals dictionary
    mock_locals = {}

    # Define the code to be executed
    code_string = "result = 42"

    # Execute the code string with locals
    exec_in(code_string, mock_globals, mock_locals)

    # Assert that the code was executed and the result is in mock_locals
    assert 'result' in mock_locals
    assert mock_locals['result'] == 42
