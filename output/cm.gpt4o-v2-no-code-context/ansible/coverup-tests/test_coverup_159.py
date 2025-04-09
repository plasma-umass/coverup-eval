# file: lib/ansible/module_utils/common/_utils.py:14-40
# asked: {"lines": [14, 28, 29, 31, 32, 34, 36, 37, 38, 39, 40], "branches": [[31, 32], [31, 40], [32, 31], [32, 34], [36, 32], [36, 37], [37, 36], [37, 38]]}
# gained: {"lines": [14, 28, 29, 31, 32, 34, 36, 37, 38, 39, 40], "branches": [[31, 32], [31, 40], [32, 31], [32, 34], [36, 32], [36, 37], [37, 38]]}

import pytest

class Base:
    pass

class Sub1(Base):
    pass

class Sub2(Base):
    pass

class SubSub1(Sub1):
    pass

class SubSub2(Sub1):
    pass

def test_get_all_subclasses():
    from ansible.module_utils.common._utils import get_all_subclasses

    subclasses = get_all_subclasses(Base)
    assert subclasses == {Sub1, Sub2, SubSub1, SubSub2}

    subclasses = get_all_subclasses(Sub1)
    assert subclasses == {SubSub1, SubSub2}

    subclasses = get_all_subclasses(Sub2)
    assert subclasses == set()

    subclasses = get_all_subclasses(SubSub1)
    assert subclasses == set()

    subclasses = get_all_subclasses(SubSub2)
    assert subclasses == set()
