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
    included_file = IncludedFile(filename, args, vars, task)

    # Verify the __repr__ output
    expected_repr = "test_file.yml (args={'arg1': 'value1'} vars={'var1': 'value1'}): []"
    assert repr(included_file) == expected_repr
