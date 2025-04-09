# file: lib/ansible/module_utils/common/json.py:18-19
# asked: {"lines": [18, 19], "branches": []}
# gained: {"lines": [18, 19], "branches": []}

import pytest

from ansible.module_utils.common.json import _is_unsafe

class TestIsUnsafe:
    def test_is_unsafe_true(self):
        class TestValue:
            __UNSAFE__ = True
            __ENCRYPTED__ = False

        value = TestValue()
        assert _is_unsafe(value) is True

    def test_is_unsafe_false_encrypted(self):
        class TestValue:
            __UNSAFE__ = True
            __ENCRYPTED__ = True

        value = TestValue()
        assert _is_unsafe(value) is False

    def test_is_unsafe_false_not_unsafe(self):
        class TestValue:
            __UNSAFE__ = False
            __ENCRYPTED__ = False

        value = TestValue()
        assert _is_unsafe(value) is False

    def test_is_unsafe_false_no_unsafe_attr(self):
        class TestValue:
            __ENCRYPTED__ = False

        value = TestValue()
        assert _is_unsafe(value) is False

    def test_is_unsafe_false_no_encrypted_attr(self):
        class TestValue:
            __UNSAFE__ = True

        value = TestValue()
        assert _is_unsafe(value) is True

    def test_is_unsafe_false_no_attrs(self):
        class TestValue:
            pass

        value = TestValue()
        assert _is_unsafe(value) is False
