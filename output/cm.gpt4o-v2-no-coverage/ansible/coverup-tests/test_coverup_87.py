# file: lib/ansible/utils/unsafe_proxy.py:121-138
# asked: {"lines": [121, 122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}
# gained: {"lines": [121, 122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136]]}

import pytest
from ansible.utils.unsafe_proxy import wrap_var, AnsibleUnsafe, NativeJinjaUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafeText
from ansible.module_utils.common._collections_compat import Mapping, Set
from ansible.module_utils.common.collections import is_sequence
from ansible.utils.native_jinja import NativeJinjaText

class MockMapping(Mapping):
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

class MockSet(Set):
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        return item in self.data

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

def test_wrap_var_with_none():
    assert wrap_var(None) is None

def test_wrap_var_with_ansible_unsafe():
    unsafe_obj = AnsibleUnsafe()
    assert wrap_var(unsafe_obj) is unsafe_obj

def test_wrap_var_with_mapping():
    mapping = MockMapping({'key': 'value'})
    wrapped = wrap_var(mapping)
    assert isinstance(wrapped, dict)
    assert wrapped == {'key': 'value'}

def test_wrap_var_with_set():
    s = MockSet({'value'})
    wrapped = wrap_var(s)
    assert isinstance(wrapped, set)
    assert wrapped == {'value'}

def test_wrap_var_with_sequence():
    sequence = ['value1', 'value2']
    wrapped = wrap_var(sequence)
    assert isinstance(wrapped, list)
    assert wrapped == ['value1', 'value2']

def test_wrap_var_with_native_jinja_text():
    native_jinja_text = NativeJinjaText('text')
    wrapped = wrap_var(native_jinja_text)
    assert isinstance(wrapped, NativeJinjaUnsafeText)
    assert wrapped == 'text'

def test_wrap_var_with_binary_type():
    binary = b'binary'
    wrapped = wrap_var(binary)
    assert isinstance(wrapped, AnsibleUnsafeBytes)
    assert wrapped == b'binary'

def test_wrap_var_with_text_type():
    text = 'text'
    wrapped = wrap_var(text)
    assert isinstance(wrapped, AnsibleUnsafeText)
    assert wrapped == 'text'
