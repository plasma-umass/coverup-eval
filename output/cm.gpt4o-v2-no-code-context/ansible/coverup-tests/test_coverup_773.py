# file: lib/ansible/utils/unsafe_proxy.py:82-83
# asked: {"lines": [82, 83], "branches": []}
# gained: {"lines": [82, 83], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import NativeJinjaText, AnsibleUnsafeText

def test_native_jinja_unsafe_text_inheritance():
    class NativeJinjaUnsafeText(NativeJinjaText, AnsibleUnsafeText):
        pass

    instance = NativeJinjaUnsafeText("test")
    assert isinstance(instance, NativeJinjaText)
    assert isinstance(instance, AnsibleUnsafeText)
    assert instance == "test"
