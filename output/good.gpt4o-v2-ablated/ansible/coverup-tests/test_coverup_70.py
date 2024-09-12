# file: lib/ansible/module_utils/common/_utils.py:14-40
# asked: {"lines": [14, 28, 29, 31, 32, 34, 36, 37, 38, 39, 40], "branches": [[31, 32], [31, 40], [32, 31], [32, 34], [36, 32], [36, 37], [37, 36], [37, 38]]}
# gained: {"lines": [14, 28, 29, 31, 32, 34, 36, 37, 38, 39, 40], "branches": [[31, 32], [31, 40], [32, 31], [32, 34], [36, 32], [36, 37], [37, 38]]}

import pytest

def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(A):
        pass

    from ansible.module_utils.common._utils import get_all_subclasses

    subclasses = get_all_subclasses(A)
    assert subclasses == {B, C, D}

    subclasses = get_all_subclasses(B)
    assert subclasses == {C}

    subclasses = get_all_subclasses(C)
    assert subclasses == set()

    subclasses = get_all_subclasses(D)
    assert subclasses == set()
