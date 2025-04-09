# file: lib/ansible/module_utils/common/_utils.py:14-40
# asked: {"lines": [37, 38, 39], "branches": [[36, 37], [37, 36], [37, 38]]}
# gained: {"lines": [37, 38, 39], "branches": [[36, 37], [37, 38]]}

import pytest

class Base:
    pass

class Sub1(Base):
    pass

class Sub2(Base):
    pass

class SubSub1(Sub1):
    pass

def test_get_all_subclasses():
    from ansible.module_utils.common._utils import get_all_subclasses

    subclasses = get_all_subclasses(Base)
    assert Sub1 in subclasses
    assert Sub2 in subclasses
    assert SubSub1 in subclasses
    assert Base not in subclasses
