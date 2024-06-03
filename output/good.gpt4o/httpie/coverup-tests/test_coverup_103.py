# file httpie/output/formatters/json.py:7-34
# lines [10, 11, 14, 19, 20, 21, 22, 23, 24, 28, 29, 30, 31, 32, 34]
# branches ['19->21', '19->34']

import pytest
import json
from httpie.output.formatters.json import JSONFormatter

@pytest.fixture
def json_formatter():
    format_options = {
        'json': {
            'format': True,
            'sort_keys': True,
            'indent': 4
        }
    }
    return JSONFormatter(format_options=format_options, explicit_json=False)

def test_json_formatter_enabled(json_formatter):
    assert json_formatter.enabled is True

def test_json_formatter_format_body_valid_json(json_formatter):
    body = '{"key": "value"}'
    mime = 'application/json'
    formatted_body = json_formatter.format_body(body, mime)
    expected_body = json.dumps(json.loads(body), sort_keys=True, ensure_ascii=False, indent=4)
    assert formatted_body == expected_body

def test_json_formatter_format_body_invalid_json(json_formatter):
    body = 'invalid json'
    mime = 'application/json'
    formatted_body = json_formatter.format_body(body, mime)
    assert formatted_body == body

def test_json_formatter_format_body_non_json_mime(json_formatter):
    body = '{"key": "value"}'
    mime = 'text/plain'
    formatted_body = json_formatter.format_body(body, mime)
    expected_body = json.dumps(json.loads(body), sort_keys=True, ensure_ascii=False, indent=4)
    assert formatted_body == expected_body

def test_json_formatter_explicit_json(json_formatter):
    json_formatter.kwargs['explicit_json'] = True
    body = '{"key": "value"}'
    mime = 'text/plain'
    formatted_body = json_formatter.format_body(body, mime)
    expected_body = json.dumps(json.loads(body), sort_keys=True, ensure_ascii=False, indent=4)
    assert formatted_body == expected_body
