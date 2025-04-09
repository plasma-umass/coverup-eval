# file lib/ansible/playbook/included_file.py:53-58
# lines [53, 54, 55, 56, 57, 58]
# branches []

import pytest
from ansible.playbook.included_file import IncludedFile
from unittest.mock import MagicMock

# Mock Task and Parent UUIDs
@pytest.fixture
def mock_task():
    task = MagicMock()
    task._uuid = '1234'
    task._parent = MagicMock()
    task._parent._uuid = '5678'
    return task

# Test function to improve coverage for IncludedFile __eq__ method
def test_included_file_eq(mock_task):
    # Create two IncludedFile instances with the same properties
    included_file1 = IncludedFile(filename='test_file.yml', args={'arg1': 'value1'}, vars={'var1': 'value1'}, task=mock_task)
    included_file2 = IncludedFile(filename='test_file.yml', args={'arg1': 'value1'}, vars={'var1': 'value1'}, task=mock_task)

    # Assert that the two instances are equal
    assert included_file1 == included_file2

    # Create a third IncludedFile instance with different properties
    included_file3 = IncludedFile(filename='different_file.yml', args={'arg1': 'value1'}, vars={'var1': 'value1'}, task=mock_task)

    # Assert that the first instance is not equal to the third instance
    assert not (included_file1 == included_file3)

    # Create a fourth IncludedFile instance with different task UUID
    mock_task_different_uuid = MagicMock()
    mock_task_different_uuid._uuid = '9999'
    mock_task_different_uuid._parent = MagicMock()
    mock_task_different_uuid._parent._uuid = '5678'

    included_file4 = IncludedFile(filename='test_file.yml', args={'arg1': 'value1'}, vars={'var1': 'value1'}, task=mock_task_different_uuid)

    # Assert that the first instance is not equal to the fourth instance
    assert not (included_file1 == included_file4)

    # Create a fifth IncludedFile instance with different parent task UUID
    mock_task_different_parent_uuid = MagicMock()
    mock_task_different_parent_uuid._uuid = '1234'
    mock_task_different_parent_uuid._parent = MagicMock()
    mock_task_different_parent_uuid._parent._uuid = '0000'

    included_file5 = IncludedFile(filename='test_file.yml', args={'arg1': 'value1'}, vars={'var1': 'value1'}, task=mock_task_different_parent_uuid)

    # Assert that the first instance is not equal to the fifth instance
    assert not (included_file1 == included_file5)
