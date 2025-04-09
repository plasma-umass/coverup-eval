# file: lib/ansible/module_utils/common/dict_transformations.py:16-52
# asked: {"lines": [37], "branches": [[36, 37]]}
# gained: {"lines": [37], "branches": [[36, 37]]}

import pytest
from ansible.module_utils.common.dict_transformations import camel_dict_to_snake_dict

def test_camel_dict_to_snake_dict_simple():
    camel_dict = {'SimpleKey': 'value'}
    expected = {'simple_key': 'value'}
    result = camel_dict_to_snake_dict(camel_dict)
    assert result == expected

def test_camel_dict_to_snake_dict_nested():
    camel_dict = {'NestedKey': {'InnerKey': 'value'}}
    expected = {'nested_key': {'inner_key': 'value'}}
    result = camel_dict_to_snake_dict(camel_dict)
    assert result == expected

def test_camel_dict_to_snake_dict_list():
    camel_dict = {'ListKey': [{'InnerKey': 'value'}, 'string']}
    expected = {'list_key': [{'inner_key': 'value'}, 'string']}
    result = camel_dict_to_snake_dict(camel_dict)
    assert result == expected

def test_camel_dict_to_snake_dict_reversible():
    camel_dict = {'HTTPEndpoint': 'value'}
    expected = {'h_t_t_p_endpoint': 'value'}
    result = camel_dict_to_snake_dict(camel_dict, reversible=True)
    assert result == expected

def test_camel_dict_to_snake_dict_ignore_list():
    camel_dict = {'Tags': {'Key': 'value'}, 'OtherKey': 'othervalue'}
    expected = {'tags': {'Key': 'value'}, 'other_key': 'othervalue'}
    result = camel_dict_to_snake_dict(camel_dict, ignore_list=['Tags'])
    assert result == expected

def test_camel_dict_to_snake_dict_complex():
    camel_dict = {
        'ComplexKey': {
            'NestedList': [
                {'InnerKey': 'value'},
                ['SubListItem']
            ],
            'AnotherKey': 'anothervalue'
        }
    }
    expected = {
        'complex_key': {
            'nested_list': [
                {'inner_key': 'value'},
                ['SubListItem']
            ],
            'another_key': 'anothervalue'
        }
    }
    result = camel_dict_to_snake_dict(camel_dict)
    assert result == expected
