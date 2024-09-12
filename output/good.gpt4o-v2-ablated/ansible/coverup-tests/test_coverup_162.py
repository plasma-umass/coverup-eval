# file: lib/ansible/plugins/filter/core.py:558-566
# asked: {"lines": [558, 561, 562, 563, 564, 566], "branches": [[561, 562], [561, 563], [563, 564], [563, 566]]}
# gained: {"lines": [558, 561, 562, 563, 564, 566], "branches": [[561, 562], [561, 563], [563, 564], [563, 566]]}

import os
import pytest
from ansible.errors import AnsibleFilterTypeError
from ansible.module_utils.six import string_types
from ansible.module_utils.common.collections import is_sequence

# Assuming the path_join function is imported from the module where it is defined
from ansible.plugins.filter.core import path_join

def test_path_join_with_string(monkeypatch):
    test_path = "test_path"
    expected_result = os.path.join(test_path)
    
    result = path_join(test_path)
    
    assert result == expected_result

def test_path_join_with_sequence(monkeypatch):
    test_paths = ["path1", "path2", "path3"]
    expected_result = os.path.join(*test_paths)
    
    result = path_join(test_paths)
    
    assert result == expected_result

def test_path_join_with_invalid_type(monkeypatch):
    test_input = 12345  # Not a string or sequence
    
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        path_join(test_input)
    
    assert "|path_join expects string or sequence, got" in str(excinfo.value)
