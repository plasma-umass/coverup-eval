# file: lib/ansible/utils/unsafe_proxy.py:82-83
# asked: {"lines": [82, 83], "branches": []}
# gained: {"lines": [82, 83], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import NativeJinjaUnsafeText
from ansible.utils.native_jinja import NativeJinjaText
from ansible.module_utils.six import text_type

def test_native_jinja_unsafe_text_inheritance():
    # Ensure NativeJinjaUnsafeText inherits from NativeJinjaText and AnsibleUnsafeText
    assert issubclass(NativeJinjaUnsafeText, NativeJinjaText)
    assert issubclass(NativeJinjaUnsafeText, text_type)

def test_native_jinja_unsafe_text_instance():
    # Ensure an instance of NativeJinjaUnsafeText can be created and is an instance of the expected classes
    instance = NativeJinjaUnsafeText("test")
    assert isinstance(instance, NativeJinjaUnsafeText)
    assert isinstance(instance, NativeJinjaText)
    assert isinstance(instance, text_type)
