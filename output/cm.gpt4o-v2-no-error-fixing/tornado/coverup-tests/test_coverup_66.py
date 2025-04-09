# file: tornado/util.py:160-167
# asked: {"lines": [160, 161, 163, 166, 167], "branches": [[163, 166], [163, 167]]}
# gained: {"lines": [160, 161, 163, 166, 167], "branches": [[163, 166], [163, 167]]}

import pytest
from tornado.util import exec_in

def test_exec_in_with_string_code():
    code = "a = 1"
    glob = {}
    loc = {}
    exec_in(code, glob, loc)
    assert loc['a'] == 1

def test_exec_in_with_compiled_code():
    code = compile("a = 1", "<string>", "exec")
    glob = {}
    loc = {}
    exec_in(code, glob, loc)
    assert loc['a'] == 1

def test_exec_in_with_none_loc():
    code = "a = 1"
    glob = {}
    exec_in(code, glob)
    assert glob['a'] == 1
