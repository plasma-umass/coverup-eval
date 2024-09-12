# file: httpie/cli/dicts.py:49-50
# asked: {"lines": [49, 50], "branches": []}
# gained: {"lines": [49, 50], "branches": []}

import pytest
from httpie.cli.dicts import RequestDataDict, MultiValueOrderedDict

def test_request_data_dict_inheritance():
    # Ensure that RequestDataDict is a subclass of MultiValueOrderedDict
    assert issubclass(RequestDataDict, MultiValueOrderedDict)

def test_request_data_dict_instance():
    # Ensure that an instance of RequestDataDict can be created
    rdd = RequestDataDict()
    assert isinstance(rdd, RequestDataDict)
    assert isinstance(rdd, MultiValueOrderedDict)
