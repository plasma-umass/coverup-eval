# file httpie/cli/dicts.py:53-54
# lines [53, 54]
# branches []

import pytest
from httpie.cli.dicts import MultipartRequestDataDict

def test_multipart_request_data_dict_initialization():
    # Test the initialization of MultipartRequestDataDict
    multipart_dict = MultipartRequestDataDict([('key1', 'value1'), ('key2', 'value2')])
    assert multipart_dict['key1'] == 'value1'
    assert multipart_dict['key2'] == 'value2'
    assert isinstance(multipart_dict, MultipartRequestDataDict)
