# file: httpie/output/formatters/json.py:7-34
# asked: {"lines": [7, 9, 10, 11, 13, 14, 19, 20, 21, 22, 23, 24, 28, 29, 30, 31, 32, 34], "branches": [[19, 21], [19, 34]]}
# gained: {"lines": [7, 9, 10, 11, 13, 14, 19, 20, 21, 22, 23, 24, 28, 29, 30, 31, 32, 34], "branches": [[19, 21]]}

import pytest
import json
from httpie.output.formatters.json import JSONFormatter

@pytest.fixture
def formatter():
    return JSONFormatter(
        format_options={
            'json': {
                'format': True,
                'sort_keys': True,
                'indent': 4
            }
        },
        explicit_json=False
    )

def test_format_body_with_valid_json(formatter):
    body = '{"key": "value"}'
    mime = 'application/json'
    formatted_body = formatter.format_body(body, mime)
    expected_body = json.dumps(
        obj=json.loads(body),
        sort_keys=True,
        ensure_ascii=False,
        indent=4
    )
    assert formatted_body == expected_body

def test_format_body_with_invalid_json(formatter):
    body = '{"key": "value"'
    mime = 'application/json'
    formatted_body = formatter.format_body(body, mime)
    assert formatted_body == body  # Should return the original body

def test_format_body_with_non_json_mime(formatter):
    body = '{"key": "value"}'
    mime = 'text/plain'
    formatted_body = formatter.format_body(body, mime)
    expected_body = json.dumps(
        obj=json.loads(body),
        sort_keys=True,
        ensure_ascii=False,
        indent=4
    )
    assert formatted_body == expected_body  # Should return the formatted body

def test_format_body_with_explicit_json(formatter, monkeypatch):
    monkeypatch.setattr(formatter, 'kwargs', {'explicit_json': True})
    body = '{"key": "value"}'
    mime = 'text/plain'
    formatted_body = formatter.format_body(body, mime)
    expected_body = json.dumps(
        obj=json.loads(body),
        sort_keys=True,
        ensure_ascii=False,
        indent=4
    )
    assert formatted_body == expected_body
