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
    code = compile("a = 2", "<string>", "exec")
    glob = {}
    exec_in(code, glob)
    assert glob["a"] == 2

def test_exec_in_with_locals():
    code = "a = 3"
    glob = {}
    loc = {}
    exec_in(code, glob, loc)
    assert loc["a"] == 3

def test_exec_in_with_non_string_code():
    code = compile("a = 4", "<string>", "exec")
    glob = {}
    exec_in(code, glob)
    assert glob["a"] == 4
