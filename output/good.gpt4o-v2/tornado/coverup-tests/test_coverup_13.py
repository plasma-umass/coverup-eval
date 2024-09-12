# file: tornado/netutil.py:555-591
# asked: {"lines": [555, 568, 569, 570, 571, 574, 575, 576, 577, 579, 580, 581, 582, 583, 584, 585, 590, 591], "branches": [[568, 569], [568, 570], [575, 576], [575, 579], [579, 580], [579, 581], [581, 582], [581, 583], [583, 584], [583, 585], [585, 590], [585, 591]]}
# gained: {"lines": [555, 568, 569, 570, 571, 574, 575, 576, 577, 579, 580, 581, 582, 583, 584, 585, 590, 591], "branches": [[568, 569], [568, 570], [575, 576], [579, 580], [581, 582], [581, 583], [583, 584], [583, 585], [585, 590]]}

import pytest
import ssl
from tornado.netutil import ssl_options_to_context

_SSL_CONTEXT_KEYWORDS = frozenset(['ssl_version', 'certfile', 'keyfile', 'cert_reqs', 'ca_certs', 'ciphers'])

def test_ssl_options_to_context_with_sslcontext():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    result = ssl_options_to_context(context)
    assert result is context

def test_ssl_options_to_context_with_dict(monkeypatch):
    ssl_options = {
        'ssl_version': ssl.PROTOCOL_TLS,
        'certfile': 'path/to/certfile',
        'keyfile': 'path/to/keyfile',
        'cert_reqs': ssl.CERT_REQUIRED,
        'ca_certs': 'path/to/ca_certs',
        'ciphers': 'ECDHE+AESGCM'
    }

    def mock_load_cert_chain(self, certfile, keyfile=None):
        assert certfile == 'path/to/certfile'
        assert keyfile == 'path/to/keyfile'

    def mock_load_verify_locations(self, cafile=None, capath=None, cadata=None):
        assert cafile == 'path/to/ca_certs'

    def mock_set_ciphers(self, ciphers):
        assert ciphers == 'ECDHE+AESGCM'

    monkeypatch.setattr(ssl.SSLContext, 'load_cert_chain', mock_load_cert_chain)
    monkeypatch.setattr(ssl.SSLContext, 'load_verify_locations', mock_load_verify_locations)
    monkeypatch.setattr(ssl.SSLContext, 'set_ciphers', mock_set_ciphers)

    context = ssl_options_to_context(ssl_options)
    assert isinstance(context, ssl.SSLContext)
    assert context.verify_mode == ssl.CERT_REQUIRED
    assert context.options & ssl.OP_NO_COMPRESSION

def test_ssl_options_to_context_with_partial_dict(monkeypatch):
    ssl_options = {
        'certfile': 'path/to/certfile',
        'cert_reqs': ssl.CERT_OPTIONAL,
    }

    def mock_load_cert_chain(self, certfile, keyfile=None):
        assert certfile == 'path/to/certfile'
        assert keyfile is None

    monkeypatch.setattr(ssl.SSLContext, 'load_cert_chain', mock_load_cert_chain)

    context = ssl_options_to_context(ssl_options)
    assert isinstance(context, ssl.SSLContext)
    assert context.verify_mode == ssl.CERT_OPTIONAL
    assert context.options & ssl.OP_NO_COMPRESSION
