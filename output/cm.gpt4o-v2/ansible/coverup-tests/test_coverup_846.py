# file: lib/ansible/playbook/included_file.py:60-61
# asked: {"lines": [60, 61], "branches": []}
# gained: {"lines": [60, 61], "branches": []}

import pytest
from ansible.playbook.included_file import IncludedFile

def test_included_file_repr():
    filename = "test_file.yml"
    args = {"arg1": "value1"}
    vars = {"var1": "value1"}
    task = "test_task"
    hosts = ["host1", "host2"]

    included_file = IncludedFile(filename, args, vars, task)
    included_file._hosts = hosts

    expected_repr = "test_file.yml (args={'arg1': 'value1'} vars={'var1': 'value1'}): ['host1', 'host2']"
    assert repr(included_file) == expected_repr
