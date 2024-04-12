# file lib/ansible/executor/powershell/module_manifest.py:254-261
# lines [258, 259, 260, 261]
# branches ['255->258']

import os
import pytest
from ansible.errors import AnsibleError
from ansible.executor.powershell.module_manifest import _slurp

def test_slurp_existing_file(tmp_path, mocker):
    # Create a temporary file and write some data to it
    test_file = tmp_path / "test_file.txt"
    test_data = b"Test data for _slurp"
    test_file.write_bytes(test_data)

    # Call the _slurp function with the path of the temporary file
    result = _slurp(str(test_file))

    # Assert that the result is the same as the test data
    assert result == test_data

def test_slurp_non_existing_file(mocker):
    # Mock os.path.exists to return False
    mocker.patch('os.path.exists', return_value=False)

    # Define a non-existing file path
    non_existing_file = '/path/to/non/existing/file'

    # Assert that AnsibleError is raised when calling _slurp with a non-existing file path
    with pytest.raises(AnsibleError) as excinfo:
        _slurp(non_existing_file)
    assert "imported module support code does not exist at" in str(excinfo.value)
