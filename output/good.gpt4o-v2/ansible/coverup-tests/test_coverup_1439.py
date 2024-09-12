# file: lib/ansible/module_utils/urls.py:1146-1166
# asked: {"lines": [], "branches": [[1161, 1164]]}
# gained: {"lines": [], "branches": [[1161, 1164]]}

import pytest
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.x509.oid import NameOID
from cryptography.exceptions import UnsupportedAlgorithm
import datetime

# Mock HAS_CRYPTOGRAPHY to ensure the code path is taken
HAS_CRYPTOGRAPHY = True

from ansible.module_utils.urls import get_channel_binding_cert_hash

def generate_certificate(signature_algorithm):
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    # Generate a self-signed certificate
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"mycompany.com"),
    ])
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        # Our certificate will be valid for 10 days
        datetime.datetime.utcnow() + datetime.timedelta(days=10)
    ).add_extension(
        x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
        critical=False,
    ).sign(private_key, hashes.SHA256(), default_backend())

    return cert.public_bytes(serialization.Encoding.DER)

def test_get_channel_binding_cert_hash_sha256():
    cert_der = generate_certificate(hashes.SHA256())
    result = get_channel_binding_cert_hash(cert_der)
    assert result is not None

def test_get_channel_binding_cert_hash_md5(monkeypatch):
    def mock_load_der_x509_certificate(data, backend):
        class MockCert:
            @property
            def signature_hash_algorithm(self):
                class MockAlgorithm:
                    name = 'md5'
                return MockAlgorithm()
        return MockCert()

    monkeypatch.setattr(x509, "load_der_x509_certificate", mock_load_der_x509_certificate)
    cert_der = generate_certificate(hashes.SHA256())
    result = get_channel_binding_cert_hash(cert_der)
    assert result is not None

def test_get_channel_binding_cert_hash_sha1(monkeypatch):
    def mock_load_der_x509_certificate(data, backend):
        class MockCert:
            @property
            def signature_hash_algorithm(self):
                class MockAlgorithm:
                    name = 'sha1'
                return MockAlgorithm()
        return MockCert()

    monkeypatch.setattr(x509, "load_der_x509_certificate", mock_load_der_x509_certificate)
    cert_der = generate_certificate(hashes.SHA256())
    result = get_channel_binding_cert_hash(cert_der)
    assert result is not None

def test_get_channel_binding_cert_hash_unsupported_algorithm(monkeypatch):
    def mock_load_der_x509_certificate(data, backend):
        class MockCert:
            @property
            def signature_hash_algorithm(self):
                raise UnsupportedAlgorithm("Unsupported algorithm")
        return MockCert()

    monkeypatch.setattr(x509, "load_der_x509_certificate", mock_load_der_x509_certificate)
    cert_der = generate_certificate(hashes.SHA256())
    result = get_channel_binding_cert_hash(cert_der)
    assert result is not None
