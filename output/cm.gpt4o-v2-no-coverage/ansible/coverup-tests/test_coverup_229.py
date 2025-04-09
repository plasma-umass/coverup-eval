# file: lib/ansible/module_utils/common/_utils.py:14-40
# asked: {"lines": [14, 28, 29, 31, 32, 34, 36, 37, 38, 39, 40], "branches": [[31, 32], [31, 40], [32, 31], [32, 34], [36, 32], [36, 37], [37, 36], [37, 38]]}
# gained: {"lines": [14, 28, 29, 31, 32, 34, 36, 37, 38, 39, 40], "branches": [[31, 32], [31, 40], [32, 31], [32, 34], [36, 32], [36, 37], [37, 38]]}

import pytest
from ansible.module_utils.common._utils import get_all_subclasses

def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(A):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D}

    assert result == expected, f"Expected {expected}, but got {result}"

    # Clean up by deleting the created classes
    del A, B, C, D
