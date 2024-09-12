# file: lib/ansible/modules/pip.py:485-491
# asked: {"lines": [486, 487, 488, 489, 490, 491], "branches": [[487, 488], [487, 489], [489, 490], [489, 491]]}
# gained: {"lines": [486, 487, 488, 489, 490, 491], "branches": [[487, 488], [487, 489], [489, 490], [489, 491]]}

import pytest
from unittest.mock import Mock
from ansible.modules.pip import _fail

def test_fail_with_stdout_and_stderr():
    module = Mock()
    cmd = "test command"
    out = "test output"
    err = "test error"

    _fail(module, cmd, out, err)

    module.fail_json.assert_called_once_with(cmd=cmd, msg="stdout: test output\n:stderr: test error")

def test_fail_with_only_stdout():
    module = Mock()
    cmd = "test command"
    out = "test output"
    err = ""

    _fail(module, cmd, out, err)

    module.fail_json.assert_called_once_with(cmd=cmd, msg="stdout: test output")

def test_fail_with_only_stderr():
    module = Mock()
    cmd = "test command"
    out = ""
    err = "test error"

    _fail(module, cmd, out, err)

    module.fail_json.assert_called_once_with(cmd=cmd, msg="\n:stderr: test error")

def test_fail_with_no_output():
    module = Mock()
    cmd = "test command"
    out = ""
    err = ""

    _fail(module, cmd, out, err)

    module.fail_json.assert_called_once_with(cmd=cmd, msg="")
