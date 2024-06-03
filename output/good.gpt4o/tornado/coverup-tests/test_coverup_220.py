# file tornado/util.py:160-167
# lines [163, 166, 167]
# branches ['163->166', '163->167']

import pytest
from tornado.util import exec_in

def test_exec_in_string_code():
    code_str = "a = 1 + 1"
    glob = {}
    exec_in(code_str, glob)
    assert glob['a'] == 2

def test_exec_in_code_object():
    code_obj = compile("b = 2 + 2", "<string>", "exec")
    glob = {}
    exec_in(code_obj, glob)
    assert glob['b'] == 4
