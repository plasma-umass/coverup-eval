# file lib/ansible/module_utils/common/_utils.py:14-40
# lines [14, 28, 29, 31, 32, 34, 36, 37, 38, 39, 40]
# branches ['31->32', '31->40', '32->31', '32->34', '36->32', '36->37', '37->36', '37->38']

import pytest

class Base:
    pass

class ChildA(Base):
    pass

class ChildB(Base):
    pass

class GrandChildA1(ChildA):
    pass

class GrandChildA2(ChildA):
    pass

class GrandChildB1(ChildB):
    pass

class GrandChildB2(ChildB):
    pass

def test_get_all_subclasses():
    from ansible.module_utils.common._utils import get_all_subclasses

    # Test that all subclasses are found, including grandchildren
    expected_subclasses = {ChildA, ChildB, GrandChildA1, GrandChildA2, GrandChildB1, GrandChildB2}
    found_subclasses = get_all_subclasses(Base)
    assert found_subclasses == expected_subclasses

    # Test that no subclasses are found for a class without subclasses
    assert get_all_subclasses(GrandChildA1) == set()

    # Test that direct subclasses are found
    assert get_all_subclasses(ChildA) == {GrandChildA1, GrandChildA2}

    # Test that direct subclasses are found
    assert get_all_subclasses(ChildB) == {GrandChildB1, GrandChildB2}
