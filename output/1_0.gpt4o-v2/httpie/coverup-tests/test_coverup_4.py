# file: httpie/cli/dicts.py:53-54
# asked: {"lines": [53, 54], "branches": []}
# gained: {"lines": [53, 54], "branches": []}

import pytest
from httpie.cli.dicts import MultipartRequestDataDict, MultiValueOrderedDict

def test_multipart_request_data_dict_inheritance():
    instance = MultipartRequestDataDict()
    assert isinstance(instance, MultiValueOrderedDict)
    assert isinstance(instance, MultipartRequestDataDict)
