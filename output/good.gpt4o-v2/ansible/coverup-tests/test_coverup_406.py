# file: lib/ansible/executor/powershell/module_manifest.py:254-261
# asked: {"lines": [254, 255, 256, 257, 258, 259, 260, 261], "branches": [[255, 256], [255, 258]]}
# gained: {"lines": [254, 255, 256, 257, 258, 259, 260, 261], "branches": [[255, 256], [255, 258]]}

import os
import pytest
from ansible.errors import AnsibleError
from ansible.executor.powershell.module_manifest import _slurp

def test_slurp_file_exists(tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "test_file.txt"
    temp_file.write_bytes(b"test content")

    # Test that _slurp reads the file correctly
    result = _slurp(str(temp_file))
    assert result == b"test content"

def test_slurp_file_does_not_exist():
    # Test that _slurp raises an error when the file does not exist
    with pytest.raises(AnsibleError, match="imported module support code does not exist at"):
        _slurp("non_existent_file.txt")
