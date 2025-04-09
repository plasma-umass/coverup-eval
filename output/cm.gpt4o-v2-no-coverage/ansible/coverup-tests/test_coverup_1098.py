# file: lib/ansible/plugins/lookup/url.py:186-224
# asked: {"lines": [186, 188, 190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}
# gained: {"lines": [186, 188, 190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.lookup.url import LookupModule
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import SSLValidationError, ConnectionError

@pytest.fixture
def lookup_module():
    module = LookupModule()
    module._load_name = "url"
    return module

def test_run_success(lookup_module, monkeypatch):
    terms = ["http://example.com"]
    variables = {}
    kwargs = {}

    mock_response = MagicMock()
    mock_response.read.return_value = b"response content"

    monkeypatch.setattr("ansible.plugins.lookup.url.open_url", lambda *args, **kwargs: mock_response)
    monkeypatch.setattr(lookup_module, "get_option", lambda option: False if option == "split_lines" else None)

    result = lookup_module.run(terms, variables, **kwargs)
    assert result == ["response content"]

def test_run_http_error(lookup_module, monkeypatch):
    terms = ["http://example.com"]
    variables = {}
    kwargs = {}

    monkeypatch.setattr("ansible.plugins.lookup.url.open_url", lambda *args, **kwargs: (_ for _ in ()).throw(HTTPError(None, None, None, None, None)))
    monkeypatch.setattr(lookup_module, "get_option", lambda option: None)

    with pytest.raises(AnsibleError, match="Received HTTP error for http://example.com"):
        lookup_module.run(terms, variables, **kwargs)

def test_run_url_error(lookup_module, monkeypatch):
    terms = ["http://example.com"]
    variables = {}
    kwargs = {}

    monkeypatch.setattr("ansible.plugins.lookup.url.open_url", lambda *args, **kwargs: (_ for _ in ()).throw(URLError(None)))
    monkeypatch.setattr(lookup_module, "get_option", lambda option: None)

    with pytest.raises(AnsibleError, match="Failed lookup url for http://example.com"):
        lookup_module.run(terms, variables, **kwargs)

def test_run_ssl_validation_error(lookup_module, monkeypatch):
    terms = ["http://example.com"]
    variables = {}
    kwargs = {}

    monkeypatch.setattr("ansible.plugins.lookup.url.open_url", lambda *args, **kwargs: (_ for _ in ()).throw(SSLValidationError(None)))
    monkeypatch.setattr(lookup_module, "get_option", lambda option: None)

    with pytest.raises(AnsibleError, match="Error validating the server's certificate for http://example.com"):
        lookup_module.run(terms, variables, **kwargs)

def test_run_connection_error(lookup_module, monkeypatch):
    terms = ["http://example.com"]
    variables = {}
    kwargs = {}

    monkeypatch.setattr("ansible.plugins.lookup.url.open_url", lambda *args, **kwargs: (_ for _ in ()).throw(ConnectionError(None)))
    monkeypatch.setattr(lookup_module, "get_option", lambda option: None)

    with pytest.raises(AnsibleError, match="Error connecting to http://example.com"):
        lookup_module.run(terms, variables, **kwargs)

def test_run_split_lines(lookup_module, monkeypatch):
    terms = ["http://example.com"]
    variables = {}
    kwargs = {}

    mock_response = MagicMock()
    mock_response.read.return_value = b"line1\nline2\nline3"

    monkeypatch.setattr("ansible.plugins.lookup.url.open_url", lambda *args, **kwargs: mock_response)
    monkeypatch.setattr(lookup_module, "get_option", lambda option: True if option == "split_lines" else None)

    result = lookup_module.run(terms, variables, **kwargs)
    assert result == ["line1", "line2", "line3"]
