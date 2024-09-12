# file: httpie/cli/dicts.py:13-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import pytest
from collections import OrderedDict
from httpie.cli.dicts import RequestJSONDataDict

def test_request_json_data_dict_inheritance():
    obj = RequestJSONDataDict()
    assert isinstance(obj, OrderedDict)
    assert isinstance(obj, RequestJSONDataDict)
