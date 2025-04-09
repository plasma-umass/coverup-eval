# file: lib/ansible/module_utils/urls.py:1034-1050
# asked: {"lines": [1037, 1043, 1044, 1046, 1049], "branches": [[1036, 1037], [1041, 1043], [1043, 1044], [1043, 1046], [1048, 1049]]}
# gained: {"lines": [1037, 1043, 1046, 1049], "branches": [[1036, 1037], [1041, 1043], [1043, 1046], [1048, 1049]]}

import pytest
from ssl import create_default_context
import ansible.module_utils.six.moves.urllib.request as urllib_request
from ansible.module_utils.urls import SSLValidationHandler

class MockSSLContext:
    def __init__(self, protocol):
        self.protocol = protocol
        self.verify_mode = None
        self.check_hostname = None

    def load_verify_locations(self, cafile=None, capath=None, cadata=None):
        self.cafile = cafile
        self.capath = capath
        self.cadata = cadata

@pytest.fixture
def mock_ssl_context(monkeypatch):
    monkeypatch.setattr("ssl.create_default_context", lambda cafile=None: MockSSLContext("PROTOCOL_TLS_CLIENT"))
    monkeypatch.setattr("ansible.module_utils.urls.create_default_context", lambda cafile=None: MockSSLContext("PROTOCOL_TLS_CLIENT"))

def test_make_context_with_cafile(mock_ssl_context):
    handler = SSLValidationHandler("hostname", 443, ca_path=None)
    context = handler.make_context(cafile="cafile", cadata=None)
    assert context.cafile == "cafile"
    assert context.cadata is None

def test_make_context_with_cadata(mock_ssl_context):
    handler = SSLValidationHandler("hostname", 443, ca_path=None)
    context = handler.make_context(cafile=None, cadata="cadata")
    assert context.cafile is None
    assert context.cadata == "cadata"

def test_make_context_with_ca_path(mock_ssl_context):
    handler = SSLValidationHandler("hostname", 443, ca_path="ca_path")
    context = handler.make_context(cafile="cafile", cadata="cadata")
    assert context.cafile == "ca_path"
    assert context.cadata is None

def test_make_context_no_ssl_support(monkeypatch):
    monkeypatch.setattr("ansible.module_utils.urls.HAS_SSLCONTEXT", False)
    monkeypatch.setattr("ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT", False)
    handler = SSLValidationHandler("hostname", 443, ca_path=None)
    with pytest.raises(NotImplementedError, match="Host libraries are too old to support creating an sslcontext"):
        handler.make_context(cafile=None, cadata=None)
