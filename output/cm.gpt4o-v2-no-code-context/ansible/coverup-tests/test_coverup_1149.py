# file: lib/ansible/module_utils/urls.py:1146-1166
# asked: {"lines": [1148, 1149, 1152, 1154, 1155, 1156, 1157, 1158, 1161, 1162, 1164, 1165, 1166], "branches": [[1148, 1149], [1148, 1152], [1161, 1162], [1161, 1164]]}
# gained: {"lines": [1148, 1149, 1152, 1154, 1155, 1156, 1161, 1162, 1164, 1165, 1166], "branches": [[1148, 1149], [1148, 1152], [1161, 1162], [1161, 1164]]}

import pytest
from unittest.mock import patch, MagicMock
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.x509 import Certificate
from cryptography.x509.oid import NameOID
import datetime
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import UnsupportedAlgorithm

# Assuming the function is imported from the module
from ansible.module_utils.urls import get_channel_binding_cert_hash

def generate_certificate():
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
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
        key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=10)
    ).sign(key, hashes.SHA256(), default_backend())
    return cert.public_bytes(Encoding.DER)

def test_get_channel_binding_cert_hash_no_cryptography(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.urls.HAS_CRYPTOGRAPHY', False)
    result = get_channel_binding_cert_hash(b'')
    assert result is None

def test_get_channel_binding_cert_hash_unsupported_algorithm(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.urls.HAS_CRYPTOGRAPHY', True)
    cert_der = generate_certificate()

    mock_cert = MagicMock(spec=Certificate)
    mock_cert.signature_hash_algorithm = None
    with patch('ansible.module_utils.urls.x509.load_der_x509_certificate', return_value=mock_cert):
        result = get_channel_binding_cert_hash(cert_der)
        assert result is not None

def test_get_channel_binding_cert_hash_md5_algorithm(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.urls.HAS_CRYPTOGRAPHY', True)
    cert_der = generate_certificate()

    mock_cert = MagicMock(spec=Certificate)
    mock_cert.signature_hash_algorithm.name = 'md5'
    with patch('ansible.module_utils.urls.x509.load_der_x509_certificate', return_value=mock_cert):
        result = get_channel_binding_cert_hash(cert_der)
        assert result is not None

def test_get_channel_binding_cert_hash_sha1_algorithm(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.urls.HAS_CRYPTOGRAPHY', True)
    cert_der = generate_certificate()

    mock_cert = MagicMock(spec=Certificate)
    mock_cert.signature_hash_algorithm.name = 'sha1'
    with patch('ansible.module_utils.urls.x509.load_der_x509_certificate', return_value=mock_cert):
        result = get_channel_binding_cert_hash(cert_der)
        assert result is not None

def test_get_channel_binding_cert_hash_supported_algorithm(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.urls.HAS_CRYPTOGRAPHY', True)
    cert_der = generate_certificate()

    mock_cert = MagicMock(spec=Certificate)
    mock_cert.signature_hash_algorithm = hashes.SHA256()
    with patch('ansible.module_utils.urls.x509.load_der_x509_certificate', return_value=mock_cert):
        result = get_channel_binding_cert_hash(cert_der)
        assert result is not None
