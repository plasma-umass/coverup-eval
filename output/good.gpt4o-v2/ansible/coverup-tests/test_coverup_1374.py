# file: lib/ansible/plugins/filter/core.py:558-566
# asked: {"lines": [561, 562, 563, 564, 566], "branches": [[561, 562], [561, 563], [563, 564], [563, 566]]}
# gained: {"lines": [561, 562, 563, 564, 566], "branches": [[561, 562], [561, 563], [563, 564], [563, 566]]}

import pytest
from ansible.errors import AnsibleFilterTypeError
from ansible.module_utils.six import string_types
from ansible.module_utils.common.collections import is_sequence
import os.path

from ansible.plugins.filter.core import path_join

def test_path_join_with_string():
    result = path_join("test/path")
    assert result == os.path.join("test/path")

def test_path_join_with_sequence():
    result = path_join(["test", "path"])
    assert result == os.path.join("test", "path")

def test_path_join_with_invalid_type():
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        path_join(123)
    assert "|path_join expects string or sequence, got" in str(excinfo.value)
