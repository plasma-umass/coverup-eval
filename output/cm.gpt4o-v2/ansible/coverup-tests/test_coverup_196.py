# file: lib/ansible/module_utils/urls.py:1146-1166
# asked: {"lines": [1146, 1148, 1149, 1152, 1154, 1155, 1156, 1157, 1158, 1161, 1162, 1164, 1165, 1166], "branches": [[1148, 1149], [1148, 1152], [1161, 1162], [1161, 1164]]}
# gained: {"lines": [1146, 1148, 1149, 1152, 1154, 1155, 1156, 1161, 1162, 1164, 1165, 1166], "branches": [[1148, 1149], [1148, 1152], [1161, 1162]]}

import pytest
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import UnsupportedAlgorithm
from ansible.module_utils.urls import get_channel_binding_cert_hash

def test_get_channel_binding_cert_hash_with_crypto(monkeypatch):
    # Mock HAS_CRYPTOGRAPHY to be True
    monkeypatch.setattr('ansible.module_utils.urls.HAS_CRYPTOGRAPHY', True)
    
    # Create a dummy certificate in DER format
    certificate_der = b'0\x82\x03\x9e0\x82\x02\x86\xa0\x03\x02\x01\x02\x02\x10\x0b\x9a\xdc\x8a\x0e\x8a\x0b\x9a\xdc\x8a\x0e\x8a\x0b\x9a\xdc\x8a0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x000\x1e1\x1c0\x1a\x06\x03U\x04\x03\x0c\x13Test Certificate0\x1e\x17\r210101000000Z\x17\r220101000000Z0\x1e1\x1c0\x1a\x06\x03U\x04\x03\x0c\x13Test Certificate0\x82\x01"0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\xaf\x82\x01\x01\x00\xaf'
    
    # Mock the load_der_x509_certificate function to return a certificate with a known hash algorithm
    class MockCert:
        signature_hash_algorithm = hashes.SHA1()
    
    monkeypatch.setattr(x509, 'load_der_x509_certificate', lambda der, backend: MockCert())
    
    # Call the function and check the result
    result = get_channel_binding_cert_hash(certificate_der)
    assert result is not None
    assert isinstance(result, bytes)

def test_get_channel_binding_cert_hash_without_crypto(monkeypatch):
    # Mock HAS_CRYPTOGRAPHY to be False
    monkeypatch.setattr('ansible.module_utils.urls.HAS_CRYPTOGRAPHY', False)
    
    # Create a dummy certificate in DER format
    certificate_der = b'0\x82\x03\x9e0\x82\x02\x86\xa0\x03\x02\x01\x02\x02\x10\x0b\x9a\xdc\x8a\x0e\x8a\x0b\x9a\xdc\x8a\x0e\x8a\x0b\x9a\xdc\x8a0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x000\x1e1\x1c0\x1a\x06\x03U\x04\x03\x0c\x13Test Certificate0\x1e\x17\r210101000000Z\x17\r220101000000Z0\x1e1\x1c0\x1a\x06\x03U\x04\x03\x0c\x13Test Certificate0\x82\x01"0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\xaf\x82\x01\x01\x00\xaf'
    
    # Call the function and check the result
    result = get_channel_binding_cert_hash(certificate_der)
    assert result is None
