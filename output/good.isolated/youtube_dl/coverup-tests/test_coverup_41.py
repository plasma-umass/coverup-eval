# file youtube_dl/jsinterp.py:38-57
# lines [39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 54, 56, 57]
# branches ['39->40', '39->42', '45->46', '45->48', '49->50', '49->54']

import pytest
from youtube_dl.jsinterp import JSInterpreter
from youtube_dl.utils import ExtractorError

@pytest.fixture
def js_interpreter():
    return JSInterpreter('')

def test_interpret_statement_var(js_interpreter):
    local_vars = {}
    stmt = "var a = 1"
    result, should_abort = js_interpreter.interpret_statement(stmt, local_vars)
    assert result == 1
    assert should_abort == False

def test_interpret_statement_return(js_interpreter):
    local_vars = {}
    stmt = "return 2"
    result, should_abort = js_interpreter.interpret_statement(stmt, local_vars)
    assert result == 2
    assert should_abort == True

def test_interpret_statement_expression(js_interpreter):
    local_vars = {}
    stmt = "3"
    result, should_abort = js_interpreter.interpret_statement(stmt, local_vars)
    assert result == 3
    assert should_abort == False

def test_interpret_statement_recursion_limit(js_interpreter):
    local_vars = {}
    stmt = "var a = 1"
    with pytest.raises(ExtractorError, match='Recursion limit reached'):
        js_interpreter.interpret_statement(stmt, local_vars, allow_recursion=-1)
