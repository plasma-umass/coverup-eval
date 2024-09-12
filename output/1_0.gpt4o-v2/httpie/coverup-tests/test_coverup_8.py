# file: httpie/cli/dicts.py:45-46
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

import pytest
from httpie.cli.dicts import RequestQueryParamsDict, MultiValueOrderedDict

def test_request_query_params_dict_inheritance():
    # Ensure that RequestQueryParamsDict is a subclass of MultiValueOrderedDict
    assert issubclass(RequestQueryParamsDict, MultiValueOrderedDict)

def test_request_query_params_dict_instance():
    # Ensure that an instance of RequestQueryParamsDict can be created
    instance = RequestQueryParamsDict()
    assert isinstance(instance, RequestQueryParamsDict)
    assert isinstance(instance, MultiValueOrderedDict)
