# file: lib/ansible/template/native_helpers.py:46-93
# asked: {"lines": [82], "branches": [[81, 82]]}
# gained: {"lines": [82], "branches": [[81, 82]]}

import pytest
from itertools import chain
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.utils.native_jinja import NativeJinjaText
from ansible.module_utils.six import string_types
from ansible.module_utils._text import to_text
from ansible.template.native_helpers import ansible_native_concat

def _fail_on_undefined(data):
    from jinja2.runtime import StrictUndefined
    from ansible.module_utils.common.collections import is_sequence, Mapping

    if isinstance(data, Mapping):
        for value in data.values():
            _fail_on_undefined(value)
    elif is_sequence(data):
        for item in data:
            _fail_on_undefined(item)
    elif isinstance(data, StrictUndefined):
        str(data)
    return data

def test_ansible_native_concat_with_generator():
    # Create a generator
    def node_generator():
        yield "1"
        yield "2"
        yield "3"

    nodes = node_generator()
    result = ansible_native_concat(nodes)
    
    # Assert the result is as expected
    assert result == 123

def test_ansible_native_concat_with_empty_generator():
    # Create an empty generator
    def empty_generator():
        if False:
            yield

    nodes = empty_generator()
    result = ansible_native_concat(nodes)
    
    # Assert the result is as expected
    assert result is None

def test_ansible_native_concat_with_single_node():
    nodes = ["42"]
    result = ansible_native_concat(nodes)
    
    # Assert the result is as expected
    assert result == 42

def test_ansible_native_concat_with_vault_encrypted_unicode():
    nodes = [AnsibleVaultEncryptedUnicode("encrypted_data")]
    result = ansible_native_concat(nodes)
    
    # Assert the result is as expected
    assert result == "encrypted_data"

def test_ansible_native_concat_with_native_jinja_text():
    nodes = [NativeJinjaText("native_jinja_text")]
    result = ansible_native_concat(nodes)
    
    # Assert the result is as expected
    assert result == "native_jinja_text"

def test_ansible_native_concat_with_non_string_type():
    nodes = [42]
    result = ansible_native_concat(nodes)
    
    # Assert the result is as expected
    assert result == 42

def test_ansible_native_concat_with_mixed_nodes():
    nodes = ["1", "2", "3"]
    result = ansible_native_concat(nodes)
    
    # Assert the result is as expected
    assert result == 123
