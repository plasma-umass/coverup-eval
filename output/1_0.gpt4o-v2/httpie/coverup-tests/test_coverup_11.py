# file: httpie/cli/constants.py:108-111
# asked: {"lines": [108, 109, 110, 111], "branches": []}
# gained: {"lines": [108, 109, 110, 111], "branches": []}

import enum
import pytest
from httpie.cli.constants import RequestType

def test_request_type_enum():
    assert RequestType.FORM.name == 'FORM'
    assert RequestType.MULTIPART.name == 'MULTIPART'
    assert RequestType.JSON.name == 'JSON'
    assert isinstance(RequestType.FORM, RequestType)
    assert isinstance(RequestType.MULTIPART, RequestType)
    assert isinstance(RequestType.JSON, RequestType)
