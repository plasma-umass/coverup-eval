# file: lib/ansible/playbook/included_file.py:39-45
# asked: {"lines": [39, 40, 41, 42, 43, 44, 45], "branches": []}
# gained: {"lines": [39, 40, 41, 42, 43, 44, 45], "branches": []}

import pytest
from ansible.playbook.included_file import IncludedFile

def test_included_file_init():
    filename = "test_file.yml"
    args = {"arg1": "value1"}
    vars = {"var1": "value1"}
    task = "test_task"
    is_role = True

    included_file = IncludedFile(filename, args, vars, task, is_role)

    assert included_file._filename == filename
    assert included_file._args == args
    assert included_file._vars == vars
    assert included_file._task == task
    assert included_file._hosts == []
    assert included_file._is_role == is_role
