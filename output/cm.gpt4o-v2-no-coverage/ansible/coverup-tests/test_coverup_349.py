# file: lib/ansible/module_utils/facts/system/distribution.py:30-44
# asked: {"lines": [30, 32, 33, 36, 37, 40, 41, 44], "branches": [[32, 33], [32, 36], [36, 37], [36, 40], [40, 41], [40, 44]]}
# gained: {"lines": [30, 32, 33, 36, 37, 40, 41, 44], "branches": [[32, 33], [32, 36], [36, 37], [36, 40], [40, 41], [40, 44]]}

import os
import pytest
from unittest.mock import patch

from ansible.module_utils.facts.system.distribution import _file_exists

@pytest.mark.parametrize("path, allow_empty, exists, size, expected", [
    ("/fake/path", False, False, 0, False),  # Path does not exist
    ("/fake/path", True, False, 0, False),   # Path does not exist, allow_empty=True
    ("/fake/path", True, True, 0, True),     # Path exists, allow_empty=True
    ("/fake/path", False, True, 0, False),   # Path exists, size=0, allow_empty=False
    ("/fake/path", False, True, 10, True),   # Path exists, size>0, allow_empty=False
])
def test_file_exists(path, allow_empty, exists, size, expected):
    with patch("os.path.exists", return_value=exists):
        with patch("os.path.getsize", return_value=size):
            assert _file_exists(path, allow_empty) == expected
