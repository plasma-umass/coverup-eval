# file: httpie/cli/dicts.py:57-58
# asked: {"lines": [57, 58], "branches": []}
# gained: {"lines": [57, 58], "branches": []}

import pytest
from httpie.cli.dicts import RequestFilesDict, RequestDataDict, MultiValueOrderedDict

def test_request_files_dict_inheritance():
    # Ensure that RequestFilesDict is a subclass of RequestDataDict
    assert issubclass(RequestFilesDict, RequestDataDict)

    # Ensure that an instance of RequestFilesDict can be created
    request_files_dict = RequestFilesDict()
    assert isinstance(request_files_dict, RequestFilesDict)
    assert isinstance(request_files_dict, RequestDataDict)
    assert isinstance(request_files_dict, MultiValueOrderedDict)
