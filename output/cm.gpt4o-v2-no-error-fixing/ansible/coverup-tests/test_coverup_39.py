# file: lib/ansible/utils/unsafe_proxy.py:121-138
# asked: {"lines": [121, 122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}
# gained: {"lines": [121, 122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136]]}

import pytest
from ansible.utils.unsafe_proxy import wrap_var, AnsibleUnsafe
from ansible.module_utils.common._collections_compat import Mapping, Set
from ansible.module_utils.common.collections import is_sequence
from ansible.module_utils.six import binary_type, text_type
from ansible.utils.native_jinja import NativeJinjaText
from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes, AnsibleUnsafeText, NativeJinjaUnsafeText

class TestWrapVar:

    def test_wrap_var_none(self):
        assert wrap_var(None) is None

    def test_wrap_var_ansible_unsafe(self):
        unsafe_obj = AnsibleUnsafe()
        assert wrap_var(unsafe_obj) is unsafe_obj

    def test_wrap_var_mapping(self, mocker):
        mock_wrap_dict = mocker.patch('ansible.utils.unsafe_proxy._wrap_dict', return_value={'wrapped': 'dict'})
        result = wrap_var({'key': 'value'})
        mock_wrap_dict.assert_called_once_with({'key': 'value'})
        assert result == {'wrapped': 'dict'}

    def test_wrap_var_set(self, mocker):
        mock_wrap_set = mocker.patch('ansible.utils.unsafe_proxy._wrap_set', return_value={'wrapped_set'})
        result = wrap_var({'item1', 'item2'})
        mock_wrap_set.assert_called_once_with({'item1', 'item2'})
        assert result == {'wrapped_set'}

    def test_wrap_var_sequence(self, mocker):
        mock_wrap_sequence = mocker.patch('ansible.utils.unsafe_proxy._wrap_sequence', return_value=['wrapped_sequence'])
        result = wrap_var(['item1', 'item2'])
        mock_wrap_sequence.assert_called_once_with(['item1', 'item2'])
        assert result == ['wrapped_sequence']

    def test_wrap_var_native_jinja_text(self):
        native_jinja_text = NativeJinjaText("some text")
        result = wrap_var(native_jinja_text)
        assert isinstance(result, NativeJinjaUnsafeText)
        assert result == native_jinja_text

    def test_wrap_var_binary_type(self):
        binary_data = binary_type(b'some binary data')
        result = wrap_var(binary_data)
        assert isinstance(result, AnsibleUnsafeBytes)
        assert result == binary_data

    def test_wrap_var_text_type(self):
        text_data = text_type('some text data')
        result = wrap_var(text_data)
        assert isinstance(result, AnsibleUnsafeText)
        assert result == text_data
