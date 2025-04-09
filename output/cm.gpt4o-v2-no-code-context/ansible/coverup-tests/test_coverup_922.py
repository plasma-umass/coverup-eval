# file: lib/ansible/plugins/lookup/url.py:186-224
# asked: {"lines": [186, 188, 190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}
# gained: {"lines": [186, 188, 190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.lookup.url import LookupModule
from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import SSLValidationError, ConnectionError

@pytest.fixture
def lookup_module():
    module = LookupModule()
    module._load_name = 'url'
    return module

def test_run_success(monkeypatch, lookup_module):
    terms = ['http://example.com']
    variables = {}
    kwargs = {}

    mock_response = MagicMock()
    mock_response.read.return_value = b"response content"

    def mock_open_url(*args, **kwargs):
        return mock_response

    monkeypatch.setattr('ansible.plugins.lookup.url.open_url', mock_open_url)
    monkeypatch.setattr(lookup_module, 'get_option', lambda x: False)

    result = lookup_module.run(terms, variables, **kwargs)
    assert result == ['response content']

def test_run_http_error(monkeypatch, lookup_module):
    terms = ['http://example.com']
    variables = {}
    kwargs = {}

    def mock_open_url(*args, **kwargs):
        raise HTTPError(None, None, None, None, None)

    monkeypatch.setattr('ansible.plugins.lookup.url.open_url', mock_open_url)
    monkeypatch.setattr(lookup_module, 'get_option', lambda x: False)

    with pytest.raises(AnsibleError, match="Received HTTP error for http://example.com"):
        lookup_module.run(terms, variables, **kwargs)

def test_run_url_error(monkeypatch, lookup_module):
    terms = ['http://example.com']
    variables = {}
    kwargs = {}

    def mock_open_url(*args, **kwargs):
        raise URLError(None)

    monkeypatch.setattr('ansible.plugins.lookup.url.open_url', mock_open_url)
    monkeypatch.setattr(lookup_module, 'get_option', lambda x: False)

    with pytest.raises(AnsibleError, match="Failed lookup url for http://example.com"):
        lookup_module.run(terms, variables, **kwargs)

def test_run_ssl_validation_error(monkeypatch, lookup_module):
    terms = ['http://example.com']
    variables = {}
    kwargs = {}

    def mock_open_url(*args, **kwargs):
        raise SSLValidationError(None)

    monkeypatch.setattr('ansible.plugins.lookup.url.open_url', mock_open_url)
    monkeypatch.setattr(lookup_module, 'get_option', lambda x: False)

    with pytest.raises(AnsibleError, match="Error validating the server's certificate for http://example.com"):
        lookup_module.run(terms, variables, **kwargs)

def test_run_connection_error(monkeypatch, lookup_module):
    terms = ['http://example.com']
    variables = {}
    kwargs = {}

    def mock_open_url(*args, **kwargs):
        raise ConnectionError(None)

    monkeypatch.setattr('ansible.plugins.lookup.url.open_url', mock_open_url)
    monkeypatch.setattr(lookup_module, 'get_option', lambda x: False)

    with pytest.raises(AnsibleError, match="Error connecting to http://example.com"):
        lookup_module.run(terms, variables, **kwargs)

def test_run_split_lines(monkeypatch, lookup_module):
    terms = ['http://example.com']
    variables = {}
    kwargs = {}

    mock_response = MagicMock()
    mock_response.read.return_value = b"line1\nline2\nline3"

    def mock_open_url(*args, **kwargs):
        return mock_response

    monkeypatch.setattr('ansible.plugins.lookup.url.open_url', mock_open_url)
    monkeypatch.setattr(lookup_module, 'get_option', lambda x: x == 'split_lines')

    result = lookup_module.run(terms, variables, **kwargs)
    assert result == ['line1', 'line2', 'line3']
