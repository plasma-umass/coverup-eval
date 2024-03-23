# file httpie/cli/dicts.py:45-46
# lines [45, 46]
# branches []

import pytest
from httpie.cli.dicts import RequestQueryParamsDict

def test_request_query_params_dict_initialization():
    # Test initialization of RequestQueryParamsDict
    query_params = RequestQueryParamsDict([('key1', 'value1'), ('key2', 'value2')])
    assert query_params['key1'] == 'value1'
    assert query_params['key2'] == 'value2'
    assert isinstance(query_params, RequestQueryParamsDict)
