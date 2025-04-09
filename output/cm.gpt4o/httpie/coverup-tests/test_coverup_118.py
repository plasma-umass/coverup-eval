# file httpie/output/formatters/json.py:7-34
# lines []
# branches ['19->34']

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

def test_format_body_with_explicit_json(json_formatter):
    json_formatter.kwargs['explicit_json'] = True
    body = '{"key": "value"}'
    mime = 'application/json'
    formatted_body = json_formatter.format_body(body, mime)
    assert formatted_body == json.dumps(
        obj=json.loads(body),
        sort_keys=True,
        ensure_ascii=False,
        indent=4
    )

def test_format_body_with_invalid_json(json_formatter):
    json_formatter.kwargs['explicit_json'] = True
    body = '{"key": "value"'
    mime = 'application/json'
    formatted_body = json_formatter.format_body(body, mime)
    assert formatted_body == body

def test_format_body_with_mime_containing_json(json_formatter):
    body = '{"key": "value"}'
    mime = 'application/javascript'
    formatted_body = json_formatter.format_body(body, mime)
    assert formatted_body == json.dumps(
        obj=json.loads(body),
        sort_keys=True,
        ensure_ascii=False,
        indent=4
    )

def test_format_body_with_non_json_mime(json_formatter):
    body = '{"key": "value"}'
    mime = 'text/plain'
    formatted_body = json_formatter.format_body(body, mime)
    assert formatted_body == json.dumps(
        obj=json.loads(body),
        sort_keys=True,
        ensure_ascii=False,
        indent=4
    )

def test_format_body_with_non_matching_mime(json_formatter):
    body = '{"key": "value"}'
    mime = 'image/png'
    formatted_body = json_formatter.format_body(body, mime)
    assert formatted_body == body
