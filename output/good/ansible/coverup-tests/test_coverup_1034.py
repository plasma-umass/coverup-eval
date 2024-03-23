# file lib/ansible/module_utils/common/json.py:18-19
# lines [18, 19]
# branches []

import pytest
from ansible.module_utils.common.json import _is_unsafe

class MockUnsafe:
    __UNSAFE__ = True
    __ENCRYPTED__ = False

class MockSafe:
    __UNSAFE__ = False
    __ENCRYPTED__ = False

class MockEncryptedUnsafe:
    __UNSAFE__ = True
    __ENCRYPTED__ = True

@pytest.fixture
def unsafe_value():
    return MockUnsafe()

@pytest.fixture
def safe_value():
    return MockSafe()

@pytest.fixture
def encrypted_unsafe_value():
    return MockEncryptedUnsafe()

def test_is_unsafe_with_unsafe_value(unsafe_value):
    assert _is_unsafe(unsafe_value) is True

def test_is_unsafe_with_safe_value(safe_value):
    assert _is_unsafe(safe_value) is False

def test_is_unsafe_with_encrypted_unsafe_value(encrypted_unsafe_value):
    assert _is_unsafe(encrypted_unsafe_value) is False
