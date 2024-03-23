# file httpie/cli/dicts.py:49-50
# lines [49, 50]
# branches []

import pytest
from httpie.cli.dicts import RequestDataDict, MultiValueOrderedDict

def test_request_data_dict_initialization():
    # Test initialization of RequestDataDict
    data_dict = RequestDataDict()
    assert isinstance(data_dict, RequestDataDict)
    assert isinstance(data_dict, MultiValueOrderedDict)  # Ensure it's a subclass

def test_request_data_dict_usage(mocker):
    # Test usage of RequestDataDict to ensure it behaves like MultiValueOrderedDict
    setitem_mock = mocker.patch.object(MultiValueOrderedDict, '__setitem__')
    data_dict = RequestDataDict()
    data_dict['key'] = 'value'
    setitem_mock.assert_called_once_with('key', 'value')

    getitem_mock = mocker.patch.object(MultiValueOrderedDict, '__getitem__')
    _ = data_dict['key']
    getitem_mock.assert_called_once_with('key')

    delitem_mock = mocker.patch.object(MultiValueOrderedDict, '__delitem__')
    del data_dict['key']
    delitem_mock.assert_called_once_with('key')

    items_mock = mocker.patch.object(MultiValueOrderedDict, 'items')
    _ = data_dict.items()
    items_mock.assert_called_once()

    # Ensure that the test does not affect other tests by cleaning up the mock
    mocker.stopall()
