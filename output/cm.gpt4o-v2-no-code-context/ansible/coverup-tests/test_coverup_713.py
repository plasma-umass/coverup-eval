# file: lib/ansible/playbook/included_file.py:60-61
# asked: {"lines": [60, 61], "branches": []}
# gained: {"lines": [60], "branches": []}

import pytest
from ansible.playbook.included_file import IncludedFile

class MockIncludedFile:
    def __init__(self, filename, args, vars, hosts):
        self._filename = filename
        self._args = args
        self._vars = vars
        self._hosts = hosts

    def __repr__(self):
        return "%s (args=%s vars=%s): %s" % (self._filename, self._args, self._vars, self._hosts)

@pytest.fixture
def included_file():
    return MockIncludedFile("test_file.yml", {"arg1": "value1"}, {"var1": "value1"}, ["host1", "host2"])

def test_included_file_repr(included_file):
    expected_repr = "test_file.yml (args={'arg1': 'value1'} vars={'var1': 'value1'}): ['host1', 'host2']"
    assert repr(included_file) == expected_repr
