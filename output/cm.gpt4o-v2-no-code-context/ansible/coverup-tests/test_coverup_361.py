# file: lib/ansible/executor/powershell/module_manifest.py:254-261
# asked: {"lines": [254, 255, 256, 257, 258, 259, 260, 261], "branches": [[255, 256], [255, 258]]}
# gained: {"lines": [254, 255, 256, 257, 258, 259, 260, 261], "branches": [[255, 256], [255, 258]]}

import os
import pytest
from ansible.errors import AnsibleError
from ansible.executor.powershell.module_manifest import _slurp

def test_slurp_file_exists(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_content = b"test content"
    test_file.write_bytes(test_content)

    result = _slurp(str(test_file))
    assert result == test_content

def test_slurp_file_does_not_exist():
    with pytest.raises(AnsibleError, match="imported module support code does not exist at"):
        _slurp("non_existent_file.txt")
