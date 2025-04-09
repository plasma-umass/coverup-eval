# file: lib/ansible/module_utils/pycompat24.py:35-47
# asked: {"lines": [35, 47], "branches": []}
# gained: {"lines": [35, 47], "branches": []}

import pytest
import sys
from ansible.module_utils.pycompat24 import get_exception

def test_get_exception():
    try:
        raise ValueError("An error occurred")
    except Exception:
        e = get_exception()
        assert isinstance(e, ValueError)
        assert str(e) == "An error occurred"
