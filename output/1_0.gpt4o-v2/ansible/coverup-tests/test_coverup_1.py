# file: lib/ansible/utils/native_jinja.py:12-13
# asked: {"lines": [12, 13], "branches": []}
# gained: {"lines": [12, 13], "branches": []}

import pytest
from ansible.utils.native_jinja import NativeJinjaText
from ansible.module_utils.six import text_type

def test_native_jinja_text_inheritance():
    # Verify that NativeJinjaText is a subclass of text_type
    assert issubclass(NativeJinjaText, text_type)

def test_native_jinja_text_instance():
    # Verify that an instance of NativeJinjaText can be created and is an instance of text_type
    instance = NativeJinjaText("test")
    assert isinstance(instance, NativeJinjaText)
    assert isinstance(instance, text_type)
    assert instance == "test"
