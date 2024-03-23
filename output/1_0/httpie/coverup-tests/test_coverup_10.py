# file httpie/cli/constants.py:108-111
# lines [108, 109, 110, 111]
# branches []

import pytest
from httpie.cli.constants import RequestType

def test_request_type_enum():
    assert RequestType.FORM is not None
    assert RequestType.MULTIPART is not None
    assert RequestType.JSON is not None

    # Check that the enum has exactly three members
    assert len(RequestType) == 3

    # Check that the names are correct
    assert RequestType.FORM.name == "FORM"
    assert RequestType.MULTIPART.name == "MULTIPART"
    assert RequestType.JSON.name == "JSON"

    # Check that the values are unique
    assert RequestType.FORM.value != RequestType.MULTIPART.value
    assert RequestType.FORM.value != RequestType.JSON.value
    assert RequestType.MULTIPART.value != RequestType.JSON.value
