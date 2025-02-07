# file: lib/ansible/module_utils/urls.py:1146-1166
# asked: {"lines": [1157, 1158], "branches": [[1161, 1164]]}
# gained: {"lines": [1157, 1158], "branches": []}

import pytest
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import UnsupportedAlgorithm
from ansible.module_utils.urls import get_channel_binding_cert_hash

def test_get_channel_binding_cert_hash_with_unsupported_algorithm(monkeypatch):
    class MockCert:
        @property
        def signature_hash_algorithm(self):
            raise UnsupportedAlgorithm("Unsupported algorithm")

    def mock_load_der_x509_certificate(data, backend):
        return MockCert()

    monkeypatch.setattr(x509, "load_der_x509_certificate", mock_load_der_x509_certificate)

    certificate_der = b"dummy_certificate_der"
    result = get_channel_binding_cert_hash(certificate_der)
    assert result is not None

def test_get_channel_binding_cert_hash_with_md5_algorithm(monkeypatch):
    class MockHashAlgorithm:
        name = "md5"

    class MockCert:
        @property
        def signature_hash_algorithm(self):
            return MockHashAlgorithm()

    def mock_load_der_x509_certificate(data, backend):
        return MockCert()

    monkeypatch.setattr(x509, "load_der_x509_certificate", mock_load_der_x509_certificate)

    certificate_der = b"dummy_certificate_der"
    result = get_channel_binding_cert_hash(certificate_der)
    assert result is not None

def test_get_channel_binding_cert_hash_with_sha1_algorithm(monkeypatch):
    class MockHashAlgorithm:
        name = "sha1"

    class MockCert:
        @property
        def signature_hash_algorithm(self):
            return MockHashAlgorithm()

    def mock_load_der_x509_certificate(data, backend):
        return MockCert()

    monkeypatch.setattr(x509, "load_der_x509_certificate", mock_load_der_x509_certificate)

    certificate_der = b"dummy_certificate_der"
    result = get_channel_binding_cert_hash(certificate_der)
    assert result is not None
