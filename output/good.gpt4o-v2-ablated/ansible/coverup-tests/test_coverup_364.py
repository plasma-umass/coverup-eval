# file: lib/ansible/utils/unsafe_proxy.py:82-83
# asked: {"lines": [82, 83], "branches": []}
# gained: {"lines": [82, 83], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import NativeJinjaUnsafeText, NativeJinjaText, AnsibleUnsafeText

def test_native_jinja_unsafe_text_inheritance():
    # Test that NativeJinjaUnsafeText inherits from NativeJinjaText and AnsibleUnsafeText
    assert issubclass(NativeJinjaUnsafeText, NativeJinjaText)
    assert issubclass(NativeJinjaUnsafeText, AnsibleUnsafeText)

def test_native_jinja_unsafe_text_instance():
    # Test that an instance of NativeJinjaUnsafeText is also an instance of NativeJinjaText and AnsibleUnsafeText
    instance = NativeJinjaUnsafeText("test")
    assert isinstance(instance, NativeJinjaUnsafeText)
    assert isinstance(instance, NativeJinjaText)
    assert isinstance(instance, AnsibleUnsafeText)
    assert instance == "test"
