# file: tornado/util.py:160-167
# asked: {"lines": [160, 161, 163, 166, 167], "branches": [[163, 166], [163, 167]]}
# gained: {"lines": [160, 161, 163, 166, 167], "branches": [[163, 166], [163, 167]]}

import pytest

from tornado.util import exec_in

def test_exec_in_with_string_code():
    code = "a = 1"
    glob = {}
    exec_in(code, glob)
    assert glob["a"] == 1

def test_exec_in_with_compiled_code():
    code = compile("a = 1", "<string>", "exec", dont_inherit=True)
    glob = {}
    exec_in(code, glob)
    assert glob["a"] == 1

def test_exec_in_with_locals():
    code = "a = 1"
    glob = {}
    loc = {}
    exec_in(code, glob, loc)
    assert "a" not in glob
    assert loc["a"] == 1

def test_exec_in_with_non_string_code():
    class CustomCode:
        def __init__(self):
            self.code = compile("a = 1", "<string>", "exec", dont_inherit=True)
    
    code = CustomCode().code
    glob = {}
    exec_in(code, glob)
    assert glob["a"] == 1
