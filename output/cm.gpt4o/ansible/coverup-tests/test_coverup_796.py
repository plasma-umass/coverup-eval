# file lib/ansible/playbook/included_file.py:60-61
# lines [60, 61]
# branches []

import pytest
from ansible.playbook.included_file import IncludedFile

@pytest.fixture
def included_file():
    class MockIncludedFile(IncludedFile):
        def __init__(self, filename, args, vars, hosts):
            self._filename = filename
            self._args = args
            self._vars = vars
            self._hosts = hosts

    return MockIncludedFile("test_file.yml", {"arg1": "value1"}, {"var1": "value1"}, ["host1", "host2"])

def test_included_file_repr(included_file):
    repr_str = repr(included_file)
    assert repr_str == "test_file.yml (args={'arg1': 'value1'} vars={'var1': 'value1'}): ['host1', 'host2']"
