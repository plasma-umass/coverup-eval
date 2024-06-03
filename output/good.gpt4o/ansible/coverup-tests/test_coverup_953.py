# file lib/ansible/module_utils/common/json.py:18-19
# lines [18, 19]
# branches []

import pytest
from ansible.module_utils.common.json import _is_unsafe

class MockValue:
    def __init__(self, unsafe, encrypted):
        self.__UNSAFE__ = unsafe
        self.__ENCRYPTED__ = encrypted

def test_is_unsafe():
    # Test case where value is unsafe and not encrypted
    value = MockValue(unsafe=True, encrypted=False)
    assert _is_unsafe(value) == True

    # Test case where value is unsafe and encrypted
    value = MockValue(unsafe=True, encrypted=True)
    assert _is_unsafe(value) == False

    # Test case where value is not unsafe
    value = MockValue(unsafe=False, encrypted=False)
    assert _is_unsafe(value) == False

    # Test case where value does not have __UNSAFE__ attribute
    class NoUnsafeAttr:
        __ENCRYPTED__ = False
    value = NoUnsafeAttr()
    assert _is_unsafe(value) == False

    # Test case where value does not have __ENCRYPTED__ attribute
    class NoEncryptedAttr:
        __UNSAFE__ = True
    value = NoEncryptedAttr()
    assert _is_unsafe(value) == True

    # Test case where value does not have both __UNSAFE__ and __ENCRYPTED__ attributes
    class NoUnsafeAndEncryptedAttr:
        pass
    value = NoUnsafeAndEncryptedAttr()
    assert _is_unsafe(value) == False
