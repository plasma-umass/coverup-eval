# file: lib/ansible/playbook/included_file.py:53-58
# asked: {"lines": [54, 55, 56, 57, 58], "branches": []}
# gained: {"lines": [54, 55, 56, 57, 58], "branches": []}

import pytest

from ansible.playbook.included_file import IncludedFile

class MockTask:
    def __init__(self, uuid, parent=None):
        self._uuid = uuid
        self._parent = parent

def test_included_file_equality():
    task1 = MockTask(uuid="1234", parent=MockTask(uuid="5678"))
    task2 = MockTask(uuid="1234", parent=MockTask(uuid="5678"))
    task3 = MockTask(uuid="1234", parent=MockTask(uuid="91011"))

    file1 = IncludedFile(filename="file1.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task=task1)
    file2 = IncludedFile(filename="file1.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task=task2)
    file3 = IncludedFile(filename="file1.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task=task3)
    file4 = IncludedFile(filename="file2.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task=task1)

    assert file1 == file2  # Should be equal
    assert file1 != file3  # Different parent UUID
    assert file1 != file4  # Different filename
