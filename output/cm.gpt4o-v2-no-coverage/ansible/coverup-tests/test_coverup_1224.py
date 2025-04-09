# file: lib/ansible/playbook/included_file.py:60-61
# asked: {"lines": [61], "branches": []}
# gained: {"lines": [61], "branches": []}

import pytest
from ansible.playbook.included_file import IncludedFile

@pytest.fixture
def included_file():
    return IncludedFile(filename="test_file.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="test_task")

def test_included_file_repr(included_file):
    included_file._hosts = ["host1", "host2"]
    expected_repr = "test_file.yml (args={'arg1': 'value1'} vars={'var1': 'value1'}): ['host1', 'host2']"
    assert repr(included_file) == expected_repr

def test_included_file_cleanup(included_file):
    included_file._hosts = ["host1", "host2"]
    del included_file._hosts
    assert not hasattr(included_file, '_hosts')
