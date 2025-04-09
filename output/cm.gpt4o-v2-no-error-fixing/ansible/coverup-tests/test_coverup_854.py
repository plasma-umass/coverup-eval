# file: lib/ansible/utils/unsafe_proxy.py:117-118
# asked: {"lines": [118], "branches": []}
# gained: {"lines": [118], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import _wrap_set, wrap_var

def test_wrap_set_with_empty_set():
    result = _wrap_set(set())
    assert result == set()

def test_wrap_set_with_non_empty_set():
    class AnsibleUnsafe:
        pass

    unsafe_item = AnsibleUnsafe()
    safe_item = "safe"
    input_set = {unsafe_item, safe_item}
    
    result = _wrap_set(input_set)
    
    assert len(result) == 2
    assert any(isinstance(item, AnsibleUnsafe) for item in result)
    assert any(item == "safe" for item in result)
