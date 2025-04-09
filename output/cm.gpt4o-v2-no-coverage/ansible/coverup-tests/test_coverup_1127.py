# file: lib/ansible/module_utils/urls.py:1146-1166
# asked: {"lines": [1148, 1149, 1152, 1154, 1155, 1156, 1157, 1158, 1161, 1162, 1164, 1165, 1166], "branches": [[1148, 1149], [1148, 1152], [1161, 1162], [1161, 1164]]}
# gained: {"lines": [1148, 1149, 1152, 1154, 1155, 1156, 1161, 1162, 1164, 1165, 1166], "branches": [[1148, 1149], [1148, 1152], [1161, 1162]]}

import pytest
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import UnsupportedAlgorithm
from ansible.module_utils.urls import get_channel_binding_cert_hash

class MockCertificate:
    def __init__(self, signature_hash_algorithm=None):
        self.signature_hash_algorithm = signature_hash_algorithm

def test_get_channel_binding_cert_hash_with_crypto(monkeypatch):
    # Mock HAS_CRYPTOGRAPHY to be True
    monkeypatch.setattr('ansible.module_utils.urls.HAS_CRYPTOGRAPHY', True)

    # Mock certificate_der
    certificate_der = b"dummy_certificate_der"

    # Mock x509.load_der_x509_certificate to return a mock certificate
    def mock_load_der_x509_certificate(data, backend):
        return MockCertificate(signature_hash_algorithm=hashes.SHA1())

    monkeypatch.setattr(x509, 'load_der_x509_certificate', mock_load_der_x509_certificate)

    # Call the function
    result = get_channel_binding_cert_hash(certificate_der)

    # Assert the result is not None and is of expected length
    assert result is not None
    assert len(result) == 32  # SHA256 produces a 32-byte hash

def test_get_channel_binding_cert_hash_without_crypto(monkeypatch):
    # Mock HAS_CRYPTOGRAPHY to be False
    monkeypatch.setattr('ansible.module_utils.urls.HAS_CRYPTOGRAPHY', False)

    # Mock certificate_der
    certificate_der = b"dummy_certificate_der"

    # Call the function
    result = get_channel_binding_cert_hash(certificate_der)

    # Assert the result is None
    assert result is None

def test_get_channel_binding_cert_hash_with_unsupported_algorithm(monkeypatch):
    # Mock HAS_CRYPTOGRAPHY to be True
    monkeypatch.setattr('ansible.module_utils.urls.HAS_CRYPTOGRAPHY', True)

    # Mock certificate_der
    certificate_der = b"dummy_certificate_der"

    # Mock x509.load_der_x509_certificate to return a mock certificate
    def mock_load_der_x509_certificate(data, backend):
        return MockCertificate(signature_hash_algorithm=None)

    monkeypatch.setattr(x509, 'load_der_x509_certificate', mock_load_der_x509_certificate)

    # Call the function
    result = get_channel_binding_cert_hash(certificate_der)

    # Assert the result is not None and is of expected length
    assert result is not None
    assert len(result) == 32  # SHA256 produces a 32-byte hash

def test_get_channel_binding_cert_hash_with_md5_algorithm(monkeypatch):
    # Mock HAS_CRYPTOGRAPHY to be True
    monkeypatch.setattr('ansible.module_utils.urls.HAS_CRYPTOGRAPHY', True)

    # Mock certificate_der
    certificate_der = b"dummy_certificate_der"

    # Mock x509.load_der_x509_certificate to return a mock certificate with md5 algorithm
    def mock_load_der_x509_certificate(data, backend):
        return MockCertificate(signature_hash_algorithm=hashes.MD5())

    monkeypatch.setattr(x509, 'load_der_x509_certificate', mock_load_der_x509_certificate)

    # Call the function
    result = get_channel_binding_cert_hash(certificate_der)

    # Assert the result is not None and is of expected length
    assert result is not None
    assert len(result) == 32  # SHA256 produces a 32-byte hash
