# file lib/ansible/utils/unsafe_proxy.py:82-83
# lines [82, 83]
# branches []

import pytest
from ansible.utils.unsafe_proxy import NativeJinjaText, AnsibleUnsafeText

class TestNativeJinjaUnsafeText:
    def test_inheritance(self):
        class NativeJinjaUnsafeText(NativeJinjaText, AnsibleUnsafeText):
            pass

        instance = NativeJinjaUnsafeText("test")
        assert isinstance(instance, NativeJinjaText)
        assert isinstance(instance, AnsibleUnsafeText)
        assert instance == "test"
