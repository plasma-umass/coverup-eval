# file sanic/response.py:251-274
# lines [251, 253, 254, 255, 256, 267, 268, 269, 270, 271, 272, 273]
# branches ['267->268', '267->269']

import pytest
from sanic.response import json, HTTPResponse
from unittest.mock import Mock

@pytest.fixture
def mock_dumps():
    return Mock(return_value='{"key": "value"}')

def test_json_with_custom_dumps(mock_dumps):
    # Setup
    body = {"key": "value"}
    status = 200
    headers = {"Custom-Header": "Custom Value"}
    content_type = "application/json"
    kwargs = {"indent": 2}

    # Execute
    response = json(
        body,
        status=status,
        headers=headers,
        content_type=content_type,
        dumps=mock_dumps,
        **kwargs
    )

    # Verify
    mock_dumps.assert_called_once_with(body, **kwargs)
    assert isinstance(response, HTTPResponse)
    assert response.status == status
    assert response.headers == headers
    assert response.content_type == content_type
    assert response.body == b'{"key": "value"}'

    # Cleanup - nothing to clean up as the test does not affect global state
