# file: lib/ansible/playbook/included_file.py:39-45
# asked: {"lines": [39, 40, 41, 42, 43, 44, 45], "branches": []}
# gained: {"lines": [39, 40, 41, 42, 43, 44, 45], "branches": []}

import pytest
from ansible.playbook.included_file import IncludedFile

@pytest.fixture
def included_file():
    return IncludedFile(filename="test_file.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="test_task")

def test_included_file_initialization(included_file):
    assert included_file._filename == "test_file.yml"
    assert included_file._args == {"arg1": "value1"}
    assert included_file._vars == {"var1": "value1"}
    assert included_file._task == "test_task"
    assert included_file._hosts == []
    assert included_file._is_role == False

def test_included_file_initialization_with_role():
    included_file = IncludedFile(filename="test_file.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="test_task", is_role=True)
    assert included_file._is_role == True
