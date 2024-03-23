# file httpie/cli/dicts.py:13-14
# lines [13, 14]
# branches []

import pytest
from httpie.cli.dicts import RequestJSONDataDict
from collections import OrderedDict

def test_request_json_data_dict_initialization():
    # Test the initialization of RequestJSONDataDict
    data_dict = RequestJSONDataDict([('key1', 'value1'), ('key2', 'value2')])
    assert data_dict['key1'] == 'value1'
    assert data_dict['key2'] == 'value2'
    assert isinstance(data_dict, RequestJSONDataDict)
    assert isinstance(data_dict, OrderedDict)

def test_request_json_data_dict_order():
    # Test the order preservation of RequestJSONDataDict
    data_dict = RequestJSONDataDict([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
    keys = list(data_dict.keys())
    assert keys == ['key1', 'key2', 'key3']
    values = list(data_dict.values())
    assert values == ['value1', 'value2', 'value3']

def test_request_json_data_dict_update():
    # Test the update functionality of RequestJSONDataDict
    data_dict = RequestJSONDataDict()
    data_dict.update({'key1': 'value1', 'key2': 'value2'})
    assert data_dict['key1'] == 'value1'
    assert data_dict['key2'] == 'value2'

def test_request_json_data_dict_equality():
    # Test the equality check of RequestJSONDataDict
    data_dict1 = RequestJSONDataDict([('key1', 'value1'), ('key2', 'value2')])
    data_dict2 = RequestJSONDataDict([('key1', 'value1'), ('key2', 'value2')])
    assert data_dict1 == data_dict2

def test_request_json_data_dict_inequality():
    # Test the inequality check of RequestJSONDataDict
    data_dict1 = RequestJSONDataDict([('key1', 'value1'), ('key2', 'value2')])
    data_dict2 = RequestJSONDataDict([('key2', 'value2'), ('key1', 'value1')])
    assert data_dict1 != data_dict2
